# Post-render step: Quarto appends " – <site title>" to every page <title>.
# The homepage sets a complete title of its own ("Name | Role"), so strip the
# suffix from index.html only. Other pages keep Quarto's default behaviour.
import os
import re

out_dir = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site")
path = os.path.join(out_dir, "index.html")

if os.path.exists(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    fixed = re.sub(r"<title>([^<|]+\|[^<]+?) – [^<]+</title>", r"<title>\1</title>", html, count=1)
    if fixed != html:
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed)
