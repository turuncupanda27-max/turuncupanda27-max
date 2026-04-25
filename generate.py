import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

readme = f"""
# 👋 Profilim

📊 Bugün öğrenilen kelime: {data["gunluk"]}  
🌍 Aktif dil: {data["dil"]}  
📚 Toplam kelime: {data["kelime"]}  

---
🚀 Bu profil otomatik güncelleniyor.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
