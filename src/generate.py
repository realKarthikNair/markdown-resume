#!/usr/bin/env python3

import argparse
import re
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


def preprocess_markdown(md_text: str) -> str:
    """
    Preprocess markdown text to format dates for right alignment.
    
    Args:
        md_text (str): Original markdown text
        
    Returns:
        str: Processed markdown text with formatted dates
    """
    # Convert ::text:: to <center>text</center>
    md_text = re.sub(r'::(.*?)::', r'<center>\1</center>', md_text, flags=re.DOTALL)
    
    # Convert {text} to <u>text</u>
    md_text = re.sub(r'\{(.*?)\}', r'<u>\1</u>', md_text, flags=re.DOTALL)
    
    # Format heading with project and date: "#### **Project Name** (July 2025 - Present)" -> "#### **Project Name** <span class="date">July 2025 - Present</span>"
    md_text = re.sub(r'(#+\s*\*\*[^*]+\*\*)\s*\(([A-Za-z]+\s+[0-9]{4}\s*-\s*[A-Za-z]+(?:\s+[0-9]{4})?|[A-Za-z]+\s+[0-9]{4}\s*-\s*Present)\)', 
                     r'\1 <span class="date">\2</span>', 
                     md_text)

    # Format dates after pipe in headings: "### Institution | Date Range"
    md_text = re.sub(r'(#+\s+[^|]+)\|\s*([A-Za-z]+\s+[0-9]{4}\s*-\s*[A-Za-z]+(?:\s+[0-9]{4})?|[A-Za-z]+\s+[0-9]{4}\s*-\s*Present)', 
                     r'\1| <span class="date">\2</span>', 
                     md_text)

    # Format project dates in list items: "* **Project Name** (Date Range): Description"
    md_text = re.sub(r'(\* \*\*[^*]+\*\*)\s*\(([A-Za-z]+\s+[0-9]{4}\s*-\s*[A-Za-z]+(?:\s+[0-9]{4})?|[A-Za-z]+\s+[0-9]{4}\s*-\s*Present)\):', 
                     r'\1 <span class="date">\2</span>:', 
                     md_text)
    
    md_text = re.sub(r'(#+\s+[^|]+(?:\|[^|]+)?)\|\s*([A-Za-z]+\s+[0-9]{4}\s*-\s*[A-Za-z]+\s+[0-9]{4}|[A-Za-z]+\s+[0-9]{4}\s*-\s*Present)', 
                     r'\1| <span class="date">\2</span>', 
                     md_text)
    
    # Format year ranges with pipe separator: "| 2020-2023" -> "<span class="date">2020-2023</span>"
    md_text = re.sub(r'\|\s*([0-9]{4}[-–][0-9]{4}|[0-9]{4}\s*-\s*Present)', r' <span class="date">\1</span>', md_text)
    
    # Format month/year to present in brackets: "[January 2020–Present]" -> "<span class="date">January 2020–Present</span>"
    md_text = re.sub(r'\[([A-Za-z]+\s+[0-9]{4}[-–][A-Za-z]+|[A-Za-z]+\s+[0-9]{4}[-–][0-9]{4})\]', r' <span class="date">\1</span>', md_text)
    
    # Format dates in parentheses with colon: "(April 2025 - May 2025):" -> "<span class="date">April 2025 - May 2025</span>:"
    md_text = re.sub(r'\(([A-Za-z]+\s+[0-9]{4}\s*-\s*[A-Za-z]+\s+[0-9]{4}|[A-Za-z]+\s+[0-9]{4}\s*-\s*[A-Za-z]+|[A-Za-z]+\s+[0-9]{4}\s*-\s*[0-9]{4}|[A-Za-z]+\s+[0-9]{4}\s*-\s*Present)\):', r'<span class="date">\1</span>:', md_text)
    
    # Format single year at end of line: "| 2021" -> "<span class="date">2021</span>"
    md_text = re.sub(r'\|\s*([0-9]{4})\s*$', r' <span class="date">\1</span>', md_text, flags=re.MULTILINE)
    
    # Format dates after dash: "– (May 2022– December 2023)" -> "– <span class="date">May 2022– December 2023</span>"
    md_text = re.sub(r'–\s*\(([A-Za-z]+\s+[0-9]{4}[-–][A-Za-z]+\s+[0-9]{4}|[A-Za-z]+\s+[0-9]{4}[-–][A-Za-z]+|[A-Za-z]+\s+[0-9]{4}[-–][0-9]{4})\)', r'– <span class="date">\1</span>', md_text)
    
    # Format standalone month/year: "June 2023" at end of line -> "<span class="date">June 2023</span>"
    md_text = re.sub(r'(?<![A-Za-z])([A-Za-z]+\s+[0-9]{4})$', r'<span class="date">\1</span>', md_text, flags=re.MULTILINE)
    
    # Format day-specific dates: "June 15, 2023" -> "<span class="date">June 15, 2023</span>"
    md_text = re.sub(r'([A-Za-z]+\s+[0-9]{1,2},\s+[0-9]{4})$', r'<span class="date">\1</span>', md_text, flags=re.MULTILINE)
    
    # Format quarter-based dates: "Q2 2023" -> "<span class="date">Q2 2023</span>"
    md_text = re.sub(r'(Q[1-4]\s+[0-9]{4})$', r'<span class="date">\1</span>', md_text, flags=re.MULTILINE)
    
    # Format academic years: "2023/2024" -> "<span class="date">2023/2024</span>"
    md_text = re.sub(r'([0-9]{4}/[0-9]{4})$', r'<span class="date">\1</span>', md_text, flags=re.MULTILINE)
    
    # Format seasonal references: "Summer 2023" -> "<span class="date">Summer 2023</span>"
    md_text = re.sub(r'((Spring|Summer|Fall|Winter|Autumn)\s+[0-9]{4})$', r'<span class="date">\1</span>', md_text, flags=re.MULTILINE)
    
    # Format month ranges within same year: "Jan-Mar 2023" -> "<span class="date">Jan-Mar 2023</span>"
    md_text = re.sub(r'([A-Za-z]{3,}-[A-Za-z]{3,}\s+[0-9]{4})$', r'<span class="date">\1</span>', md_text, flags=re.MULTILINE)
    
    # Format date ranges with "to" instead of dash: "2020 to 2023" -> "<span class="date">2020 to 2023</span>"
    md_text = re.sub(r'([0-9]{4}\s+to\s+[0-9]{4})$', r'<span class="date">\1</span>', md_text, flags=re.MULTILINE)
    
    # Format ISO dates: "2023-06-15" -> "<span class="date">2023-06-15</span>"
    md_text = re.sub(r'([0-9]{4}-[0-9]{2}-[0-9]{2})$', r'<span class="date">\1</span>', md_text, flags=re.MULTILINE)

    return md_text

def convert_markdown_to_html(md_text: str, html_path: str) -> str:
    """
    Convert Markdown text to styled HTML content.

    Args:
        md_text (str): Markdown input text
        html_path (str): Path to the HTML file for styling

    Returns:
        str: Full HTML document with styling and converted content
    """
    processed_md = preprocess_markdown(md_text)
    
    with open(html_path, "r", encoding="utf-8") as f:
        base_html = f.read()

    content_html = markdown(processed_md, extensions=["extra"])
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