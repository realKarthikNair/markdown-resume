import argparse
import os
import subprocess
import sys

def show_help():
    print("Usage: ./build.py -i <input_file> -o <output_file> [--sanitize true|false]")
    print("")
    print("Options:")
    print("  -i           Input markdown file (e.g., resume.md)")
    print("  -o           Output PDF file (e.g., resume.pdf)")
    print("  --sanitize   Whether to sanitize input before generating PDF (default: false)")
    print("  --help       Show this help message")
    print("Example usage:")
    print("python build.py -i resume.md -o resume.pdf --sanitize true")

def main():
    input_file = ""
    output_file = ""
    sanitize = "false"

    parser = argparse.ArgumentParser(description="Convert Markdown resume to PDF", add_help=False)
    parser.add_argument("-i", dest="input", help="Input markdown file")
    parser.add_argument("-o", dest="output", help="Output PDF file")
    parser.add_argument("--sanitize", dest="sanitize", default="false", help="Whether to sanitize input")
    parser.add_argument("--help", action="store_true", help="Show help message")
    
    args = parser.parse_args()
    
    if args.help:
        show_help()
        sys.exit(0)
    
    input_file = args.input
    output_file = args.output
    sanitize = args.sanitize
    
    if not input_file or not output_file:
        print("Error: Both input and output files are required.")
        show_help()
        sys.exit(1)
    
    if sanitize == "true":
        sanitized = f"{os.path.splitext(input_file)[0]}_sanitized.md"
        print(f"[*] Sanitizing {input_file}...")
        subprocess.run(["python", "src/sanitize.py", "-i", input_file, "-o", sanitized], check=True)
        input_file = sanitized
    
    print("[*] Generating PDF...")
    subprocess.run(["python", "src/generate.py", "-i", input_file, "-o", output_file], check=True)
    
    if sanitize == "true":
        print("[*] Cleaning up sanitized file...")
        os.remove(input_file)
    
    print(f"[+] Done. PDF saved to {output_file}")

if __name__ == "__main__":
    main()