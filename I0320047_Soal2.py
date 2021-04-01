#Program grading nilai

#input nama dan nilai siswa
print("Selamat datang di program grading nilai")
print("Masukkan data yang dibutuhkan")
nama = input("Nama : ")
nilai = int(input("Nilai yang akan dikonversi : "))

#output menggunakan percabangan
if nilai < 60 :
    print("Halo,", nama,"! Nilai anda setelah dikonversi adalah E.")
elif nilai <= 64 :
    print("Halo,", nama,"! Nilai anda setelah dikonversi adalah C.")
elif nilai <= 69 :
    print("Halo,", nama,"! Nilai anda setelah dikonversi adalah C+.")
elif nilai <= 74 :
    print("Halo,", nama,"! Nilai anda setelah dikonversi adalah B.")
elif nilai <= 79 :
    print("Halo,", nama,"! Nilai anda setelah dikonversi adalah B+.")
elif nilai <= 84 :
    print("Halo,", nama,"! Nilai anda setelah dikonversi adalah A.")
elif nilai <= 100 :
    print("Halo,", nama,"! Nilai anda setelah dikonversi adalah A+.")
else :
    pass
