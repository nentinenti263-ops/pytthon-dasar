import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        # Mengambil input dari entry dan mengubahnya ke angka
        harga = float(entry_harga.get())
        kuantitas = float(entry_kuantitas.get())
        
        # Melakukan kalkulasi
        total = harga * kuantitas
        
        # Menampilkan hasil dengan format mata uang
        label_hasil.config(text=f"Total: Rp.{total:,.2f}")
    except ValueError:
        # Pesan error jika input bukan angka
        messagebox.showerror("Error", "Masukkan angka yang valid untuk Harga dan Kuantitas!")

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x250")

# Label dan Entry untuk Harga
tk.Label(root, text="Harga:", font=("Arial", 10)).pack(pady=(10, 0))
entry_harga = tk.Entry(root)
entry_harga.pack(pady=5)

# Label dan Entry untuk Kuantitas
tk.Label(root, text="Kuantitas:", font=("Arial", 10)).pack(pady=(10, 0))
entry_kuantitas = tk.Entry(root)
entry_kuantitas.pack(pady=5)

# Tombol Hitung Total
btn_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
btn_hitung.pack(pady=20)

# Label untuk menampilkan Total
label_hasil = tk.Label(root, text="Total: Rp.0.00", font=("Arial", 10, "bold"))
label_hasil.pack()

# Menjalankan aplikasi
root.mainloop()