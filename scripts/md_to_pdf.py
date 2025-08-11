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
            "extra",
            "fenced_code",
            "toc",
            "sane_lists",
            "smarty",
        ],
        output_format="html5",
    )

    html_doc = HTML_TEMPLATE.format(title=markdown_path.name, content=html_content)

    base_url = str(markdown_path.parent.resolve())

    stylesheets: list[CSS] = []
    if css_path and css_path.exists():
        stylesheets.append(CSS(filename=str(css_path)))
    else:
        stylesheets.append(CSS(string=DEFAULT_CSS))

    HTML(string=html_doc, base_url=base_url).write_pdf(
        target=str(pdf_path), stylesheets=stylesheets
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Markdown to PDF using WeasyPrint"
    )
    parser.add_argument(
        "markdown_file",
        type=Path,
        help="Path to the source Markdown file (e.g., README.md)",
    )
    parser.add_argument(
        "--output", "-o", type=Path, default=Path("CV.pdf"), help="Output PDF path"
    )
    parser.add_argument(
        "--css", type=Path, default=None, help="Optional CSS file for PDF styling"
    )
    args = parser.parse_args()

    convert_markdown_to_pdf(args.markdown_file, args.output, args.css)


if __name__ == "__main__":
    main()
