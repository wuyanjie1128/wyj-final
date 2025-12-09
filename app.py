import os
import uuid
import base64
from datetime import datetime

import streamlit as st
from PIL import Image
import requests

from openai import OpenAI

import config
from animal_data import (
    ANIMAL_CATEGORIES,
    ANIMALS_DATA,
    get_animals_by_category,
    get_animal_detail
)

# -----------------------------
# Optional OSS import
# -----------------------------
OSS_AVAILABLE = True
try:
    import alibabacloud_oss_v2 as oss
    from alibabacloud_oss_v2.models import PutObjectRequest
except Exception:
    OSS_AVAILABLE = False


# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Global Animal Explorer",
    page_icon="🐾",
    layout="wide"
)


# -----------------------------
# File helpers
# -----------------------------
def allowed_file(filename: str) -> bool:
    if not filename or "." not in filename:
        return False
    ext = filename.rsplit(".", 1)[1].lower()
    return ext in config.ALLOWED_EXTENSIONS


def read_image_as_data_url(uploaded_file) -> str:
    raw = uploaded_file.getvalue()
    b64 = base64.b64encode(raw).decode("utf-8")

    ext = uploaded_file.name.rsplit(".", 1)[1].lower() if "." in uploaded_file.name else "jpeg"
    mime = {
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "webp": "image/webp",
        "gif": "image/gif",
        "bmp": "image/bmp",
    }.get(ext, "image/jpeg")

    return f"data:{mime};base64,{b64}"


# -----------------------------
# OSS helpers (optional)
# -----------------------------
def oss_is_configured() -> bool:
    if not OSS_AVAILABLE:
        return False

    required = [
        config.OSS_ACCESS_KEY_ID,
        config.OSS_ACCESS_KEY_SECRET,
        config.OSS_REGION,
        config.OSS_ENDPOINT,
        config.OSS_BUCKET,
    ]
    return all(bool(x) for x in required)


def upload_to_oss_bytes(file_bytes: bytes, object_name: str) -> dict:
    if not OSS_AVAILABLE:
        return {"success": False, "error": "OSS library not available."}

    try:
        cfg = oss.config.load_default()
        cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(
            access_key_id=config.OSS_ACCESS_KEY_ID,
            access_key_secret=config.OSS_ACCESS_KEY_SECRET
        )
        cfg.region = config.OSS_REGION
        cfg.endpoint = config.OSS_ENDPOINT

        client = oss.Client(cfg)

        os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)
        tmp_name = f"{uuid.uuid4().hex}.bin"
        tmp_path = os.path.join(config.UPLOAD_FOLDER, tmp_name)

        with open(tmp_path, "wb") as f:
            f.write(file_bytes)

        result = client.put_object_from_file(
            PutObjectRequest(bucket=config.OSS_BUCKET, key=object_name),
            tmp_path
        )

        try:
            os.remove(tmp_path)
        except OSError:
            pass

        file_url = f"https://{config.OSS_BUCKET}.{config.OSS_ENDPOINT}/{object_name}"
        return {"success": True, "url": file_url, "etag": getattr(result, "etag", None)}
    except Exception as e:
        return {"success": False, "error": str(e)}


# -----------------------------
# DashScope key handling
# -----------------------------
def get_dashscope_api_key() -> str:
    """
    Priority:
    1) Runtime input (sidebar)
    2) Streamlit secrets
    3) Environment variables via config.py
    """
    key = st.session_state.get("runtime_dashscope_key", "").strip()
    if key:
        st.session_state["dashscope_key_source"] = "sidebar"
        return key

    try:
        if "DASHSCOPE_API_KEY" in st.secrets:
            sec = str(st.secrets["DASHSCOPE_API_KEY"]).strip()
            if sec:
                st.session_state["dashscope_key_source"] = "secrets"
                return sec
    except Exception:
        pass

    cfg = (config.DASHSCOPE_API_KEY or "").strip()
    if cfg:
        st.session_state["dashscope_key_source"] = "env"
        return cfg

    st.session_state["dashscope_key_source"] = "none"
    return ""


def build_openai_client():
    key = get_dashscope_api_key()
    if not key:
        return None

    return OpenAI(
        api_key=key,
        base_url=config.DASHSCOPE_BASE_URL,
    )


# -----------------------------
# Offline fallback (optional)
# -----------------------------
def identify_animal_local(pil_image: Image.Image) -> str:
    """
    No-key fallback using ImageNet classification.
    Works only if torch/torchvision are installed (local mode).
    Will not crash the app if not available.
    """
    try:
        import torch
        from torchvision import models

        weights = models.MobileNet_V3_Large_Weights.DEFAULT
        model = models.mobilenet_v3_large(weights=weights)
        model.eval()
        preprocess = weights.transforms()
        categories = weights.meta.get("categories", [])

        img = pil_image.convert("RGB")
        batch = preprocess(img).unsqueeze(0)

        with torch.no_grad():
            logits = model(batch)
            probs = torch.softmax(logits, dim=1)[0]

        topk = torch.topk(probs, k=5)

        preds = []
        for score, idx in zip(topk.values.tolist(), topk.indices.tolist()):
            label = categories[idx] if idx < len(categories) else f"class_{idx}"
            preds.append((label, score))

        # Helpful mustelid interpretation (for ferret-like cases)
        mustelid_keywords = {"weasel", "polecat", "mink", "otter", "stoat", "ermine"}
        top_labels = [p[0].lower() for p in preds]
        mustelid_hit = any(any(k in lab for k in mustelid_keywords) for lab in top_labels)

        lines = []
        lines.append("**Offline no-key result (best effort):**")
        lines.append("")
        for label, score in preds:
            pct = round(score * 100, 1)
            lines.append(f"- {label} — {pct}%")

        if mustelid_hit:
            lines.append("")
            lines.append(
                "**Interpretation:** The model suggests a *mustelid-type animal* "
                "(weasel/polecat/mink/otter). "
                "If your pet is small, elongated, and domesticated, "
                "**it could very likely be a ferret**."
            )

        lines.append("")
        lines.append(
            "**Note:** This offline classifier is general-purpose. "
            "Species-level accuracy is limited compared with cloud vision models."
        )
        return "\n".join(lines)

    except Exception:
        return (
            "Offline no-key identification is not available on this deployment.\n\n"
            "This is expected on Streamlit Cloud.\n"
            "For stronger no-key results, run locally with:\n"
            "`pip install -r requirements-local.txt`"
        )


# -----------------------------
# Cloud vision (ambiguity-aware)
# -----------------------------
def identify_animal_cloud(image_url: str) -> str:
    client = build_openai_client()
    if client is None:
        return ""

    prompt = (
        "You are an expert wildlife identifier.\n"
        "Carefully analyze the image.\n\n"
        "If an animal is present, produce an ambiguity-aware identification.\n"
        "Return the following format in English:\n\n"
        "Top candidates:\n"
        "1) <Common name> (<scientific name if possible>) — <confidence %>\n"
        "2) <Common name> (<scientific name if possible>) — <confidence %>\n"
        "3) <Common name> (<scientific name if possible>) — <confidence %>\n\n"
        "Rules:\n"
        "- Confidence values should be reasonable and sum to about 100%.\n"
        "- If the animal is very clear, you may provide 1 dominant candidate and 1 minor alternative.\n"
        "- Explicitly handle common look-alike groups:\n"
        "  octopus/squid/cuttlefish, sea otter/river otter,\n"
        "  raccoon/red panda, sea lion/seal/walrus.\n\n"
        "Then provide:\n"
        "• Key visual cues used\n"
        "• Short natural history notes (habitat, behavior)\n"
        "• One interesting fact\n\n"
        "If no animal is present, briefly describe the main content."
    )

    completion = client.chat.completions.create(
        model=config.QWEN_MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": image_url}},
                    {"type": "text", "text": prompt},
                ],
            }
        ],
    )

    return completion.choices[0].message.content


def identify_animal(image_url: str, pil_image: Image.Image) -> str:
    """
    Robust two-level strategy:
    - If cloud key works -> cloud result
    - Otherwise -> offline attempt
    """
    try:
        text = identify_animal_cloud(image_url)
        if text:
            return text
    except Exception:
        pass

    return identify_animal_local(pil_image)


# -----------------------------
# Global Encyclopedia (GBIF only)
# -----------------------------
@st.cache_data(ttl=60 * 60)
def gbif_species_search(query: str, limit: int = 20):
    url = "https://api.gbif.org/v1/species/search"
    params = {"q": query, "limit": limit}
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    return data.get("results", [])


@st.cache_data(ttl=60 * 60)
def gbif_species_detail(key: int):
    url = f"https://api.gbif.org/v1/species/{key}"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.json()


# -----------------------------
# UI: Home
# -----------------------------
def render_home():
    st.title("🐾 Global Animal Explorer")

    st.markdown(
        """
This app includes three parts:

1) **Featured Animals** — a curated local mini-encyclopedia.  
2) **Global Animal Encyclopedia (GBIF)** — search millions of species.  
3) **Image Animal Identifier** — robust design for GitHub + Streamlit Cloud.

**With a valid DashScope API key:** richer results + look-alike confidence ranking.  
**Without a key:** best-effort offline fallback (fully available in local mode).
"""
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Featured animals (local)", len(ANIMALS_DATA))
    with c2:
        st.metric("Global coverage", "Millions (GBIF)")
    with c3:
        st.metric("Image upload", "Up to 16 MB")


# -----------------------------
# UI: Featured Categories
# -----------------------------
def render_featured_categories():
    st.title("🗂️ Featured Animal Categories")

    cols = st.columns(3)
    i = 0
    for cat_id, info in ANIMAL_CATEGORIES.items():
        featured_count = len(get_animals_by_category(cat_id))

        with cols[i % 3]:
            st.markdown(f"### {info.get('name', cat_id.title())}")
            st.caption(info.get("description", ""))
            st.write(f"Estimated species count worldwide: **{info.get('count', 'N/A')}**")
            st.write(f"Featured examples in this category: **{featured_count}**")

            if st.button(f"Open {info.get('name', cat_id.title())}", key=f"open_{cat_id}"):
                st.session_state["page"] = "featured_category"
                st.session_state["category_id"] = cat_id
        i += 1


def render_featured_category_detail(category_id: str):
    if category_id not in ANIMAL_CATEGORIES:
        st.error("Category not found.")
        return

    info = ANIMAL_CATEGORIES[category_id]
    animals = get_animals_by_category(category_id)

    st.title(f"📌 {info.get('name', category_id.title())}")
    st.caption(info.get("description", ""))

    if not animals:
        st.info("No featured animals in this category yet.")
        return

    st.markdown("### Featured animals")
    animal_items = list(animals.items())
    cols = st.columns(3)

    for idx, (animal_id, animal) in enumerate(animal_items):
        with cols[idx % 3]:
            st.markdown(f"#### {animal.get('name', animal_id)}")
            img = animal.get("image")
            if img:
                st.image(img, use_container_width=True)

            sci = animal.get("scientific_name", "")
            if sci:
                st.caption(sci)

            short = animal.get("description", "")
            if short:
                st.write(short[:140] + ("..." if len(short) > 140 else ""))

            if st.button("View details", key=f"feat_detail_{animal_id}"):
                st.session_state["page"] = "featured_animal"
                st.session_state["animal_id"] = animal_id


def render_featured_animal_detail(animal_id: str):
    animal = get_animal_detail(animal_id)
    if not animal:
        st.error("Animal not found.")
        return

    category_info = ANIMAL_CATEGORIES.get(animal.get("category", ""), {})

    st.title(f"🦁 {animal.get('name', animal_id)}")
    if animal.get("scientific_name"):
        st.caption(animal["scientific_name"])

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        if animal.get("image"):
            st.image(animal["image"], use_container_width=True)

        st.markdown(f"**Category:** {category_info.get('name', animal.get('category', ''))}")
        st.markdown(f"**Conservation status:** {animal.get('conservation_status', 'N/A')}")
        st.markdown(f"**Habitat:** {animal.get('habitat', 'N/A')}")
        st.markdown(f"**Distribution:** {animal.get('distribution', 'N/A')}")
        st.markdown(f"**Population:** {animal.get('population', 'N/A')}")

    with col2:
        st.markdown("### Overview")
        st.write(animal.get("description", ""))

        st.markdown("### Key characteristics")
        for c in animal.get("characteristics", []):
            st.write(f"- {c}")

        st.markdown("### Interesting facts")
        for f in animal.get("facts", []):
            st.write(f"- {f}")

        if animal.get("threats"):
            st.markdown("### Main threats")
            for t in animal.get("threats", []):
                st.write(f"- {t}")


# -----------------------------
# UI: Global Encyclopedia (GBIF)
# -----------------------------
def render_global_encyclopedia():
    st.title("🌍 Global Animal Encyclopedia (GBIF)")

    st.markdown(
        "Search for *almost any animal species* using live global biodiversity data from GBIF."
    )

    query = st.text_input(
        "Search by common name or scientific name",
        placeholder="e.g., ferret, Mustela putorius furo, tiger, Panthera tigris"
    )

    col_filters = st.columns([1, 1, 1])
    with col_filters[0]:
        limit = st.slider("Max results", 5, 50, 20)
    with col_filters[1]:
        rank_filter = st.selectbox(
            "Rank filter (optional)",
            ["Any", "SPECIES", "GENUS", "FAMILY", "ORDER", "CLASS", "PHYLUM", "KINGDOM"]
        )
    with col_filters[2]:
        only_animals_hint = st.checkbox("Prefer animals (soft hint)", value=True)

    if not query:
        st.info("Type a name to start searching.")
        return

    try:
        with st.spinner("Searching GBIF..."):
            results = gbif_species_search(query, limit=limit)

        if only_animals_hint:
            animalia = [r for r in results if (r.get("kingdom") == "Animalia")]
            others = [r for r in results if (r.get("kingdom") != "Animalia")]
            results = animalia + others

        if rank_filter != "Any":
            results = [r for r in results if r.get("rank") == rank_filter]

        if not results:
            st.warning("No results found. Try a different keyword.")
            return

        st.markdown("### Search results")

        for r in results[:limit]:
            key = r.get("key")
            canonical = r.get("canonicalName") or r.get("scientificName", "Unknown")
            rank = r.get("rank", "N/A")
            kingdom = r.get("kingdom", "N/A")
            family = r.get("family", "")
            genus = r.get("genus", "")

            with st.expander(f"{canonical}  •  {rank}  •  {kingdom}", expanded=False):
                st.write(f"**GBIF key:** {key}")
                if family:
                    st.write(f"**Family:** {family}")
                if genus:
                    st.write(f"**Genus:** {genus}")

                if st.button("Load GBIF details", key=f"gbif_{key}"):
                    detail = gbif_species_detail(key)
                    st.json(detail)

    except Exception as e:
        st.error(f"Global search failed: {e}")


# -----------------------------
# UI: Image Identifier
# -----------------------------
def render_identifier():
    st.title("🧠 Image Animal Identifier")

    st.markdown(
        """
Upload an image and get an identification.

- **With a valid DashScope API key:** richer results + look-alike confidence rankings.  
- **Without a key:** offline best-effort guesses (fully available in local mode).
"""
    )

    uploaded = st.file_uploader(
        "Upload an image",
        type=list(config.ALLOWED_EXTENSIONS),
        accept_multiple_files=False
    )

    if not uploaded:
        return

    if not allowed_file(uploaded.name):
        st.error("Unsupported file type.")
        return

    try:
        image = Image.open(uploaded)
        st.image(image, caption="Uploaded image", use_container_width=True)

        file_bytes = uploaded.getvalue()
        unique_ext = uploaded.name.rsplit(".", 1)[1].lower()
        unique_name = f"{uuid.uuid4().hex}.{unique_ext}"
        timestamp = datetime.now().strftime("%Y%m%d")

        # Prefer OSS URL if fully configured, else base64
        if oss_is_configured():
            object_name = f"animal-images/{timestamp}/{unique_name}"
            up = upload_to_oss_bytes(file_bytes, object_name)
            image_url = up["url"] if up.get("success") else read_image_as_data_url(uploaded)
        else:
            image_url = read_image_as_data_url(uploaded)

        with st.spinner("Identifying..."):
            result_text = identify_animal(image_url, pil_image=image)

        st.markdown("### Result")
        st.write(result_text)

    except Exception as e:
        st.error(f"Failed to process image: {e}")


# -----------------------------
# Sidebar
# -----------------------------
def render_sidebar_key_box():
    st.sidebar.markdown("### 🔑 Optional Vision Upgrade")

    st.sidebar.text_input(
        "DashScope API Key (optional)",
        type="password",
        key="runtime_dashscope_key",
        help=(
            "Do NOT commit keys to GitHub. "
            "For Streamlit Cloud, set it in Secrets."
        )
    )

    key = get_dashscope_api_key()
    source = st.session_state.get("dashscope_key_source", "unknown")

    if key:
        st.sidebar.success(f"Cloud vision enabled (source: {source}).")
        st.sidebar.caption(f"Key preview: ****{key[-4:]}")
    else:
        st.sidebar.info("No key detected. Using lightweight mode.")

    if not OSS_AVAILABLE:
        st.sidebar.caption("OSS library not detected (image upload will use base64).")


# -----------------------------
# State + navigation
# -----------------------------
def ensure_state():
    st.session_state.setdefault("page", "home")
    st.session_state.setdefault("category_id", None)
    st.session_state.setdefault("animal_id", None)


def sidebar_nav():
    st.sidebar.title("Navigation")

    if st.sidebar.button("🏠 Home"):
        st.session_state["page"] = "home"

    if st.sidebar.button("⭐ Featured Encyclopedia"):
        st.session_state["page"] = "featured_categories"

    if st.sidebar.button("🌍 Global Encyclopedia (GBIF)"):
        st.session_state["page"] = "global"

    if st.sidebar.button("🧠 Identify an Image"):
        st.session_state["page"] = "identify"

    st.sidebar.markdown("---")


def main():
    ensure_state()
    sidebar_nav()
    render_sidebar_key_box()

    page = st.session_state["page"]

    if page == "home":
        render_home()
    elif page == "featured_categories":
        render_featured_categories()
    elif page == "featured_category":
        render_featured_category_detail(st.session_state.get("category_id"))
    elif page == "featured_animal":
        render_featured_animal_detail(st.session_state.get("animal_id"))
    elif page == "global":
        render_global_encyclopedia()
    elif page == "identify":
        render_identifier()
    else:
        render_home()


if __name__ == "__main__":
    main()
