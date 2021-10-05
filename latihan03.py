# import library
import time
import datetime

# input nama user
nama = input ("hallo ... nama saya Om Kompie , nama kamu siapa? ")

# tampilkan nama user
print("Oh.. nama kamu", nama, ", ya nama yang biasa sekali.")

# kasih jeda 3 detik
time.sleep(3)

# input tahun lahir
thnlahir = int(input("BTW... " + nama + " kamu lahir tahun berapa ya kalo om boleh tahu? "))

# kasih jeda 3 detik
time.sleep(3)

# hitung usia user 
skrg = datetime.datetime.now()
usia = skrg.year - thnlahir

# tampilkan usia
print("Owalah", nama,"kamu berarti berusia", usia,"tahun ya..")

# kasih jeda 3 detik
time.sleep(3)

# tampilkan pesan sesuai range usia
if (usia > 50):
    print("Anda sudah cukup tua ya?")
    print("Jaga kesehatan ya!!")
elif (usia > 20):
    print("Ternyata Anda masih cukup muda belia")
    print("Jangan sia-siakan masa mudamu ya!!")
elif (usia > 17):
    print("Hihihi... Anda ternyata masih ABG")
    print("Mulai berpikirlah secara dewasa ya!!")
elif (usia > 8) :
    print("ternyata kamu masih bocil ya")
    print("jangan kebanyakan main ff ya kasian orang tuamu beliin kuota tapi malah buat ngegame mulu")
elif (usia<2):
    print("wah kok udah bisa ngomong ya")

# kasih jeda 3 detik
time.sleep(3)

# say goodbye
print("OK.. see you later", nama, ".. senang berkenalan denganmu , semoga kita tidak berjumpa kembali")


