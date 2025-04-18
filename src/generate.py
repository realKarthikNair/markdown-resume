#!/usr/bin/env python3

import argparse
from typing import Tuple
from markdown import markdown
from weasyprint import HTML, CSS


def parse_args() -> Tuple[str, str]:
    """
    Parse command-line arguments for input markdown file and output PDF path.

    Returns:
        Tuple[str, str]: input Markdown file path and output PDF file path
    """
    parser = argparse.ArgumentParser(description="Convert Markdown resume to styled PDF.")
    parser.add_argument("-i", "--input", required=True, help="Path to input Markdown file")
    parser.add_argument("-o", "--output", default="output.pdf", help="Path to output PDF file")
    args = parser.parse_args()
    return args.input, args.output


def read_markdown_file(path: str) -> str:
    """
    Read the contents of the Markdown file.

    Args:
        path (str): Path to the Markdown file

    Returns:
        str: Markdown content as string
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def convert_markdown_to_html(md_text: str, html_path: str) -> str:
    """
    Convert Markdown text to styled HTML content.

    Args:
        md_text (str): Markdown input text
        html_path (str): Path to the HTML file for styling

    Returns:
        str: Full HTML document with styling and converted content
    """
    with open(html_path, "r", encoding="utf-8") as f:
        base_html = f.read()

    content_html = markdown(md_text, extensions=["extra"])
    full_html = base_html.replace("<!--CONTENT-->", content_html)
    return full_html


def generate_pdf(html_content: str, output_path: str, css_path: str) -> None:
    """
    Generate a PDF from HTML content using WeasyPrint.

    Args:
        html_content (str): Full HTML content
        output_path (str): Output file path for the PDF
        css_path (str): Path to the CSS file for styling
    """
    HTML(string=html_content).write_pdf(
        output_path,
        stylesheets=[CSS(css_path)]
    )


def main():
    input_md, output_pdf = parse_args()
    md_text = read_markdown_file(input_md)
    html = convert_markdown_to_html(md_text, "src/skeleton.html")
    generate_pdf(html, output_pdf, "src/style.css")
    print(f"✅ PDF generated: {output_pdf}")


if __name__ == "__main__":
    main()
    