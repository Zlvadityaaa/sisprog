nama = input("masukan nama anda: ")
total = len(nama)
nama = nama.upper()
#print = (nama[0:1])
#print = (nama[0:2])
#print = (nama[0:3])
for i in range(total):
    print (nama[:total - i] + "*" * i)

    
