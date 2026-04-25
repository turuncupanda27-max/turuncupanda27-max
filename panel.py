import json
import tkinter as tk
from tkinter import messagebox

DATA_FILE = 'data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"projects": []}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    messagebox.showinfo("Başarılı", "Veriler data.json dosyasına kaydedildi!")

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Proje Yönetim Paneli")
        self.root.geometry("500x400")
        self.data = load_data()

        # Liste Kutusu (Sol Taraf)
        self.listbox = tk.Listbox(root, width=30)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

        # Form Alanı (Sağ Taraf)
        self.form_frame = tk.Frame(root)
        self.form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.entries = {}
        fields = ["name", "type", "status", "desc", "tech"]
        for field in fields:
            tk.Label(self.form_frame, text=field.upper() + ":", anchor="w").pack(fill=tk.X)
            entry = tk.Entry(self.form_frame)
            entry.pack(fill=tk.X, pady=(0, 5))
            self.entries[field] = entry

        # Butonlar
        btn_frame = tk.Frame(self.form_frame)
        btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(btn_frame, text="Yeni Ekle", command=self.add_project).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Güncelle", command=self.update_project).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Sil", command=self.delete_project).pack(side=tk.LEFT, padx=2)
        tk.Button(self.form_frame, text="JSON'a Kaydet", bg="#4CAF50", fg="white", command=self.save_all).pack(fill=tk.X, pady=10)

        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for p in self.data["projects"]:
            self.listbox.insert(tk.END, p["name"])

    def on_select(self, event):
        if not self.listbox.curselection(): return
        index = self.listbox.curselection()[0]
        project = self.data["projects"][index]
        
        for field, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, project.get(field, ""))

    def add_project(self):
        new_project = {field: entry.get() for field, entry in self.entries.items()}
        if new_project["name"]:
            self.data["projects"].append(new_project)
            self.refresh_list()

    def update_project(self):
        if not self.listbox.curselection(): return
        index = self.listbox.curselection()[0]
        for field, entry in self.entries.items():
            self.data["projects"][index][field] = entry.get()
        self.refresh_list()

    def delete_project(self):
        if not self.listbox.curselection(): return
        index = self.listbox.curselection()[0]
        del self.data["projects"][index]
        self.refresh_list()
        for entry in self.entries.values(): entry.delete(0, tk.END)

    def save_all(self):
        save_data(self.data)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminPanel(root)
    root.mainloop()
