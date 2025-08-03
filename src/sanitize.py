#!/usr/bin/python

import re, argparse

def mask(m: re.Match) -> str:
    s = m.group()
    cc = re.match(r'^\+?\d{1,3}', s)
    cc_str = cc.group() if cc else ''
    digits = re.sub(r'\D', '', s[len(cc_str):])
    return f"{cc_str} {digits[:5]}{'\\*'*(len(digits)-5)}"

def is_in_url(text, match_start, match_end):
    """Check if the match is inside a URL or markdown link (but allow tel: links)"""
    before_match = text[:match_start]
    
    # mask tel: links
    tel_pattern = r'tel:\+?\d*$'
    if re.search(tel_pattern, before_match):
        return False  
    
    # dont mask if in a URL
    url_pattern = r'https?://[^\s\]]*$'
    if re.search(url_pattern, before_match):
        return True

    # dont mask if in a markdown link thats not a tel: link
    markdown_pattern = r'\[[^\]]*\]\((?!tel:)[^\s]*$'
    if re.search(markdown_pattern, before_match):
        return True
    
    return False

def main():
    p = argparse.ArgumentParser()
    p.add_argument('-i', '--input', required=True)
    p.add_argument('-o', '--output', required=True)
    a = p.parse_args()

    with open(a.input, 'r', encoding='utf-8') as f: 
        text = f.read()
    
    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,5}[-.\s]?\d{4,6}'
    
    def safe_mask(match):
        if is_in_url(text, match.start(), match.end()):
            return match.group()  # Don't mask if in URL
        return mask(match)
    
    masked = re.sub(phone_pattern, safe_mask, text)
    
    with open(a.output, 'w', encoding='utf-8') as f: 
        f.write(masked)

    print(f"✅ Phone numbers partially masked and saved to {a.output}")

if __name__ == '__main__':
    main()