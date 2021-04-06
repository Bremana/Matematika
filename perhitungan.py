import os
import time

os.system ("pkg install git -y &> /dev//null")
os.system ("clear")
time.sleep (1)

def banner():
   os.system ("figlet Perhitungan")
   print ("Author : Mr.Slyker")
   print ("Website : https://SarungCyberTeam.blogspot.com")
   print ("Github : https://github.com/MrSlyker")

banner()
print ("-----------------------------------")
print ("Silahkan Pilih Sesuai Rumus Dibawah")
print ("-----------------------------------")
print ("1. Pertambahan")
print ("2. Perkalian")
print ("3. Pengurangan")
print ("4. Pembagian")
print ("0. Exit")
print ("")

pilih = input ("Masukkan Pilihan :")
if(pilih == 1):
  os.system ("clear")
  time.sleep (1)
  banner()
  print ("---------------------------------")
  print ("Masukkan Angka Yang Mau Di Tambah")
  print ("---------------------------------")
  angka1 = input ("Masukkan Angka :")
  angka2 = input ("Tambah Berapa :")

  tambah = (angka1 + angka2)
  print ("Sedang Menghitung...")
  time.sleep (3)
  print "Hasil :", tambah
  os.system ("exit")

elif(pilih == 2):
  os.system ("clear")
  time.sleep (1)
  banner()
  print ("------------------------------")
  print ("Masukkan Angka Yang Mau Dikali")
  print ("------------------------------")
  angka3 = input ("Masukkan Angka :")
  angka4 = input ("Kali Berapa :")

  kali = (angka3 * angka4)
  print ("Sedang Menghitung...")
  time.sleep (3)
  print "Hasil :", kali
  os.system ("exit")

elif(pilih == 3):
  os.system ("clear")
  time.sleep (1)
  banner()
  print ("--------------------------------")
  print ("Masukkan Angka Yang Mau Dikurang")
  print ("--------------------------------")
  angka5 = input ("Masukkan Angka :")
  angka6 = input ("Kurang Berapa :")

  kurang = (angka5 - angka6)
  print ("Sedang Menghitung...")
  time.sleep (3)
  print "Hasil :", kurang
  os.system ("exit")

elif(pilih == 4):
  os.system ("clear")
  time.sleep (1)
  banner()
  print ("------------------------------")
  print ("Masukkan Angka Yang Mau Dibagi")
  print ("------------------------------")
  angka7 = input ("Masukkan Angka :")
  angka8 = input ("Bagi Berapa :")

  bagi = (angka7 % angka8)
  print ("Sedang Menghitung...")
  time.sleep (3)
  print "Hasil :", bagi
  os.system ("exit")
elif(pilih == 0):
  print ("Terima Kasih Sudah Menggunakan Tools Ini")
  time.sleep (1)
  os.system ("exit")

else:
  print ("Silahkan Masukkan Input Yang Benar")
  time.sleep (1)
  os.system ("exit")
