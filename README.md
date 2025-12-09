# Global Animal Explorer 🐾

A fully English Streamlit app featuring:
- **Featured Animals** (curated local mini-encyclopedia)
- **Global Animal Encyclopedia** powered by **GBIF**
- **Image Animal Identifier**
  - Works on Streamlit Cloud
  - Optional upgrade to DashScope/Qwen vision
  - Local offline fallback (stronger in local mode)

---

## Features

### 1) Featured Encyclopedia
A curated set of representative animals across:
- Mammals
- Birds
- Reptiles
- Amphibians
- Fish
- Insects

### 2) Global Animal Encyclopedia (GBIF)
Search millions of global species records using the GBIF taxonomic backbone.

### 3) Image Animal Identifier
Two-layer design:
- **With a valid DashScope API key**
  - Rich identification
  - **Look-alike top candidates + confidence**
- **Without a key**
  - Best-effort offline fallback
  - Fully enabled when running locally with `requirements-local.txt`

---

## Quick Start (Local)

```bash
pip install -r requirements-local.txt
streamlit run app.py
