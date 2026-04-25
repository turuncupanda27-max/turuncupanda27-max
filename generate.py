import json

# Veriyi yükle
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Sadece projelere odaklanan minimalist yapı
readme = "### ⚡ Projeler\n\n"

for p in data['projects']:
    readme += f"#### **{p['name']}**\n"
    readme += f"> {p['desc']}\n>\n"
    readme += f"> **Kategori:** `{p['type']}` | **Durum:** `{p['status']}` | **Stack:** `{p['tech']}`\n\n"

readme += "---\n"

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
