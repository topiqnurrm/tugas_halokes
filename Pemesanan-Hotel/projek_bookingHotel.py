import datetime
import time
import sys


def buat_pesanan(pesanan):
    # Simpan pesanan user ke file masing-masing
  nama_file = "data_" + username + ".txt"

  # Format data yang disimpan:
  # tanggal_pesan,nama_hotel,jenis_kamar,total_harga

  data_pesanan = f"{datetime.date.today()},{pesanan.hotel.nama},{pesanan.kamar.jenis},{pesanan.total_harga}\n"

  file_pesanan = open(nama_file, "a+")
  file_pesanan.write(data_pesanan)
  file_pesanan.close()

  print("Data pesanan berhasil disimpan!")

def registrasi():
  while True:
    username = input(
        "--------------------\nMasukkan username: ")
    if username == "1" :
      main_menu()
    elif len(username) < 5:
      print("--------------------\nKetik '1' untuk kembali\nUsername minimal 5 karakter")
      continue
    else:
      print("--------------------\nUsername sukses\n--------------------")
      break

  while True:
    password = input("Masukkan password: ")
    if username == "1" :
          main_menu()
    elif len(password) < 8:
      print("--------------------\nKetik '1' untuk cancel registrasi\nPassword minimal 8 karakter\n--------------------")
      continue
    else:
      print("--------------------\nPassword sukses\n--------------------")
      break

  with open("data_login.txt", "a") as file:
    file.write(f"{username},{password}\n")

  print("__________Registrasi berhasil!__________")
  main_menu()

def main_menu():
  print("\n--------------------")
  print("MAIN MENU")
  print("1. Registrasi")
  print("2. Login")
  print("3. Lihat List Username")
  print('4. Exit Program')
  print("--------------------\n\n--------------------")

  menu = input("Pilih menu: ")

  if menu == "4":
    sys.exit()
  if menu == "1":
    registrasi()
  elif menu == "2":
    login()
  elif menu == "3":
    lihat_user()
  else:
    print("--------------------\nMENU TIDAK TERSEDIA\nHarap pilih angka antara 1 sampai dengan 4\n--------------------")
    main_menu()

def login():

  with open("data_login.txt") as file:
    data = file.readlines()

  while True:
    global username
    username = input("--------------------\nMasukkan username: ")

    # Cek apakah username ditemukan
    status_user = False
    for line in data:
      temp_username, temp_password = line.strip().split(",")
      if username == temp_username:
        status_user = True
        break

    if status_user:
      print("--------------------\nUsername ditemukan")

      # Buka file data pesanan spesifik user
      nama_file = "data_" + username + ".txt"
      file_pesanan = open(nama_file, "a+")

      while True:
        password = input("--------------------\nMasukkan password: ")

        # Cek password
        status_pass = False
        for line in data:
          temp_username, temp_password = line.strip().split(",")
          if username == temp_username and password == temp_password:
            print("--------------------\npassword benar\n--------------------\n__________Login berhasil__________\n")
            status_pass = True
            home()

        if status_pass:

          break

        else:
          ulang = input("--------------------\nPassword salah. \nMasukkan '0' untuk coba lagi\nMasukkan '1' untuk kembali\n--------------------\nPilihan : ")
          if ulang == "0":
            continue
          elif ulang == '1':
              main_menu()
          else:
            main_menu()

    else:
      ulang = input(
          "--------------------\nUsername tidak ditemukan. \nMasukkan '0' untuk coba lagi\nMasukkan '1' untuk kembali\n--------------------\nPilihan : ")
      if ulang == "0":
        continue
      else:
        main_menu()

def lihat_user():
    with open("data_login.txt") as file:
        data = file.readlines()

    users = []
    for line in data:
        username = line.split(",")[0]
        users.append(username)

    users = sorted(users, key=lambda x: x.lower())

    print("--------------------\nLIST USERNAME:")
    for user in users:
        print(f"- {user}")
    print("__________Pengguna__________")

    main_menu()

def home():
    # Import modul yang diperlukan

    # Definisikan kelas Hotel

  class Hotel:
      # Konstruktor
      def __init__(self, nama, alamat):
          self.nama = nama
          self.alamat = alamat

      # Metode untuk menampilkan informasi hotel
      def tampilkan_info(self):
          print("Nama Hotel:", self.nama)
          print("Alamat:", self.alamat)
          print()

      # Metode untuk mencocokkan nama hotel
      def cocokkan_nama(self, kata_kunci):
          return kata_kunci.lower() in self.nama.lower()

  # Definisikan kelas Kamar

  class Kamar:
      # Konstruktor
      def __init__(self, jenis, orang, harga):
          self.jenis = jenis
          self.orang = orang
          self.harga = harga

      # Metode untuk menampilkan informasi kamar
      def tampilkan_info(self):
          print("Jenis Kamar:", self.jenis)
          print("Muat untuk:", self.orang)
          print("Harga Kamar:", self.harga)
          print()

      # Metode untuk mendapatkan harga hotel
      def get_harga(self):
          return self.harga

  # Definisikan kelas Pesanan

  class Pesanan:
      # Konstruktor
      def __init__(self, hotel, kamar, tanggal_checkin, tanggal_checkout):
          self.hotel = hotel
          self.kamar = kamar
          self.tanggal_checkin = tanggal_checkin
          self.tanggal_checkout = tanggal_checkout
          self.total_harga = self.hitung_total_harga()

      # Metode untuk menampilkan informasi pesanan
      def tampilkan_info(self):
          print("Pesanan Anda:")
          print("Hotel:", self.hotel.nama)
          print("Kamar:", self.kamar.jenis)
          print("Tanggal Check-in:", self.tanggal_checkin)
          print("Tanggal Check-out:", self.tanggal_checkout)
          print("Total Harga:", self.total_harga)

      # Metode untuk mendapatkan tanggal check-out
      def get_tanggal_checkout(self):
          return self.tanggal_checkout

      # Metode untuk menghitung total harga
      def hitung_total_harga(self):
          # Harga per malam (asumsi setiap malam memiliki harga yang sama)
          harga_per_malam = self.kamar.harga
          # Selisih hari antara check-in dan check-out
          selisih_hari = (self.tanggal_checkout - self.tanggal_checkin).days
          # Total harga
          total_harga = harga_per_malam * selisih_hari
          return total_harga

  # Definisikan fungsi untuk mendapatkan input dari pengguna

  def get_input(prompt):
      return input(prompt)

  # Definisikan fungsi untuk validasi input

  def validasi_input(input):
      if input == "":
          return False
      else:
          return True

  # Fungsi untuk melakukan pertukaran elemen pada daftar hotel

  def exchange_sort_hotel(arr):
      n = len(arr)
      for i in range(n - 1):
          for j in range(0, n - i - 1):
              if arr[j].nama.lower() > arr[j + 1].nama.lower():
                  arr[j], arr[j + 1] = arr[j + 1], arr[j]

  def exchange_sort_kamar(arr):
      n = len(arr)
      for i in range(n - 1):
          for j in range(0, n - i - 1):
              if arr[j].harga > arr[j + 1].harga:
                  arr[j], arr[j + 1] = arr[j + 1], arr[j]

  # Definisikan fungsi untuk menampilkan menu

  def tampilkan_menu():
      print("--------------------")
      print("Menu Pemesanan Hotel")
      print("1. Daftar Hotel")
      print("2. Cari Hotel")
      print("3. Buat Pesanan")
      print("4. Tampilkan Pesanan")
      print("5. Logout")
      print("--------------------\n")

  # Fungsi utama

  def main():
      # Buat daftar hotel
      hotel1 = Hotel("Hotel C", "Jl. Magelang No. 200, Yogyakarta")
      hotel2 = Hotel("Hotel A", "Jl. Jogja-Solo No. 100, Yogyakarta")
      hotel3 = Hotel("Hotel B", "Jl. Malioboro No. 1, Yogyakarta")

      # Buat daftar kamar
      kamar2 = Kamar("Kamar Deluxe", "4 orang", 500000)
      kamar1 = Kamar("Kamar Standard", "2 orang", 300000)
      kamar3 = Kamar("Kamar Suite", "6 orang", 700000)

      # Inisialisasi daftar pesanan
      daftar_pesanan = []


      # Pilihan menu
      pilihan = 0
      while pilihan != 5:
          tampilkan_menu()
          pilihan = int(get_input("--------------------\nPilih menu: "))

          # Validasi input
          if not validasi_input(pilihan):
              print("--------------------\nInput tidak valid!")
              continue

          # Pilih menu
          elif pilihan == 1:
              print("--------------------")
              print("1. Urutkan Sesuai Abjad:")
              print("2. List Harga Kamar Hotel:")
              menu = int(get_input("--------------------\nPilih menu: "))
              if menu == 1:
                  # Urutkan daftar hotel
                  daftar_hotel = [hotel1, hotel2, hotel3]
                  exchange_sort_hotel(daftar_hotel)
                  print("--------------------\nDaftar Hotel sesuai dengan abjad:")
                  for hotel in daftar_hotel:
                      hotel.tampilkan_info()
                  print("__________Sesuai Abjad__________\n")
              elif menu == 2:
                  # Urutkan daftar harga hotel
                  daftar_kamar = [kamar1, kamar2, kamar3]
                  exchange_sort_kamar(daftar_kamar)
                  print("--------------------\nDaftar Hotel sesuai dengan harga kamar termurah:")
                  for hotel in daftar_kamar:
                      hotel.tampilkan_info()
                  print("__________Harga Termurah__________\n")

          elif pilihan == 2:
              # Cari hotel
              kata_kunci = get_input("--------------------\nMasukkan nama hotel yang ingin dicari: ")
              ditemukan = False
              for hotel in [hotel1, hotel2, hotel3]:
                  if hotel.cocokkan_nama(kata_kunci):
                      hotel.tampilkan_info()
                      ditemukan = True
              print("__________Hasil pencarian__________\n")
              if not ditemukan:
                  print(
                      "-------------------\nHotel tidak ditemukan.\n-------------------\n")

          elif pilihan == 3:
              # Pilih hotel
              print("--------------------\nPilihan Hotel:\n")
              for hotel in [hotel1, hotel2, hotel3]:
                  hotel.tampilkan_info()
              hotel_pilihan = get_input("-------------------\nPilih hotel: ").lower()
              print(
                  f"-------------------\nAnda memilih {hotel_pilihan}")
              # Validasi input
              if not validasi_input(hotel_pilihan):
                  print("--------------------\nInput tidak valid!\n-------------------\n")
                  continue

              # Pilih kamar
              print("-------------------\nPilihan Kamar:\n")
              for kamar in [kamar1, kamar2, kamar3]:
                  kamar.tampilkan_info()
              kamar_pilihan = get_input("-------------------\nPilih kamar: ").lower()
              print(
                  f"-------------------\nAnda memilih {kamar_pilihan}\n-------------------")
              print()
              # Validasi input
              if not validasi_input(kamar_pilihan):
                  print("-------------------\nInput tidak valid!\n-------------------\n")
                  continue

              # Buat pesanan

              # Temukan objek hotel yang sesuai dengan pilihan pengguna
              selected_hotel = None
              for hotel in [hotel1, hotel2, hotel3]:
                  if hotel.cocokkan_nama(hotel_pilihan):
                      selected_hotel = hotel
                      break

              # Temukan objek kamar yang sesuai dengan pilihan pengguna
              selected_kamar = None
              for kamar in [kamar1, kamar2, kamar3]:
                  if kamar.jenis.lower() == kamar_pilihan.lower():
                      selected_kamar = kamar
                      break

              # Validasi pemilihan hotel dan kamar
              if selected_hotel is not None and selected_kamar is not None:
                  pesanan = Pesanan(selected_hotel, selected_kamar, datetime.date.today(
                  ), datetime.date.today() + datetime.timedelta(days=1))
                  daftar_pesanan.append(pesanan)
                  buat_pesanan(pesanan)
                  print("__________Pesanan berhasil dibuat!__________\n")

              else:
                  print(
                      "-------------------\nHotel atau kamar tidak valid. Pesanan tidak dapat dibuat.\n-------------------\n")

          elif pilihan == 4:
              # Buka file data pesanan spesifik user
              nama_file = "data_" + username + ".txt"
              file_pesanan = open(nama_file, "r")


             # Baca semua data
              data = file_pesanan.readlines()

            # Selection sort
              for i in range(len(data)):
                min_index = i
                for j in range(i+1, len(data)):
                    if data[min_index] > data[j]:
                        min_index = j

                data[i], data[min_index] = data[min_index], data[i]

            # Balik urutan
              data = data[::-1]

            # Tampilkan
              print("-------------------\nDaftar Pesanan:\n")
              for line in data:
                print(line)
              print("__________Pesanan__________")



          elif pilihan == 5:
            main_menu()

          else :
            print(
                "-------------------\nMENU TIDAK TERSEDIA\nHarap pilih angka antara 1 sampai dengan 5\n-------------------\n")
            home()

  if __name__ == "__main__":
      main()

main_menu()
