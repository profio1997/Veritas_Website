#!/usr/bin/env python3
"""Wrap page.html in a full HTML document for hosting anywhere (Netlify, Vercel,
GitHub Pages, S3, any static host).

    python3 build_site.py [https://your-domain.example]

Writes site/index.html and copies assets/ into site/assets/. page.html stays the
single source: it is also what gets published to the claude.ai preview link.
Pass the final site URL so the share-card image resolves to an absolute address.
"""
import pathlib
import re
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE / "site"
base = (sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "")

body = (HERE / "page.html").read_text(encoding="utf-8")
# The hosted page gets the public-facing title; the preview keeps its own.
body = re.sub(r"<title>.*?</title>\s*", "", body, count=1, flags=re.S)
# Remove the page's own description meta; the full head below carries it.
body = re.sub(r'<meta name="description"[^>]*>\s*', "", body, count=1)
if base:
    # The success screen's share link points at the real site, not wherever it is opened.
    body = body.replace('var SHARE_URL = "";', f'var SHARE_URL = "{base}/";', 1)
desc = ("Veritas reads anything to you in your own voice, then checks what you "
        "understood and brings back what you missed. Launching December 2026.")
og_img = f"{base}/assets/og-image.jpg" if base else "assets/og-image.jpg"
canonical = f'<link rel="canonical" href="{base}/">\n<meta property="og:url" content="{base}/">\n' if base else ""
head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Veritas · Master what you read.</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B0B0C">
{canonical}<meta property="og:type" content="website">
<meta property="og:title" content="Veritas · Master what you read.">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="assets/icon.svg">
</head>
<body>
"""
SITE.mkdir(exist_ok=True)
(SITE / "index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
if (SITE / "assets").exists():
    shutil.rmtree(SITE / "assets")
shutil.copytree(HERE / "assets", SITE / "assets")
icon = HERE.parent.parent / "brand" / "source" / "laurel-waveform-mark-on-dark.svg"
if icon.exists():
    shutil.copy(icon, SITE / "assets" / "icon.svg")
print("wrote", SITE / "index.html")
