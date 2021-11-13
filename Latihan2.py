print ("------------------")
print ("Pertemuan ke 7")
print ("latihan 2")
print ("------------------")

gaji = int(input("masukkan gaji :"))
berkeluarga = (False, True)[input("sudah berkeluarga? (Y/T) :") == "Y"]
punya_rumah = (False, True)[input("punya rumah? (Y/T) :") == "Y"]

if gaji > 3000000:


    print ("                        ")
    print ("-------Keterangan-------")
    print ("                        ")

    print ("gaji sudah diatas UMR")
    if berkeluarga :
        print ("- wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print ("- tidak perlu ikut asuransi")    
    if punya_rumah :
        print ("- wajib bayar pajak rumah")
    else:
        print ("- tidak wajib bayar pajak rumah")
else:
    print ("gaji belum UMR")
    