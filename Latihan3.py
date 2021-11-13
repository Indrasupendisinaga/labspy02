print ("------------------")
print ("Pertemuan ke 7")
print ("latihan 3")
print ("penggunaan kondisi or, program membandingkan 3 input bilangan")
print ("------------------")



a = int (input("masukkan bilangan A :"))
b = int (input("masukkan bilangan B :"))
c = int (input("masukkan bilangan C :"))

print ("------------------")
if a+b == c or b+c == a or c+a == b :
    print("BENAR")
else :
    print("SALAH")