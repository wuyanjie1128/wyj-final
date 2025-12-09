import os
import uuid
import base64
from datetime import datetime

import streamlit as st
from PIL import Image

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


# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Animal Explorer & Identifier",
    page_icon="🐾",
    layout="wide"
)


# -----------------------------
# Helpers
# -----------------------------
def allowed_file(filename: str) -> bool:
    if not filename or "." not in filename:
        return False
    ext = filename.rsplit(".", 1)[1].lower()
    return ext in config.ALLOWED_EXTENSIONS


def read_image_as_data_url(uploaded_file) -> str:
    """
    Convert uploaded image to a data URL.
    This avoids requiring external hosting when OSS is not configured.
    """
    raw = uploaded_file.getvalue()
    b64 = base64.b64encode(raw).decode("utf-8")

    # Try to infer MIME
    ext = uploaded_file.name.rsplit(".", 1)[1].lower() if "." in uploaded_file.name else "jpeg"
    mime = "image/jpeg"
    if ext in ("png",):
        mime = "image/png"
    elif ext in ("webp",):
        mime = "image/webp"
    elif ext in ("gif",):
        mime = "image/gif"
    elif ext in ("bmp",):
        mime = "image/bmp"

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
    """
    Upload bytes to Alibaba Cloud OSS.
    Returns dict with success/url/error.
    """
    try:
        cfg = oss.config.load_default()
        cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(
            access_key_id=config.OSS_ACCESS_KEY_ID,
            access_key_secret=config.OSS_ACCESS_KEY_SECRET
        )
        cfg.region = config.OSS_REGION
        cfg.endpoint = config.OSS_ENDPOINT

        client = oss.Client(cfg)

        # The v2 SDK supports put object from bytes via client.put_object
        # But signatures may vary by version; safest is to use a temp file.
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
    """
    Build an OpenAI-compatible client for DashScope/Qwen.
    """
    if not config.DASHSCOPE_API_KEY:
        raise RuntimeError("Missing DASHSCOPE_API_KEY. Set it in environment variables or secrets.")
    return OpenAI(
        api_key=config.DASHSCOPE_API_KEY,
        base_url=config.DASHSCOPE_BASE_URL,
    )


def identify_animal(image_url: str) -> str:
    """
    Call Qwen vision model via OpenAI-compatible API.
    Returns model text.
    """
    client = build_openai_client()

    prompt = (
        "Please carefully observe this image.\n"
        "If there is an animal, describe it in the following format:\n\n"
        "1. Animal name (Chinese + scientific name if possible)\n"
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


# -----------------------------
# UI components
# -----------------------------
def render_home():
    st.title("🐾 Animal Explorer & Identifier")

    st.markdown(
        """
This app combines:
- **Animal science popularization (encyclopedia)** by category.
- **Image-based animal identification** using a vision LLM.

You can deploy this on **Streamlit Community Cloud** directly from GitHub.
"""
    )

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("📚 Encyclopedia")
        st.write("Browse categories and learn about representative animals.")
        st.write(f"Total animals in current dataset: **{len(ANIMALS_DATA)}**")

    with col2:
        st.subheader("🧠 Image Identifier")
        st.write("Upload an image and let the model describe animals found in it.")
        if oss_is_configured():
            st.success("OSS config detected: uploaded images will be hosted on OSS.")
        else:
            st.info("OSS not configured: the app will try a base64 data-URL fallback.")


def render_category_list():
    st.title("🗂️ Animal Categories")

    cols = st.columns(3)
    i = 0
    for cat_id, info in ANIMAL_CATEGORIES.items():
        with cols[i % 3]:
            st.markdown(f"### {info.get('name', cat_id)}")
            st.caption(info.get("description", ""))
            st.write(f"Estimated species count: **{info.get('count', 'N/A')}**")
            if st.button(f"Open {info.get('name', cat_id)}", key=f"open_{cat_id}"):
                st.session_state["page"] = "category"
                st.session_state["category_id"] = cat_id
        i += 1


def render_category_detail(category_id: str):
    if category_id not in ANIMAL_CATEGORIES:
        st.error("Category not found.")
        return

    info = ANIMAL_CATEGORIES[category_id]
    animals = get_animals_by_category(category_id)

    st.title(f"📌 {info.get('name', category_id)}")
    st.caption(info.get("description", ""))

    if not animals:
        st.info("No animals in this category yet.")
        return

    st.markdown("### Animals in this category")
    animal_items = list(animals.items())

    # Grid-like display
    cols = st.columns(3)
    for idx, (animal_id, animal) in enumerate(animal_items):
        with cols[idx % 3]:
            st.markdown(f"#### {animal.get('name', animal_id)}")
            img = animal.get("image")
            if img:
                st.image(img, use_container_width=True)
            st.caption(animal.get("scientific_name", ""))
            short = animal.get("description", "")
            if short:
                st.write(short[:120] + ("..." if len(short) > 120 else ""))

            if st.button("View details", key=f"detail_{animal_id}"):
                st.session_state["page"] = "animal"
                st.session_state["animal_id"] = animal_id


def render_animal_detail_page(animal_id: str):
    animal = get_animal_detail(animal_id)
    if not animal:
        st.error("Animal not found.")
        return

    category_info = ANIMAL_CATEGORIES.get(animal.get("category", ""), {})

    st.title(f"🦁 {animal.get('name', animal_id)}")
    st.caption(animal.get("scientific_name", ""))

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


def render_identifier():
    st.title("🧠 Image Animal Identifier")

    st.markdown(
        """
Upload an image (png / jpg / jpeg / gif / bmp / webp).
The app will:
- optionally upload it to OSS (if configured),
- then call a vision model to identify animals and provide science notes.
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
        # Show preview
        image = Image.open(uploaded)
        st.image(image, caption="Uploaded image", use_container_width=True)

        file_bytes = uploaded.getvalue()
        unique_ext = uploaded.name.rsplit(".", 1)[1].lower()
        unique_name = f"{uuid.uuid4().hex}.{unique_ext}"
        timestamp = datetime.now().strftime("%Y%m%d")

        # Decide URL strategy
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

        # Call model
        with st.spinner("Identifying..."):
            result_text = identify_animal(image_url)

        st.markdown("### Model result")
        st.write(result_text)

    except Exception as e:
        st.error(f"Failed to process image: {e}")


# -----------------------------
# Simple router (single-file app)
# -----------------------------
def ensure_state():
    if "page" not in st.session_state:
        st.session_state["page"] = "home"
    if "category_id" not in st.session_state:
        st.session_state["category_id"] = None
    if "animal_id" not in st.session_state:
        st.session_state["animal_id"] = None


def sidebar_nav():
    st.sidebar.title("Navigation")

    if st.sidebar.button("🏠 Home"):
        st.session_state["page"] = "home"

    if st.sidebar.button("🗂️ Categories"):
        st.session_state["page"] = "categories"

    if st.sidebar.button("🧠 Identify an Image"):
        st.session_state["page"] = "identify"

    st.sidebar.markdown("---")
    st.sidebar.caption("Tip: Configure secrets via environment variables or Streamlit secrets.")


def main():
    ensure_state()
    sidebar_nav()

    page = st.session_state["page"]

    if page == "home":
        render_home()
    elif page == "categories":
        render_category_list()
    elif page == "category":
        render_category_detail(st.session_state.get("category_id"))
    elif page == "animal":
        render_animal_detail_page(st.session_state.get("animal_id"))
    elif page == "identify":
        render_identifier()
    else:
        render_home()


if __name__ == "__main__":
    main()
