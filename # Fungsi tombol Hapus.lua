 # Fungsi tombol Hapus
def hapus():
    entry_nama.delete(0, tk.END)
    entry_tgl.delete(0, tk.END)
    entry_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# Membuat window
root = tk.Tk()
root.title("DATA SISWA BARU")
root.geometry("400x600")

# Judul
judul = tk.Label(root, text="DATA SISWA BARU", font=("Arial", 16, "bold"))
judul.pack(pady=10)

# Form Input
tk.Label(root, text="Nama Lengkap").pack()
entry_nama = tk.Entry(root, width=40)
entry_nama.pack()

tk.Label(root, text="Tanggal Lahir").pack()
entry_tgl = tk.Entry(root, width=40)
entry_tgl.pack()

tk.Label(root, text="Asal Sekolah").pack()
entry_sekolah = tk.Entry(root, width=40)
entry_sekolah.pack()

tk.Label(root, text="NISN").pack()
entry_nisn = tk.Entry(root, width=40)
entry_nisn.pack()

tk.Label(root, text="Nama Ayah").pack()
entry_ayah = tk.Entry(root, width=40)
entry_ayah.pack()

tk.Label(root, text="Nama Ibu").pack()
entry_ibu = tk.Entry(root, width=40)
entry_ibu.pack()

tk.Label(root, text="Nomor Telepon / HP").pack()
entry_hp = tk.Entry(root, width=40)
entry_hp.pack()

tk.Label(root, text="Alamat").pack()
text_alamat = tk.Text(root, width=30, height=4)
text_alamat.pack()

# Tombol
tk.Button(root, text="Simpan", bg="orange", command=simpan).pack(pady=5)
tk.Button(root, text="Hapus", bg="red", command=hapus).pack(pady=5)