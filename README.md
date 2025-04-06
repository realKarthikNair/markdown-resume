# Markdown Resume to PDF Generator

*Build, style, and export your resume using just a text editor and a single command.*

This tool converts a Markdown resume (`resume.md`) into a styled PDF using HTML and CSS with the help of WeasyPrint.

---

## 📁 Project Structure

```
.
├── build.sh             # Shell script to sanitize and generate PDF
├── generate.py          # Main script to convert Markdown to PDF
├── resume.md            # Input resume in Markdown format
├── sanitize.py          # Script to clean/prepare the Markdown file
├── style.css            # External CSS for styling the PDF
├── style.html           # Base HTML template with placeholder for Markdown content
├── README.md            # Project documentation (this file)
```

---

## 🧩 Dependencies

You must have Python 3 and the following packages installed:

- `markdown`
- `weasyprint`

You can install them using pip:

```bash
pip install markdown weasyprint
```

> 💡 WeasyPrint may require additional system libraries like `libpango`, `cairo`, and `gdk-pixbuf` depending on your OS.

---

## ⚙️ Usage

### To generate the PDF:

```bash
chmod +x build.sh
./build.sh
```

This script will:

1. Run `sanitize.py` to clean `resume.md`
2. Convert it into HTML with styles using `generate.py`
3. Output `resume.pdf`
4. Clean up temporary files

---

## 📝 Customization

- **Edit `style.css`** to change how the PDF looks (fonts, margins, colors)
- **Edit `style.html`** to customize the HTML structure
- **Update `resume.md`** with your resume content in Markdown

___

## 📜 License

- BSD 3-Clause License : WeasyPrint
- BSD 3-Clause License : Markdown
- BSD 3-Clause License : This Project