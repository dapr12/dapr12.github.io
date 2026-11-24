# Post-render step: Quarto appends " – <site title>" to every page <title>.
# Pages listed in PAGES set a complete title of their own ("A | B"), so strip
# the suffix from those only. Other pages keep Quarto's default behaviour.
import os
import re

out_dir = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site")
PAGES = ["index.html", "books.html"]

for page in PAGES:
    path = os.path.join(out_dir, page)
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8") as f:
        html = f.read()
    fixed = re.sub(r"<title>([^<|]+\|[^<]+?) – [^<]+</title>", r"<title>\1</title>", html, count=1)
    if fixed != html:
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed)
