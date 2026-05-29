import os
import re

files_to_update = {
    'assets/js/pages/edit.js': [(r"const PRIMARY_DOMAIN = 'https://qrcode-alugueja\.netlify\.app';", "const PRIMARY_DOMAIN = window.location.origin;")],
    'assets/js/pages/new.js': [(r"const PRIMARY_DOMAIN = 'https://qrcode-alugueja\.netlify\.app';", "const PRIMARY_DOMAIN = window.location.origin;")],
    'assets/js/pages/dashboard.js': [(r"const PRIMARY_DOMAIN = 'https://qrcode-alugueja\.netlify\.app';", "const PRIMARY_DOMAIN = window.location.origin;")],
    'page/new.html': [(r"https://qrcode-alugueja\.netlify\.app/", "")],
    'page/create-card.html': [(r"qrcode-alugueja\.netlify\.app/", "")],
    'page/dashboard.html': [(r"qrcode-alugueja\.netlify\.app/", "")]
}

for filepath, replacements in files_to_update.items():
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        for old_regex, new_text in replacements:
            content = re.sub(old_regex, new_text, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
