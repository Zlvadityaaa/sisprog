def Hitung_nilai_mapel(Matematika, Saint, Inggrish):
    rata_rata = (Matematika + Saint + Inggrish) / 3
    di_bawah_70 = sum(1 for nilai in [Matematika, Saint, Inggrish] if nilai < 70)
      
    if rata_rata > 75 and di_bawah_70  <= 1:
       return "Lulus"
    else : 
       return "Tidak lulus"

Matematika = float(input("Masukan nilai Matematika: "))
Saint = float(input("Masukan nilai Saint: "))
Inggrish = float(input("Masukan nilai Inggrish: "))

hasil = Hitung_nilai_mapel(Matematika, Saint, Inggrish)
print(f"Hasil: {hasil}")
