def konversisuhu(suhu, dari="C", ke="R"):
    if dari == "C" and ke == "R":
        return  4 / 5*suhu  
    print(konversisuhu(100),"C","K")

# sample 2
def konversisuhu(suhu, dari="C", ke="R"):
    if dari == "C" and ke == "R":
        return  4 / 5*suhu  
    elif dari == "R" and ke == "C":
        return 5 / 4*suhu
    elif dari == "C" and ke == "F":
        return (9 / 5 * suhu) + 32
    elif dari == "F" and ke == "C":
        return (suhu - 32) * 5 / 9
    elif dari == "R" and ke == "F":
        return (9 / 4 * suhu) + 32
    elif dari == "F" and ke == "R":
        return (suhu - 32) * 4 / 9