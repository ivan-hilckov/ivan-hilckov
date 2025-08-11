## Goal

Build a tiny Python tool (managed with `uv`) that converts `README.md` into a styled PDF.

## Overview (the simplest reliable path)

- Convert Markdown → HTML in Python using the `markdown` package
- Render HTML → PDF using `WeasyPrint`

This approach is pure-Python at the code level and yields good, CSS-styled PDFs. It does require a few system libraries that `WeasyPrint` uses for layout and fonts (see Prerequisites).

## Prerequisites (macOS)

These are needed by WeasyPrint’s rendering engine.

```bash
brew install cairo pango gdk-pixbuf libffi
```

If you do not want any native prerequisites, consider the alternative plan using Pandoc below.

## Project setup with uv

```bash
# 1) Initialize the project if not already
uv init

# 2) Add runtime dependencies
uv add markdown weasyprint

# 3) (Optional) Add dev tooling
uv add --dev ruff
```

This will create/update `pyproject.toml` and lock dependencies with `uv.lock`.

## Libraries and their roles

- `markdown`: Parses `README.md` and converts Markdown to HTML. Supports extensions like tables and fenced code blocks.
- `weasyprint`: Renders HTML + CSS into a high-quality PDF.

## Minimal file layout

```
.
├─ pyproject.toml
├─ README.md       # source markdown to convert
├─ scripts/
│  └─ md_to_pdf.py # conversion script (example below)
└─ styles/
   └─ pdf.css      # optional CSS for nicer PDF styling
```

You can keep everything inline (single Python file) for the most minimal setup; extracting CSS makes styling easier to iterate on.

## Example implementation (copy-paste ready)

Create `scripts/md_to_pdf.py` with:

````python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import markdown
from weasyprint import HTML, CSS


DEFAULT_CSS = """
@page {
  size: A4;
  margin: 20mm;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  color: #111;
}

h1, h2, h3, h4 {
  margin-top: 1.4em;
}

code, pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

pre {
  background: #f6f8fa;
  padding: 12px;
  overflow-x: auto;
  border-radius: 6px;
}

table {
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid #ddd;
}

th, td {
  padding: 6px 10px;
}
"""


HTML_TEMPLATE = """<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>{title}</title>
  </head>
  <body>
    {content}
  </body>
  </html>
"""


def convert_markdown_to_pdf(
    markdown_path: Path,
    pdf_path: Path,
    css_path: Path | None = None,
) -> None:
    text = markdown_path.read_text(encoding="utf-8")
    html_content = markdown.markdown(
        text,
        extensions=[
            "extra",          # tables, attributes
            "fenced_code",   # ``` code blocks
            "toc",           # table of contents (if you include [TOC])
            "sane_lists",
            "smarty",        # nice quotes/dashes
        ],
        output_format="html5",
    )

    html_doc = HTML_TEMPLATE.format(title=markdown_path.name, content=html_content)

    # Base URL ensures local images like ![img](path.png) resolve relative to the README location
    base_url = str(markdown_path.parent.resolve())

    stylesheets = []
    if css_path and css_path.exists():
        stylesheets.append(CSS(filename=str(css_path)))
    else:
        stylesheets.append(CSS(string=DEFAULT_CSS))

    HTML(string=html_doc, base_url=base_url).write_pdf(target=str(pdf_path), stylesheets=stylesheets)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF using WeasyPrint")
    parser.add_argument("markdown_file", type=Path, help="Path to the source Markdown file (e.g., README.md)")
    parser.add_argument("--output", "-o", type=Path, default=Path("output.pdf"), help="Output PDF path")
    parser.add_argument("--css", type=Path, default=None, help="Optional CSS file for PDF styling")
    args = parser.parse_args()

    convert_markdown_to_pdf(args.markdown_file, args.output, args.css)


if __name__ == "__main__":
    main()
````

Optional: create `styles/pdf.css` if you want to customize styles:

```css
/* styles/pdf.css */
@page {
  size: A4;
  margin: 18mm;
}
body {
  font: 12pt/1.5 -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica,
    Arial, sans-serif;
}
h1 {
  font-size: 24pt;
}
h2 {
  font-size: 18pt;
}
pre {
  background: #f7f7f7;
  padding: 10px;
  border-radius: 6px;
}
```

## Run it (with uv)

```bash
# Using the project’s environment
uv run python scripts/md_to_pdf.py README.md -o README.pdf

# With custom CSS
uv run python scripts/md_to_pdf.py README.md -o README.pdf --css styles/pdf.css
```

If the PDF renders without images, double-check that images referenced in `README.md` are reachable from the file’s directory and that `base_url` is set to that directory (as in the example).

## Key points and caveats

- Markdown to HTML is done entirely in Python, so you get predictable behavior and can tweak extensions.
- PDF quality depends on HTML+CSS; adjust CSS for print (page size, margins, fonts, code blocks).
- WeasyPrint requires system libraries (installed once via Homebrew on macOS). If you see font or rendering issues, ensure `cairo`, `pango`, and `gdk-pixbuf` are properly installed.

## Alternative: Pandoc-based conversion (very simple, requires Pandoc binary)

If you prefer to avoid HTML/CSS or already have Pandoc:

```bash
brew install pandoc
uv add pypandoc
```

Then a tiny script like:

```python
import pypandoc
from pathlib import Path

def md_to_pdf_pandoc(src: str, dst: str) -> None:
    pypandoc.convert_file(src, to="pdf", outputfile=dst)

if __name__ == "__main__":
    md_to_pdf_pandoc("README.md", "README.pdf")
```

Pros: dead-simple. Cons: depends on the external `pandoc` executable (and sometimes LaTeX for certain templates).

## What to commit

- `pyproject.toml`, `uv.lock`
- `scripts/md_to_pdf.py`
- `styles/pdf.css` (optional)
- Update `README.md` if you want to document usage

Example:

```bash
git add PLAN.md scripts/md_to_pdf.py styles/pdf.css pyproject.toml uv.lock
git commit -m "Add Markdown→PDF plan and script using uv, markdown, WeasyPrint"
```
