#!/bin/bash

set -e

show_help() {
  echo "Usage: ./build.sh -i <input_file> -o <output_file>"
  echo ""
  echo "Options:"
  echo "  -i    Input markdown file (e.g., resume.md)"
  echo "  -o    Output PDF file (e.g., resume.pdf)"
  echo "  --help  Show this help message"
}

# Default values
INPUT=""
OUTPUT=""

# Parse arguments
while [[ "$#" -gt 0 ]]; do
  case $1 in
    -i) INPUT="$2"; shift ;;
    -o) OUTPUT="$2"; shift ;;
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

echo "[*] Generating PDF..."
./generate.py -i "$INPUT" -o "$OUTPUT"

echo "[+] Done. PDF saved to $OUTPUT"
