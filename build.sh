#!/bin/bash

set -e

show_help() {
  echo "Usage: ./build.sh -i <input_file> -o <output_file> [--sanitize true|false]"
  echo ""
  echo "Options:"
  echo "  -i           Input markdown file (e.g., resume.md)"
  echo "  -o           Output PDF file (e.g., resume.pdf)"
  echo "  --sanitize   Whether to sanitize input before generating PDF (default: false)"
  echo "  --help       Show this help message"
  echo "Example usage:"
  echo "./build.sh -i resume.md -o resume.pdf --sanitize true"
}


# Default values
INPUT=""
OUTPUT=""
SANITIZE="false"

# Parse arguments
while [[ "$#" -gt 0 ]]; do
  case $1 in
    -i) INPUT="$2"; shift ;;
    -o) OUTPUT="$2"; shift ;;
    --sanitize) SANITIZE="$2"; shift ;;
    --help) show_help; exit 0 ;;
    *) echo "Unknown option: $1"; show_help; exit 1 ;;
  esac
  shift
done

if [[ -z "$INPUT" || -z "$OUTPUT" ]]; then
  echo "Error: Both input and output files are required."
  show_help
  exit 1
fi

# Check sanitize option
if [[ "$SANITIZE" == "true" ]]; then
  SANITIZED="${INPUT%.md}_sanitized.md"
  echo "[*] Sanitizing $INPUT..."
  python3 sanitize.py -i "$INPUT" -o "$SANITIZED"
  INPUT="$SANITIZED"
fi

echo "[*] Generating PDF..."
./generate.py -i "$INPUT" -o "$OUTPUT"

if [[ "$SANITIZE" == "true" ]]; then
  echo "[*] Cleaning up sanitized file..."
  rm "$INPUT"
fi

echo "[+] Done. PDF saved to $OUTPUT"