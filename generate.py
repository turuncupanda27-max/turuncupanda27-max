import json
from datetime import datetime

# Veriyi yükle
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Modern ve Minimalist Başlık
readme = "<div align='center'>\n\n"
readme += f"# {data['header']['title']}\n"
readme += f"**{data['header']['focus']}**\n\n"
readme += "</div>\n\n"

readme += "---\n\n"
readme += "### ⚡ Projeler & Altyapılar\n\n"

# Projeleri modern bir blok alıntı (blockquote) tasarımıyla yazdır
for p in data['projects']:
    # Eski ASCII çubuklarını (örn: [████░░░░] ) temizle
    status_text = p['status'].split('] ')[-1] if '] ' in p['status'] else p['status']
    
    readme += f"#### **{p['name']}**\n"
    readme += f"> {p['desc']}\n>\n"
    readme += f"> **Kategori:** `{p['type']}` | **Durum:** `{status_text}` | **Stack:** `{p['tech']}`\n\n"

readme += "---\n"
readme += f"<p align='right'><sub>Son Güncelleme: {datetime.now().strftime('%Y-%m-%d')}</sub></p>\n"

# README.md dosyasını oluştur
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
