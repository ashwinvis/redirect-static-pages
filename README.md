# Redirect Page Generator

Don't let your old links break!

This project contains the template and script for generating redirect HTML pages.
Useful for migrating website, documentation from GitHub pages, or in principle any 
static-site generator hosts to a different domain. Use a service worker to redirect
and a HTML `<meta>` tag as fallback.

## Files

- `redirect-template.html` - Jinja2 template for redirect pages
- `generate_redirects.py` - Python script to generate all redirect pages
- `redirect-config.js` - JavaScript configuration used by Service Worker `sw.js`

## Usage

To regenerate all redirect HTML pages:

```bash
uv run _redirect/generate_redirects.py
```

This will:
1. Find all `.html` files in the repository root directory (excluding `_redirect/`)
2. Generate redirect pages using the Jinja2 template
3. Overwrite existing HTML files with redirect pages

## Configuration

The domains are configured in `redirect-config.js` and `generate_redirects.py`:
- `OLD_DOMAIN`: old.fluid.quest
- `NEW_DOMAIN`: example.com
- `PROTOCOL`: https://
- `PATH_PREFIX` (see `generate_redirects.py`. Only useful for generating `<meta>` tags)

The template uses these values dynamically to avoid hardcoding.

## Redirect Mechanism

Each generated HTML page includes:
1. Meta refresh tag (3-second delay)
2. JavaScript immediate redirect
3. Fallback clickable link
4. Reference to Service Worker for HTTP 307 redirects


## References

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/307
- https://developer.mozilla.org/en-US/docs/Web/API/Response/redirect_static

- Inspiration: https://4042302.org/
