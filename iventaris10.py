inventaris = {}

def tambah_barang():
    nama_barang = input("masukan nama brang:")
    harga_barang = float(input("masukan harga brang:"))
    stok_brang = int(input("masukan stok barang"))

    inventaris[nama_barang] = {"harga": harga_barang, "stok": stok_brang}
    print("barang berhasil di tambhkan")

def tampilkan_barang():
    if not inventaris:
        print("tidak ada barang di dalam inventaris")
    else:
        print("/nDaftar Barang:")
        print(f"{'Nama Barang':<20} {'Harga':<10} {'Stok':<10}")
        print("-" * 40)
        for nama_barang, info in inventaris.items():
            print(f"{nama_barang:<20} {info['harga']:<10} {info['stok']:<10}")
    
    def cari_barang():
        nama_barang = input("masukan nama barang yang dicari: ")
        if nama_barang in inventaris:
            info = inventaris[nama_barang]
            print(f"Nama Barang: {nama_barang}, Harga: {info['harga']}, Stok: {info['stok']}")
        else:
            print("barang tidak di temukan")
        
    def analisi_data():
        if not inventaris:
            print("tidak ada barang di dalam inventaris")
        return
harga_barang = [(nama_barang, info[0]) for nama_barang, info in inventaris.items()]
harga_tertinggi = max(harga_barang, key=lambda x: x[1])
harga_terendah = min(harga_barang, key=lambda x: x[1])

total_stok = sum(harga_barang * stok for harga_barang, stok in inventaris.values())
print(f"barang dengan harga tertinggi: {harga_tertinggi[0]} dengan harga {harga_tertinggi[1]}")
print(f"barang dengan harga terendah: {harga_terendah[0]} dengan harga {harga_terendah[1]}")
print(f"total stok barang: {total_stok}")

def main():
    while True:
        print("Menu:")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Cari Barang")
        print("4. Analisis Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            tampilkan_barang()
        elif pilihan == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")