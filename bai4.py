print("Moi ban nhap vao 1 so nguyen duong: ")
while True:
    a = int(input())
    if a<0:
        print("Nhap sai, moi ban nhap lai:")
    else:
        break

total = 0
thuong = a
while True:
    du = thuong%10
    thuong = int(thuong/10)
    total += du
    if thuong==0:
        break
print("Tong cac chu so cua so", a, "la:", total)