from termcolor import colored
# Nama file untuk menyimpan jadwal
nama_file_jadwal = "jadwal.txt"

# Dictionary untuk menyimpan kegiatan harian
jadwal = {}

# Fungsi untuk menampilkan jadwal kegiatan
def tampilkan_jadwal():
    print("\n===== Jadwal Kegiatan =====")
    for hari, kegiatan in jadwal.items():
        print(f"{hari}:")
        for waktu, deskripsi in kegiatan:
            print(f"  - {waktu}: {deskripsi}")
    print("==========================\n")

# Fungsi untuk menambah kegiatan
def tambah_kegiatan():
    hari = input("Masukkan hari kegiatan (misal: Senin): ")
    waktu = input("Masukkan waktu kegiatan (misal: 08:00): ")
    deskripsi = input("Masukkan deskripsi kegiatan: ")
    if hari not in jadwal:
        jadwal[hari] = [ ]
    jadwal[hari].append((waktu, deskripsi))
    print(f"Kegiatan pada {hari} pukul {waktu} telah ditambahkan.")

# Fungsi untuk mengubah kegiatan
def ubah_kegiatan():
    hari = input("Masukkan hari kegiatan yang ingin diubah: ")
    if hari in jadwal:
        waktu = input("Masukkan waktu kegiatan yang ingin diubah: ")
        for i, (w, deskripsi) in enumerate(jadwal[hari]):
            if w == waktu:
                deskripsi_baru = input(f"Masukkan deskripsi baru untuk kegiatan pukul {waktu}: ")
                jadwal[hari][i] = (waktu, deskripsi_baru)
                print(f"Kegiatan pada {hari} pukul {waktu} telah diubah.")
                return
        print(f"Kegiatan pada {hari} pukul {waktu} tidak ditemukan.")
    else:
        print(f"Tidak ada kegiatan yang dijadwalkan pada {hari}.")

# Fungsi untuk menghapus kegiatan
def hapus_kegiatan():
    hari = input("Masukkan hari kegiatan yang ingin dihapus: ")
    if hari in jadwal:
        waktu = input("Masukkan waktu kegiatan yang ingin dihapus: ")
        for i, (w, deskripsi) in enumerate(jadwal[hari]):
            if w == waktu:
                del jadwal[hari][i]
                if not jadwal[hari]:  # Hapus hari jika kosong
                    del jadwal[hari]
                print(f"Kegiatan pada {hari} pukul {waktu} telah dihapus.")
                return
        print(f"Kegiatan pada {hari} pukul {waktu} tidak ditemukan.")
    else:
        print(f"Tidak ada kegiatan yang dijadwalkan pada {hari}.")

# Fungsi untuk menyimpan jadwal ke file teks
def simpan_ke_file():
    with open(nama_file_jadwal, 'w') as file:
        for hari, kegiatan in jadwal.items():
            file.write(f"{hari}\n")
            for waktu, deskripsi in kegiatan:
                file.write(f"{waktu},{deskripsi}\n")
    print("Jadwal kegiatan telah disimpan ke file.")

# Fungsi untuk memuat jadwal dari file teks
def muat_dari_file():
    jadwal.clear()
    try:
        with open(nama_file_jadwal, 'r') as file:
            lines = file.readlines()
            hari = None
            for line in lines:
                line = line.strip()
                if "," not in line:
                    hari = line
                    jadwal[hari] = []
                else:
                    waktu, deskripsi = line.split(',', 1)
                    jadwal[hari].append((waktu, deskripsi))
        print("Jadwal kegiatan telah dimuat dari file.")
    except FileNotFoundError:
        print("File tidak ditemukan. Belum ada jadwal yang tersimpan.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n===== Menu Manajemen Jadwal =====")
    print("1. Tambah Kegiatan")
    print("2. Ubah Kegiatan")
    print("3. Hapus Kegiatan")
    print("4. Tampilkan Jadwal")
    print("5. Simpan Jadwal ke File")
    print("6. Keluar")
    pilihan = input("Pilih opsi: ")
    return pilihan

# Memuat data jadwal dari file
muat_dari_file()

# Menampilkan menu
while True:
    pilihan = tampilkan_menu()
    if pilihan == "1":
        tambah_kegiatan()
    elif pilihan == "2":
        ubah_kegiatan()
    elif pilihan == "3":
        hapus_kegiatan()
    elif pilihan == "4":
        tampilkan_jadwal()
    elif pilihan == "5":
        simpan_ke_file()
    elif pilihan == "6":
        print(colored("Terima kasih telah menggunakan aplikasi manajemen jadwal!","red"))
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")
