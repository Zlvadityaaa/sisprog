def penentuan_usia(umur):
    if 0 <= umur< 2:
        return"OROK"
    elif 2 <= umur< 5:
        return"Balita"
    elif 5 <= umur< 12:
        return"Budak budak"
    elif 12 <= umur< 18:
        return"Remaja"
    else:
        return"Dewasa"

umur = float(input("masukan usia anda: "))
print(f"penentuan_usia: {penentuan_usia(umur)}")