import json
from datetime import datetime

# Veriyi yükle
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Retro ASCII Başlık
readme = "```text\n"
readme += "╔════════════════════════════════════════════════════════╗\n"
readme += f"║ USER: {data['header']['title']:<48} ║\n"
readme += f"║ STAT: {data['header']['status']:<48} ║\n"
readme += f"║ MODE: {data['header']['focus']:<48} ║\n"
readme += "╚════════════════════════════════════════════════════════╝\n\n"

readme += f"LAST_LOGIN: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

readme += "> ./list_projects.sh\n"
readme += "----------------------------------------------------------\n"

# Projeleri terminal listesi gibi yazdır
for p in data['projects']:
    readme += f"[{p['name'].upper()}] - {p['type']}\n"
    readme += f"  > Status : {p['status']}\n"
    readme += f"  > Desc   : {p['desc']}\n"
    readme += f"  > Stack  : {p['tech']}\n"
    readme += "----------------------------------------------------------\n"

readme += "```\n"

# README.md dosyasını oluştur
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
