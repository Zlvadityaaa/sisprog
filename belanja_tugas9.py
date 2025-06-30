daftar_belanja = []
for i in range(5):
    item = input(f"Masukan item belanja{i+1}:")
    daftar_belanja.append(item)

hapus = input("Masukan item yang sudah anda beli:")

if hapus in daftar_belanja:
    daftar_belanja.remove(hapus)
    print("daftar belanja setelah di hapus :")
else : 
    print("item tidak ada dalam daftar belanja")

print("list daftar belanja:", daftar_belanja)