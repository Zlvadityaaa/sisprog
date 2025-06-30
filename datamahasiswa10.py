data_mahasiswa = {}
def tambah_data ():
    NIM = input("Masukkan NIM: ")
    NAMA = input("Masukkan Nama: ")
    ALAMAT = input("Masukkan Alamat: ")
    JURUSAN = input("Masukkan Jurusan: ")
    IPK = input("Masukan IPK :")

    data_mahasiswa[NIM] = {"nama": NAMA, "alamat": ALAMAT, "jurusan": JURUSAN, "ipk": IPK}
    print("Data mahasiwa berhasil ditambhkan")

def tampilkan_data():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa .")
    else:
        for NIM, info in data_mahasiswa.items():
            mahasiswa_info = (NIM, info['nama'], info['jurusan'], info['ipk'])
            print(f"NIM: {mahasiswa_info[0] }, nama: {mahasiswa_info[1]},  jurusan: {mahasiswa_info[2]}, ipk: {mahasiswa_info[3]}")

def cari_data():
    NIM =input("masukan NIM yang dicari: ")
    if NIM in data_mahasiswa:
        info = data_mahasiswa[NIM]
        print(f"NIM: {NIM}, Nama: {info['nama']}, Jurusan: {info['jurusan']}, IPK: {info['ipk']}")

    else:
        print("Data mahasiswa tidak ditemukan.")
def hapus_data():
    NIM = input("Maukan NIM yang mau dihapus: ")
    if NIM in data_mahasiswa:
        del data_mahasiswa[NIM]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Data mahasiswa tidak ditemukan.")

def main():
    while True:
        print("Menu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Cari Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            cari_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
