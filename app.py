import os
import uuid
import base64
from datetime import datetime

import streamlit as st
from PIL import Image
import requests

from openai import OpenAI

# Alibaba Cloud OSS v2
import alibabacloud_oss_v2 as oss
from alibabacloud_oss_v2.models import PutObjectRequest

import config
from animal_data import (
    ANIMAL_CATEGORIES,
    ANIMALS_DATA,
    get_animals_by_category,
    get_animal_detail
)

# ------------------------------------
# Page config
# ------------------------------------
st.set_page_config(
    page_title="Global Animal Explorer",
    page_icon="🐾",
    layout="wide"
)

# ------------------------------------
# English UI labels for categories
# (UI-only; your data file can stay unchanged)
# ------------------------------------
CATEGORY_EN = {
    "mammals": {
        "name": "Mammals",
        "description": "Warm-blooded vertebrates that give live birth and nurse their young.",
    },
    "birds": {
        "name": "Birds",
        "description": "Feathered warm-blooded vertebrates, many capable of flight.",
    },
    "reptiles": {
        "name": "Reptiles",
        "description": "Cold-blooded vertebrates with scales, mostly egg-laying.",
    },
    "amphibians": {
        "name": "Amphibians",
        "description": "Animals that live both in water and on land with metamorphosis.",
    },
    "fish": {
        "name": "Fish",
        "description": "Aquatic vertebrates that breathe using gills.",
    },
    "insects": {
        "name": "Insects",
        "description": "Six-legged arthropods with exoskeletons.",
    },
}

# ------------------------------------
# Helpers
# ------------------------------------
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


def oss_is_configured() -> bool:
    required = [
        config.OSS_ACCESS_KEY_ID,
        config.OSS_ACCESS_KEY_SECRET,
        config.OSS_REGION,
        config.OSS_ENDPOINT,
        config.OSS_BUCKET,
    ]
    return all(bool(x) for x in required)


def upload_to_oss_bytes(file_bytes: bytes, object_name: str) -> dict:
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


def build_openai_client() -> OpenAI:
    if not config.DASHSCOPE_API_KEY:
        raise RuntimeError(
            "Missing DASHSCOPE_API_KEY. Set it in environment variables or Streamlit secrets."
        )
    return OpenAI(
        api_key=config.DASHSCOPE_API_KEY,
        base_url=config.DASHSCOPE_BASE_URL,
    )


def identify_animal(image_url: str) -> str:
    client = build_openai_client()

    prompt = (
        "Please carefully observe this image.\n"
        "If there is an animal, describe it in the following format:\n\n"
        "1. Animal name (common name + scientific name if possible)\n"
        "2. Key characteristics\n"
        "3. Behavior and lifestyle\n"
        "4. Habitat\n"
        "5. Interesting facts\n\n"
        "If there is no animal, briefly describe the main content of the image."
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


# ------------------------------------
# Global Encyclopedia (GBIF + Wikipedia)
# ------------------------------------
@st.cache_data(ttl=60 * 60)
def gbif_species_search(query: str, limit: int = 20):
    """
    Search GBIF species by name.
    """
    url = "https://api.gbif.org/v1/species/search"
    params = {"q": query, "limit": limit}
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    return data.get("results", [])


@st.cache_data(ttl=60 * 60)
def gbif_species_detail(key: int):
    """
    Get a single species record by GBIF key.
    """
    url = f"https://api.gbif.org/v1/species/{key}"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.json()


@st.cache_data(ttl=60 * 60)
def wikipedia_summary(title: str):
    """
    Fetch an English summary from Wikipedia REST API.
    """
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    r = requests.get(url, timeout=15)
    if r.status_code != 200:
        return None
    return r.json()


def best_wikipedia_title(gbif_record: dict):
    """
    Try to guess a good Wikipedia title from GBIF record.
    Usually the scientific name works best.
    """
    sci = gbif_record.get("scientificName")
    canonical = gbif_record.get("canonicalName")
    return canonical or sci


# ------------------------------------
# UI blocks
# ------------------------------------
def render_home():
    st.title("🐾 Global Animal Explorer")

    st.markdown(
        """
This app includes three parts:

1) **Featured Animals** — a curated mini-encyclopedia from your local dataset.  
2) **Global Animal Encyclopedia** — search millions of species via live biodiversity databases.  
3) **Image Animal Identifier** — upload an image and let a vision model describe the animal.

This structure is how you realistically get *“almost all animals in the world”* in a Streamlit app.
"""
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Featured animals (local)", len(ANIMALS_DATA))
    with c2:
        st.metric("Global coverage", "Millions (via GBIF)")
    with c3:
        st.metric("Image upload", "Up to 16 MB")


def render_featured_categories():
    st.title("🗂️ Featured Animal Categories")

    cols = st.columns(3)
    i = 0
    for cat_id, info in ANIMAL_CATEGORIES.items():
        en = CATEGORY_EN.get(cat_id, {})
        name = en.get("name", cat_id.title())
        desc = en.get("description", info.get("description", ""))

        with cols[i % 3]:
            st.markdown(f"### {name}")
            st.caption(desc)
            st.write(f"Estimated species count: **{info.get('count', 'N/A')}**")

            if st.button(f"Open {name}", key=f"open_{cat_id}"):
                st.session_state["page"] = "featured_category"
                st.session_state["category_id"] = cat_id
        i += 1


def render_featured_category_detail(category_id: str):
    if category_id not in ANIMAL_CATEGORIES:
        st.error("Category not found.")
        return

    info = ANIMAL_CATEGORIES[category_id]
    en = CATEGORY_EN.get(category_id, {})
    name = en.get("name", category_id.title())
    desc = en.get("description", info.get("description", ""))

    animals = get_animals_by_category(category_id)

    st.title(f"📌 {name}")
    st.caption(desc)

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
                st.write(short[:120] + ("..." if len(short) > 120 else ""))

            if st.button("View details", key=f"feat_detail_{animal_id}"):
                st.session_state["page"] = "featured_animal"
                st.session_state["animal_id"] = animal_id


def render_featured_animal_detail(animal_id: str):
    animal = get_animal_detail(animal_id)
    if not animal:
        st.error("Animal not found.")
        return

    category_info = ANIMAL_CATEGORIES.get(animal.get("category", ""), {})
    cat_en = CATEGORY_EN.get(animal.get("category", ""), {})

    st.title(f"🦁 {animal.get('name', animal_id)}")
    if animal.get("scientific_name"):
        st.caption(animal["scientific_name"])

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        if animal.get("image"):
            st.image(animal["image"], use_container_width=True)

        st.markdown(f"**Category:** {cat_en.get('name', animal.get('category', ''))}")
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


def render_global_encyclopedia():
    st.title("🌍 Global Animal Encyclopedia")

    st.markdown(
        """
Search for *almost any animal species* using live global biodiversity data.

Data flow:
- **GBIF** provides taxonomy and species backbone records.
- **Wikipedia** provides readable science summaries when available.
"""
    )

    query = st.text_input("Search by common name or scientific name", placeholder="e.g., tiger, Panthera tigris, emperor penguin")

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
        with st.spinner("Searching global databases..."):
            results = gbif_species_search(query, limit=limit)

        # Soft filtering for animals: we can't perfectly filter by kingdom in all cases,
        # but we can prioritize Animalia.
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

                colA, colB = st.columns([1, 1])

                with colA:
                    if st.button("Load GBIF details", key=f"gbif_{key}"):
                        detail = gbif_species_detail(key)
                        st.json(detail)

                with colB:
                    wp_title = best_wikipedia_title(r)
                    if wp_title:
                        if st.button("Load Wikipedia summary", key=f"wp_{key}"):
                            summ = wikipedia_summary(wp_title)
                            if not summ:
                                st.warning("Wikipedia summary not found for this title.")
                            else:
                                # display summary and image if present
                                st.markdown(f"#### {summ.get('title', wp_title)}")
                                if summ.get("thumbnail", {}).get("source"):
                                    st.image(summ["thumbnail"]["source"], use_container_width=True)
                                text = summ.get("extract")
                                if text:
                                    st.write(text)
                                else:
                                    st.info("No summary text available.")
                    else:
                        st.caption("No Wikipedia title guess available.")

    except Exception as e:
        st.error(f"Global search failed: {e}")


def render_identifier():
    st.title("🧠 Image Animal Identifier")

    st.markdown(
        """
Upload an image and the model will identify animals and provide nature-science notes.

If OSS is configured, the image will be uploaded and analyzed by public URL.  
Otherwise the app will try a base64 data-URL fallback.
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

        if oss_is_configured():
            st.info("Uploading to OSS...")
            object_name = f"animal-images/{timestamp}/{unique_name}"
            up = upload_to_oss_bytes(file_bytes, object_name)

            if not up["success"]:
                st.warning("OSS upload failed. Falling back to base64 data URL.")
                image_url = read_image_as_data_url(uploaded)
            else:
                image_url = up["url"]
                st.success("Uploaded to OSS.")
                st.caption(image_url)
        else:
            image_url = read_image_as_data_url(uploaded)

        with st.spinner("Identifying..."):
            result_text = identify_animal(image_url)

        st.markdown("### Model result")
        st.write(result_text)

    except Exception as e:
        st.error(f"Failed to process image: {e}")


# ------------------------------------
# State + navigation
# ------------------------------------
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

    if st.sidebar.button("🌍 Global Encyclopedia"):
        st.session_state["page"] = "global"

    if st.sidebar.button("🧠 Identify an Image"):
        st.session_state["page"] = "identify"

    st.sidebar.markdown("---")
    st.sidebar.caption("Secrets should be stored in environment variables or Streamlit secrets.")


def main():
    ensure_state()
    sidebar_nav()

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
