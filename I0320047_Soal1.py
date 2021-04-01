#Program untuk menyapa pengunjung hotel

#input nama dan jenis kelamin pengunjung
print("Masukkan data di bawah ini")
nama = input("Nama lengkap : ")
gender = input("Jenis kelamin (L/P) : ")

#output menggunakan percabangan
if gender == "L" :
    print("Selamat datang, Mr.",nama,"!")
else :
    print("Selamat datang, Ms.",nama,"!")
