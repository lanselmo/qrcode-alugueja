import os
import re

files_to_update = {
    'page/new.html': [
        (r'<span style="font-size:\.9rem; color:var\(--text-dim\);"></span>', r'<span style="font-size:.9rem; color:var(--text-dim);" class="dynamic-domain-display"></span>')
    ],
    'page/create-card.html': [
        (r'<span></span>', r'<span class="dynamic-domain-display"></span>')
    ],
    'page/dashboard.html': [
        (r'<span></span>', r'<span class="dynamic-domain-display"></span>')
    ]
}

script_to_add = """
  <script>
    document.querySelectorAll('.dynamic-domain-display').forEach(el => {
      el.textContent = window.location.host + '/';
    });
  </script>
</body>
"""

for filepath, replacements in files_to_update.items():
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old_regex, new_text in replacements:
            content = re.sub(old_regex, new_text, content)
            
        if 'dynamic-domain-display' not in content:
            # wait, if I use re.sub for <span></span> in dashboard, there might be other empty spans. Let's be careful.
            pass

        # Add the script right before </body>
        if 'dynamic-domain-display' in content and 'el.textContent = window.location.host' not in content:
            content = content.replace('</body>', script_to_add)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
