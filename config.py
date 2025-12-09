import os

# -----------------------------
# DashScope / Qwen (OpenAI-compatible)
# -----------------------------
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
DASHSCOPE_BASE_URL = os.getenv(
    "DASHSCOPE_BASE_URL",
    "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# Model name may change over time. Keep it configurable.
QWEN_MODEL = os.getenv("QWEN_MODEL", "qwen3-vl-plus")


# -----------------------------
# Alibaba Cloud OSS
# -----------------------------
OSS_ACCESS_KEY_ID = os.getenv("OSS_ACCESS_KEY_ID", "")
OSS_ACCESS_KEY_SECRET = os.getenv("OSS_ACCESS_KEY_SECRET", "")
OSS_REGION = os.getenv("OSS_REGION", "cn-shanghai")
OSS_ENDPOINT = os.getenv("OSS_ENDPOINT", "oss-cn-shanghai.aliyuncs.com")
OSS_BUCKET = os.getenv("OSS_BUCKET", "")


# -----------------------------
# App settings
# -----------------------------
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "temp_uploads")

ALLOWED_EXTENSIONS = {
    "png", "jpg", "jpeg", "gif", "bmp", "webp"
}

MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
