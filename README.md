# latihan1
<p>
- sourcecode Latihan 1
<p>
<p> print ("------------------")
<p> print ("Pertemuan ke 7")
<p> print ("latihan 1")
<p> print ("------------------")

<p> nama    = input ("Masukkan nama:")
<p> uts     = input ("Masukkan nilai UTS :")
<p> uas     = input ("Masukkan nilai UAS :")
<p> tugas   = input ("Masukkan nilai Tugas:")
<p> akhir   = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)
<p> keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]

<p> if akhir > 80:
<p>    huruf = "A"
<p> elif akhir > 70:
<p>    huruf = "B"
<p> elif akhir > 50:
<p>   huruf = "c"
<p> elif akhir > 40:
<p>    huruf = "D"
<p>else:
<p>    huruf = "E"

<p> print ("Nama        :",nama)
<p> print ("Nilai UTS   :",uts)
<p> print ("Nilai UAS   :",uas)
<p> print ("Nilai Tugas :",tugas)
<p> print ("Nilai Akhir :",akhir)

<p> print ("-------------------------")
<p> print ("Nilai Huruf :",huruf)
<p> print ("Keterangan  :",keterangan)

<p> print("--------------------------")
<p>
<p> ![screenshotlatihan1](https://user-images.githubusercontent.com/92582081/141603893-079b0c26-840b-4b69-abe8-258127b1e118.png)
  
  
# latihan2
<p>
- sourcecode Latihan 2
<p> print ("------------------")
<p> print ("Pertemuan ke 7")
<p> print ("latihan 2")
<p> print ("------------------")

<p> gaji = int(input("masukkan gaji :"))
<p> berkeluarga = (False, True)[input("sudah berkeluarga? (Y/T) :") == "Y"]
<p> punya_rumah = (False, True)[input("punya rumah? (Y/T) :") == "Y"]

<p> if gaji > 3000000:


<p>    print ("                        ")
<p>    print ("-------Keterangan-------")
<p>    print ("                        ")

<p>    print ("gaji sudah diatas UMR")
<p>    if berkeluarga :
<p>        print ("- wajib ikutan asuransi dan menabung untuk pensiun")
<p>    else:
<p>        print ("- tidak perlu ikut asuransi")    
<p>    if punya_rumah :
<p>        print ("- wajib bayar pajak rumah")
<p>    else:
<p>        print ("- tidak wajib bayar pajak rumah")
<p> else:
<p>    print ("gaji belum UMR")
 <p>
 <p> ![screenshotlatihan2](https://user-images.githubusercontent.com/92582081/141603978-471425a7-de42-4d7c-99af-65bbb5213d2d.png)
 
  
# latihan3
<p>
- sourcecde Latihan 3
<p> print ("------------------")
<p> print ("Pertemuan ke 7")
<p> print ("latihan 3")
<p> print ("penggunaan kondisi or, program membandingkan 3 input bilangan")
<p> print ("------------------")

<p> a = int (input("masukkan bilangan A :"))
<p> b = int (input("masukkan bilangan B :"))
<p> c = int (input("masukkan bilangan C :"))

<p> print ("------------------")
<p> if a+b == c or b+c == a or c+a == b :
<p>    print("BENAR")
<p> else :
<p>    print("SALAH")
<p>
<P> ![screenshotlatihan2](https://user-images.githubusercontent.com/92582081/141603978-471425a7-de42-4d7c-99af-65bbb5213d2d.png)
<p>
# Tugaspraktikum2
<p>
- Sourcecode tugaspraktikum3
