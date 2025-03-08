#Case 1
tahun = 2025
jenis = "ganjil"
if tahun % 4 == 0:
    jenis = "genap"
print("%s adalah tahun %s" % (tahun, jenis))

#Case 2
angka = int(input("Masukan sebuah angka:"))

if angka > 0:
    print("positif")
elif angka < 0:
    print("negatif")
else:
    print("nol")

#Case 3
nilai = int(input("masukan Total:"))
grade = "E"

if nilai >=100:
    grade="A"

elif nilai >=80:
    grade="B"
elif nilai >70:
    grade="C"
elif nilai >60:
    grade="D"
print("Garde:", grade)
