
def cek_kelulusan (pembayaran_lunas, nilai_rata_rata):
    if pembayaran_lunas and nilai_rata_rata >= 2.0: 
        return "lulus"
    else :
        return "tidak lulus"
    
pembayaran_lunas=input("Apakah sudah membayar uang semester?: ya/tidak").strip() == "ya"
nilai_rata_rata=float(input("masukan nilai rata rata anda:(D=1.0, C=2.0, B=3.0, A=4.0 ): "))

hasil = cek_kelulusan(pembayaran_lunas, nilai_rata_rata)
print(f"status: {hasil}")