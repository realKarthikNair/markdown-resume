So many Resume builders out there, but I wanted something that

- requires just a text editor to edit the resume
- could be customized easily through CSS
- a CLI command to generate the PDF

This repo will now serve as a repo for my own resume (minus phone number) and of course the script to generate it. 

# Markdown Resume to PDF Generator

*Build, style, and export your resume using just a text editor and a single command.*

This tool converts a Markdown resume (`resume.md`) into a styled PDF using HTML and CSS with the help of WeasyPrint.

---

## 🧩 Setting up

### Windows specific setup (mandatory)

```
curl -L https://github.com/msys2/msys2-installer/releases/download/2025-02-21/msys2-x86_64-20250221.exe -o mysys.exe
```

Run the installer and follow the instructions to install MSYS2.

in MSYS2’s shell, execute `pacman -S mingw-w64-x86_64-pango`

Close MSYS2’s shell.

### Install Dependencies (all platforms)

You must have Python 3 and `markdown` and `weasyprint` packages installed.

```bash
pip install -r requirements.txt
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

1. Linux:
   
```bash
chmod +x build.sh
# run
/build.sh -i docs/resume.md -o docs/resume_sanitized.pdf --sanitize true # false if you want to skip sanitization
```

2. Windows

```
rem run without sanitization
python .\build.py -i .\docs\resume.md -o .\docs\resume.pdf
rem run with sanitization
python .\build.py -i .\docs\resume.md -o .\docs\resume_sanitized.pdf --sanitize true
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