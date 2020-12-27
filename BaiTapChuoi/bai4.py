hoten=input("Nhap ho ten: ")
hoten_new=""
for i in hoten:
    if i.isalpha() or i ==" ":
        hoten_new+=i
print(hoten_new)
hoten_split=hoten_new.split()
print(" ".join(hoten_split).title())
hoten1=""
for i in hoten_split:
    hoten1+=i+" "
print(hoten1)
