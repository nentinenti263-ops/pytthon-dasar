import tkinter as tk
from tkinter import ttk, messagebox

class AplikasiParkir:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Parkir Kelompok 6")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f5f5")

        # --- Variabel Data ---
        self.biaya_per_jam = 2000
        self.data_parkir = []

        # --- Header ---
        tk.Label(root, text="Aplikasi Parkir Kelompok 6", font=("Arial", 16, "bold"), bg="#f0f5f5").place(x=20, y=10)

        # --- Input Section ---
        tk.Label(root, text="Cari NoPol", bg="#f0f5f5").place(x=20, y=50)
        self.ent_cari = tk.Entry(root)
        self.ent_cari.place(x=120, y=50, width=150)
        tk.Button(root, text="Cari", command=self.cari_data).place(x=280, y=47)

        tk.Label(root, text="No Plat Polisi", bg="#f0f5f5").place(x=20, y=90)
        self.ent_nopol = tk.Entry(root)
        self.ent_nopol.place(x=120, y=90, width=150)

        tk.Label(root, text="Waktu Masuk", bg="#f0f5f5").place(x=20, y=120)
        self.ent_masuk = tk.Entry(root)
        self.ent_masuk.place(x=120, y=120, width=150)

        tk.Label(root, text="Waktu Keluar", bg="#f0f5f5").place(x=20, y=150)
        self.ent_keluar = tk.Entry(root)
        self.ent_keluar.place(x=120, y=150, width=150)

        tk.Label(root, text="Biaya", bg="#f0f5f5").place(x=20, y=180)
        self.ent_biaya = tk.Entry(root)
        self.ent_biaya.insert(0, "0")
        self.ent_biaya.place(x=120, y=180, width=100)
        tk.Button(root, text="Hitung & Simpan", bg="#ddd", command=self.hitung_dan_simpan).place(x=230, y=177)

        # --- Label Biaya Besar ---
        tk.Label(root, text="Biaya Per Jam", font=("Arial", 14), fg="red", bg="#f0f5f5").place(x=450, y=60)
        tk.Label(root, text=f"Rp. {self.biaya_per_jam:,}", font=("Arial", 24, "bold"), fg="red", bg="#f0f5f5").place(x=450, y=90)

        # --- Tabel Section ---
        # Tabel 1: List Pelanggan Terakhir Keluar
        tk.Label(root, text="List Pelanggan Urut Terakhir Keluar", fg="blue", bg="#f0f5f5").place(x=20, y=230)
        self.tree_terakhir = self.buat_tabel(root, x=20, y=250)

        # Tabel 2: List Pelanggan Banyak Bayar
        tk.Label(root, text="List Pelanggan Banyak Bayar", fg="blue", bg="#f0f5f5").place(x=410, y=230)
        self.tree_banyak = self.buat_tabel(root, x=410, y=250)

    def buat_tabel(self, parent, x, y):
        cols = ("No Plat Polisi", "Masuk", "Keluar", "Biaya")
        tree = ttk.Treeview(parent, columns=cols, show="headings", height=8)
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=90)
        tree.place(x=x, y=y)
        return tree

    def hitung_dan_simpan(self):
        try:
            nopol = self.ent_nopol.get()
            masuk = int(self.ent_masuk.get())
            keluar = int(self.ent_keluar.get())
            
            durasi = keluar - masuk
            if durasi < 0: raise ValueError
            
            total_biaya = durasi * self.biaya_per_jam
            self.ent_biaya.delete(0, tk.END)
            self.ent_biaya.insert(0, str(total_biaya))

            # Simpan Data
            data = (nopol, masuk, keluar, total_biaya)
            self.data_parkir.append(data)
            self.update_tabel()
            
        except ValueError:
            messagebox.showerror("Error", "Masukkan jam (angka) dengan benar!")

    def update_tabel(self):
        # Bersihkan tabel
        for i in self.tree_terakhir.get_children(): self.tree_terakhir.delete(i)
        for i in self.tree_banyak.get_children(): self.tree_banyak.delete(i)

        # Update Tabel Terakhir (Urutan Input)
        for item in reversed(self.data_parkir):
            self.tree_terakhir.insert("", tk.END, values=item)

        # Update Tabel Banyak Bayar (Sorting Biaya Tinggi ke Rendah)
        data_sorted = sorted(self.data_parkir, key=lambda x: x[3], reverse=True)
        for item in data_sorted:
            self.tree_banyak.insert("", tk.END, values=item)

    def cari_data(self):
        target = self.ent_cari.get()
        for item in self.data_parkir:
            if item[0] == target:
                self.ent_nopol.delete(0, tk.END)
                self.ent_nopol.insert(0, item[0])
                self.ent_masuk.delete(0, tk.END)
                self.ent_masuk.insert(0, item[1])
                return
        messagebox.showinfo("Cari", "Data tidak ditemukan")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiParkir(root)
    root.mainloop()