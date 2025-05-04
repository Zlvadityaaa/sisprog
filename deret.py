#case1 angka terkecil kebesar
for x in range(100,1,4):
    print(x,end=" ")

#case2 angka terbsesar ke kecil
for x in range(30,0,-3):
    print(x,end=" ")

#case3 
result = 30
add = -1
for i in range(8):
    print(result, end=" ")
    result -=add
    add +=2

#case4
a, b= 1, 1
for _ in range(9):
    print(a, end=" ")
    a,b =b, a + b

