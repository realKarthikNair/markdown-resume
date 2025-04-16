So many Resume builders out there, but I wanted something that's

- minimal and doesn't require a complex setup
- requires just a text editor to edit the resume
- a CLI command to generate the PDF

This repo will now serve as a repo for my own resume (minus phone number) and of course the script to generate it. 

> ⚠️ This tool doesn't work on Windows yet. See [#1](https://github.com/realKarthikNair/markdown-resume/issues/1)

# Markdown Resume to PDF Generator

*Build, style, and export your resume using just a text editor and a single command.*

This tool converts a Markdown resume (`resume.md`) into a styled PDF using HTML and CSS with the help of WeasyPrint.

---

## 🧩 Dependencies

You must have Python 3 and the following packages installed:

- `markdown`
- `weasyprint`

You can install them using pip:

```bash
pip install markdown weasyprint
```

> 💡 On Linux WeasyPrint may require additional system libraries like `libpango`, `cairo`, and `gdk-pixbuf` depending on your OS.

---

## ⚙️ Usage

### Edit your Resume

1. Open `docs/resume.md` in your favorite text editor (e.g., VSCode, Notepad, Vim).
2. Update the content with your personal information, education, work experience, projects, skills, awards, and languages.
3. Save the changes.

> 💡 You might need to know Markdown syntax to customize the format. Read [this](./docs/markdown_basics.pdf) to learn it in 4 minutes

### (optional) Edit CSS

1. Open `src/style.css` to customize the appearance of your PDF.

### To generate the PDF:

1. Linux/macOS:
   
```bash
chmod +x build.sh
# run
/build.sh -i docs/resume.md -o docs/resume_sanitized.pdf --sanitize true # false if you want to skip sanitization
```

2. Windows

```
rem run without sanitization
build.bat -i docs/resume.md -o docs/resume.pdf
rem run with sanitization
build.bat -i docs/resume.md -o docs/resume.pdf --sanitize true
```

> `sanitize` flag when true, builds the resume with phone number masked. This is useful if you want to share your resume publicly without exposing your phone number.

---

## 📝 Customization

- **Edit `src/style.css`** to change how the PDF looks (fonts, margins, colors)
- **Update `docs/resume.md`** with your resume content in Markdown

___

## 📜 License

- BSD 3-Clause License : WeasyPrint
- BSD 3-Clause License : Markdown
- BSD 3-Clause License : This Project