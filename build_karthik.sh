./build.sh -i docs/resume_karthik.md -o docs/resume_karthik.pdf --sanitize false
./src/sanitize.py -i docs/resume_karthik.md -o docs/resume.md
./build.sh -i docs/resume_karthik.md -o docs/resume_sanitized.pdf --sanitize true