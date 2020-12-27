#chuoi=input("Nhap vao mot chuoi: ")
#a=input("Nhap vao ky tu: ")
#print(chuoi.count(a))
#print(chuoi.find(a))
#for i in range(len(chuoi)):
#    print(str(chuoi[i])+":"+str(chuoi.count(chuoi[i])))
#tu=input("Nhap vao mot tu: ")
#print(chuoi.find(tu))

xaukitu=input("Nhap vao 1 xau bat ki: ")
kitu = input("Nhap vao 1 ky tu: ")
print("So lan xuat hien: ",xaukitu.count(kitu))
print("Vi tri ki tu: ",xaukitu.find(kitu))
dictionary={}
for i in xaukitu:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1
print(dictionary)
for i in dictionary:
    print(i,dictionary[i])
tucantim=input("Nhap tu can tim trong xau: ")
vitri=xaukitu.find(tucantim)
if vitri>0:
    print("Vi tri can tim la: ",vitri)
else:
    print("Khong tim thay")