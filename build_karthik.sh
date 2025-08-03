./build.sh -i docs/resume_karthik.md -o docs/KarthikNair.pdf --sanitize false
cp docs/KarthikNair.pdf $HOME/RESUME/KarthikNair.pdf
./io_push.sh #personal script to push unmasked resume to somewhere
./src/sanitize.py -i docs/resume_karthik.md -o docs/resume.md
./build.sh -i docs/resume_karthik.md -o docs/KarthikNair_sanitized.pdf --sanitize true