./build.sh -i resume_karthik.md -o resume_karthik.pdf --sanitize false
./sanitize.py -i resume_karthik.md -o resume.md
./build.sh -i resume_karthik.md -o resume_sanitized.pdf --sanitize true