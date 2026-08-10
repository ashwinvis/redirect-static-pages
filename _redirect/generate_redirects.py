#!/usr/bin/env python3
"""
Generate redirect HTML pages for all HTML files in the directory.
Uses Jinja2 template to create pages that redirect from ashwinvis.github.io to fluid.quest.
"""

# /// script
# dependencies = ["jinja2"]
# ///

import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# Configuration
OLD_DOMAIN = "old.fluid.quest"
NEW_DOMAIN = "example.com"
PROTOCOL = "https://"
## If top-level repo like username.github.io
# PATH_PREFIX = "/"
## In this case
PATH_PREFIX = "/redirect-static-pages/"

# Paths
SCRIPT_DIR = Path(__file__).parent
BASE_DIR = SCRIPT_DIR.parent
TEMPLATE_PATH = SCRIPT_DIR / "redirect-template.html"

# Find all HTML files (excluding the _redirect_template directory)
html_files = []
for root, _, files in os.walk(BASE_DIR):
    root_path = Path(root)
    # Skip the _redirect_template directory
    if '_redirect_template' in root_path.parts:
        continue
    for file in files:
        if file.endswith(".html") and not file.startswith("."):
            full_path = root_path / file
            # Calculate relative path from BASE_DIR
            rel_path = full_path.relative_to(BASE_DIR)
            html_files.append(rel_path)

# Skip the template itself and index files we'll handle specially
skip_files = ["redirect-template.html", "redirect-config.html"]
html_files = [f for f in html_files if f.name not in skip_files]

# Set up Jinja2 environment
env = Environment(
    loader=FileSystemLoader(SCRIPT_DIR),
    autoescape=False
)
template = env.get_template("redirect-template.html")

# Generate each redirect page
for html_file in html_files:
    # Compute the path for the meta refresh
    # NOTE: the following special case may need correction
    # if there are other index.html pages
    if html_file.name in ("index.html", "404.html"):
        path = PATH_PREFIX
    else:
        path = PATH_PREFIX + str(html_file)

    # Render template
    content = template.render(
        old_domain=OLD_DOMAIN,
        new_domain=NEW_DOMAIN,
        protocol=PROTOCOL,
        path=path
    )

    # Write to file
    output_path = BASE_DIR / html_file
    output_path.write_text(content)
    print(f"Generated: {html_file}")

print(f"\nTotal files generated: {len(html_files)}")
