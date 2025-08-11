#!/usr/bin/env python3
from __future__ import annotations

import argparse
import webbrowser
from pathlib import Path
from typing import List

from flask import Flask, Response, make_response
import markdown


def build_app(project_root: Path, markdown_file: Path, css_path: Path) -> Flask:
    app = Flask(
        __name__,
        static_folder=str(project_root),
        static_url_path="/",
    )

    markdown_extensions: List[str] = [
        "extra",
        "fenced_code",
        "toc",
        "sane_lists",
        "smarty",
    ]

    html_template = """<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>{title}</title>
    <link rel=\"stylesheet\" href=\"{css_href}\" media=\"all\" />
    <style>
      /* Helpful for debugging print layout in the browser */
      @media screen {{
        body {{
          max-width: 800px;
          margin: 24px auto;
          padding: 0 16px;
          background: #fff;
        }}
      }}
    </style>
  </head>
  <body>
    {content}
  </body>
</html>
"""

    @app.route("/")
    def index() -> Response:
        text = markdown_file.read_text(encoding="utf-8")
        html_content = markdown.markdown(
            text,
            extensions=markdown_extensions,
            output_format="html5",
        )

        html_doc = html_template.format(
            title=str(markdown_file.name),
            css_href="/" + str(css_path.relative_to(project_root)).replace("\\", "/"),
            content=html_content,
        )

        response = make_response(html_doc)
        # Disable caching so refresh reflects latest changes
        response.headers["Cache-Control"] = (
            "no-store, no-cache, must-revalidate, max-age=0"
        )
        response.headers["Pragma"] = "no-cache"
        return response

    return app


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run a local preview server to debug README.md with PDF CSS.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8765,
        help="Port to run the server on (default: 8765)",
    )
    parser.add_argument(
        "--markdown",
        type=Path,
        default=Path("README.md"),
        help="Path to the Markdown file to preview (default: README.md)",
    )
    parser.add_argument(
        "--css",
        type=Path,
        default=Path("styles/pdf.css"),
        help="Path to the CSS file used for PDF styling (default: styles/pdf.css)",
    )
    args = parser.parse_args()

    project_root = Path.cwd()
    markdown_file = (project_root / args.markdown).resolve()
    css_file = (project_root / args.css).resolve()

    if not markdown_file.exists():
        raise FileNotFoundError(f"Markdown file not found: {markdown_file}")
    if not css_file.exists():
        raise FileNotFoundError(f"CSS file not found: {css_file}")

    app = build_app(
        project_root=project_root, markdown_file=markdown_file, css_path=css_file
    )

    url = f"http://127.0.0.1:{args.port}/"
    try:
        webbrowser.open(url)
    except Exception:
        pass

    # Run development server
    app.run(host="127.0.0.1", port=args.port, debug=False)


if __name__ == "__main__":
    main()
