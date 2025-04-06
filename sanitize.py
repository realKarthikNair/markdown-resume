#!/usr/bin/python

import re, argparse

def mask(m: re.Match) -> str:
    s = m.group()
    cc = re.match(r'^\+?\d{1,3}', s)
    cc_str = cc.group() if cc else ''
    digits = re.sub(r'\D', '', s[len(cc_str):])
    return f"{cc_str} {digits[:5]}{'*'*(len(digits)-5)}"

def main():
    p = argparse.ArgumentParser()
    p.add_argument('-i', '--input', required=True)
    p.add_argument('-o', '--output', required=True)
    a = p.parse_args()

    with open(a.input, 'r', encoding='utf-8') as f: text = f.read()
    masked = re.sub(r'(\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,5}[-.\s]?\d{4,6}', mask, text)
    with open(a.output, 'w', encoding='utf-8') as f: f.write(masked)

    print(f"✅ Phone numbers partially masked and saved to {a.output}")

if __name__ == '__main__':
    main()
