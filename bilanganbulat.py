a = int(input("masukan bilangan a: "))
b = int(input("masukan bilangan b: "))
c = int(input("masukan bilangan c: "))

if (a > b or b > c ) and (a % 2 == 0 and c % 2 == 1) and (b != c):
   print("Kondisi terpenuhi")
else:
   print("Kondisi tidak terpenuhi")