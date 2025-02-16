from tabulate import tabulate
daftar_suku_cadang = [
    {"Nama": "Rear Brake", "Kode SKU": 10011 , "Stok": 3, "Satuan": "Set", "Harga": 50000, "Gudang": "Gudang Suku Cadang"},
    {"Nama": "Windshield", "Kode SKU": 10012, "Stok": 2, "Satuan": "Pcs", "Harga": 300000, "Gudang": "Gudang Aksesoris"},
    {"Nama": "Oli Matic", "Kode SKU": 10013, "Stok": 20, "Satuan": "Liter", "Harga": 85000, "Gudang": "Gudang Suku Cadang"},
    {"Nama": "Hand Grip", "Kode SKU": 10014, "Stok": 5, "Satuan": "Pcs", "Harga": 55000, "Gudang": "Gudang Aksesoris"}
]
def inputString(string):
    while True:
        object=(input(f'{string}')).strip()
        if object.replace(' ', '').isalpha():
            return object
        else:
            print('Data Yang dientry Tidak Valid !!!')
        

def inputAngka(promp):
    while True:
        try:
            angka=int(input(f'{promp}: '))
            if angka<0:
                print('Angka yang diinput harus bernilai Positif')
            else:
                break
        except:
            print('Yang diinput harus angka')
    return angka


def melanjutkan_menu(string):
    while True:
        object = (input(f'{string}')).strip().lower()
        if object == "ya":
            return True
        elif object == "tidak":
            return False
        else:
            print("Hanya menerima jawaban Ya/Tidak")

#   MAIN MENU
def main_menu():
    while True:            
        print("""\nSelamat Datang di Mechanic Workshop:
        1. Daftar Barang per Gudang
        2. Merubah Daftar Barang
        3. Menambah Barang Baru
        4. Menghapus Barang Dari Daftar
        5. Exit""")
        pilihan = inputAngka("Masukkan menu yang ingin dipilih: ")
        if pilihan == 1:
            daftar_barang_per_gudang()
        elif pilihan == 2:
            merubah_daftar_barang()
        elif pilihan == 3:
            menambah_barang()
        elif pilihan == 4:
            menghapus_barang()
        elif pilihan == 5:
            break
        else:
            print("Input yang anda masukkan tidak terdapat dalam daftar")
    print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI <3:*")
            
# READ MENU
# Menampilkan Daftar Barang per Gudang (Menu 1)
def daftar_barang_per_gudang():
    while True:
        print('''Silahkan pilih daftar barang yang ingin di tampilkan:
            1. Keseluruhan barang
            2. Barang-barang tertentu
            3. Kembali ke menu utama''')
    
        masukkan_pilihan = inputAngka("Masukkan nomor yang anda pilih: ")

        if masukkan_pilihan == 1:
            print("Berikut adalah daftar seluruh barang yang tersedia di Mechanic Workshop")
            print(tabulate(daftar_suku_cadang,headers="keys",tablefmt="fancy_grid"))

        elif masukkan_pilihan == 2:
            while True:
                kode_SKU = inputAngka("Masukkan kode SKU barang: ")
                found = False
                for value in daftar_suku_cadang:
                    if value ['Kode SKU'] == kode_SKU:
                        found = True
                        print("Barang ditemukan.")
                        print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                        break
                if found:
                   if not melanjutkan_menu("Apakah anda ingin melihat daftar barang lain? (ya/tidak): "):
                       break    
                else:
                    print("Barang tidak terdapat dalam daftar")
            
        elif masukkan_pilihan == 3:
            if melanjutkan_menu("Apakah anda ingin keluar dari menu daftar barang per gudang?(Ya/Tidak): "):
                break
        else:
            print("Angka yang anda masukkan tidak terdapat dalam sub menu.")
            
# UPDATE MENU
# Untuk Merubah Daftar Barang(Menu 2)
def merubah_daftar_barang():
    while True:
        print('''Anda memasuki menu merubah daftar barang, silahkan pilih daftar apa yang ingin anda ubah:
              1. Nama Barang
              2. Stok
              3. Satuan
              4. Harga
              5. Gudang
              6. Kembali ke menu utama ''')
        pilih = inputAngka("Pilih daftar yang ingin anda ubah: ")
        if pilih == 1:
            while True:
                SKU = inputAngka(f'Masukkan kode SKU untuk barang yang ingin diubah namanya: ')
                found = False
                for value in daftar_suku_cadang:
                    if value ['Kode SKU'] == SKU:
                        found = True
                        print("Barang ditemukan")
                        print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                        while True:
                            nama_baru = inputString("Masukkan nama barang baru: ").title()
                            sudah_ada = any(value["Nama"] == nama_baru for value in daftar_suku_cadang)
                            if sudah_ada:
                                print(f'Barang dengan nama {nama_baru} sudah ada dalam daftar')
                                continue
                            break
                        while True:
                            simpan = inputString("Simpan data? (Ya/Tidak): ").lower()
                            if simpan == "ya":
                                value['Nama'] = nama_baru.title().strip()
                                print("Barang berhasil diubah.")
                                print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                                break
                            elif simpan == "tidak":
                                print("Barang batal diubah.")
                                break
                            else:
                                print("Hanya menerima jawaban ya/tidak")
                        break     
                if found:
                    if not melanjutkan_menu("Apakah anda ingin melanjutkan menu merubah barang? (ya/tidak): "):
                        break
                else:
                    print("Barang tidak ditemukan, silahkan coba lagi.")

        elif pilih == 2:
            while True:
                SKU = inputAngka(f'Masukkan kode SKU untuk barang yang ingin diubah stoknya: ')
                found = False
                for value in daftar_suku_cadang:
                    if value ['Kode SKU'] == SKU:
                        found =True
                        print("Barang ditemukan")
                        print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                        while True:
                            stok_baru = inputAngka("Masukkan jumlah stok baru: ")
                            sudah_ada = any(value["Stok"] == stok_baru for value in daftar_suku_cadang if value["Kode SKU"]==SKU)
                            if sudah_ada:
                                print(f'Barang {value["Nama"]} sudah {stok_baru} stoknya')
                                continue
                            break
                        while True:
                            simpan = inputString("Simpan data? (Ya/Tidak): ").lower()
                            if simpan == "ya":
                                value['Stok'] = stok_baru
                                print("Stok berhasil diubah.")
                                print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                                break
                            elif simpan == "tidak":
                                print("Stok batal diubah.")
                                break
                            else:
                                print("Hanya menerima jawaban ya/tidak")
                        break
                if found:
                    if not melanjutkan_menu("Apakah anda ingin melanjutkan menu merubah barang? (ya/tidak): "):
                        break
                else:
                    print("Barang tidak ditemukan, silahkan coba lagi.")
        
        elif pilih == 3:
            while True:
                SKU = inputAngka(f'Masukkan kode SKU untuk barang yang ingin diubah satuannya: ')
                found = False
                for value in daftar_suku_cadang:
                    if value ['Kode SKU'] == SKU:
                        found = True
                        print("Barang ditemukan")
                        print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                        while True:
                            satuan_baru = inputString("Masukkan nama satuan baru: ").capitalize()
                            sudah_ada = any(value["Satuan"] == satuan_baru for value in daftar_suku_cadang if value["Kode SKU"]==SKU)
                            if sudah_ada:
                                print(f'Barang {value["Nama"]} sudah {satuan_baru} satuannya')
                                continue
                            break
                        while True:
                            simpan = inputString("Simpan data? (Ya/Tidak): ").lower()
                            if simpan == "ya":
                                value['Satuan'] = satuan_baru
                                print("Satuan berhasil diubah.")
                                print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                                break
                            elif simpan == "tidak":
                                print("Satuan batal diubah.")
                                break
                            else:
                                print("Hanya menerima jawaban ya/tidak")
                        break
                if found:
                    if not melanjutkan_menu("Apakah anda ingin melanjutkan menu merubah barang? (ya/tidak): "):
                        break   
                else:
                    print("Barang tidak ditemukan, silahkan coba lagi.")
        elif pilih == 4:
            while True:
                SKU = inputAngka(f'Masukkan kode SKU untuk barang yang ingin diubah harganya: ')
                found = False
                for value in daftar_suku_cadang:
                    if value ['Kode SKU'] == SKU:
                        found = True
                        print("Barang ditemukan")
                        print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                        while True:
                            harga_baru = inputAngka("Masukkan harga baru barang: ")
                            sudah_ada = any(value["Harga"] == harga_baru for value in daftar_suku_cadang if value["Kode SKU"]==SKU)
                            if sudah_ada:
                                print(f'Barang {value["Nama"]} sudah {harga_baru} harganya')
                                continue
                            break
                        while True:
                            simpan = inputString("Simpan data? (Ya/Tidak): ").lower()
                            if simpan == "ya":
                                value['Harga'] = harga_baru
                                print("Harga berhasil diubah.")
                                print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                                break
                            elif simpan == "tidak":
                                print("Harga batal diubah.")
                                break
                            else:
                                print("Hanya menerima jawaban ya/tidak")
                        break
                if found:
                        if not melanjutkan_menu("Apakah anda ingin melanjutkan menu merubah barang? (ya/tidak): "):
                            break
                else:
                    print("Barang tidak ditemukan, silahkan coba lagi.")

        elif pilih == 5:
            while True:
                SKU = inputAngka(f'Masukkan kode SKU untuk barang yang diubah letak gudangnya: ')
                found = False
                for value in daftar_suku_cadang:
                    if value ['Kode SKU'] == SKU:
                        found = True
                        print("Barang ditemukan")
                        print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                        while True:
                            gudang_baru = inputString("Masukkan nama gudang baru: ").title()
                            if gudang_baru not in ["Gudang Aksesoris", "Gudang Suku Cadang"]:
                                print("Gudang yang terdapat hanya Gudang Aksesoris dan Gudang Suku Cadang")
                                continue
                            if value["Gudang"] == gudang_baru:
                                print(f"Barang {value['Nama']} sudah berada di {gudang_baru}")
                                continue
                            break
                        while True:
                            simpan = inputString("Simpan data? (Ya/Tidak): ").lower()
                            if simpan == "ya":
                                value['Gudang'] = gudang_baru.title().strip()
                                print("Gudang berhasil diubah.")
                                print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                                break
                            elif simpan == "tidak":
                                print("Gudang batal diubah.")
                                break
                            else:
                                print("Hanya menerima jawaban ya/tidak")
                if found:
                        if not melanjutkan_menu("Apakah anda ingin melanjutkan menu merubah barang? (ya/tidak): "):
                            break
        elif pilih == 6:
            if melanjutkan_menu("Apakah anda ingin keluar dari menu mengubah barang? (Ya/Tidak): "):
                break
        else:
            print("Angka yang anda masukkan tidak teradpat dalam sub menu.")
            
# CREATE MENU
# Untuk Menambah Barang(Menu 3)
def menambah_barang():
    while True:
        print('''Silahkan pilih sub menu yang ingin dijalankan: 
              1. Menambahkan barang
              2. Kembali ke menu utama''')
        pilih = inputAngka("Masukkan sub menu yang ingin anda jalankan: ")
        
        if pilih == 1:
            while True:
                nama = inputString("Masukkan nama barang yang ingin ditambahkan: ").title()
                # cek jika barang sudah ada
                sudah_ada = any(value["Nama"] == nama for value in daftar_suku_cadang)
                if sudah_ada:
                    print(f"Barang dengan nama {nama} sudah ada dalam daftar, masukkan barang lain")
                    continue
                qty = inputAngka("Masukkan kuantitas barang: ")
                satuan = inputString("Masukkan nama satuan barang: ").capitalize()
                harga = inputAngka("Masukkan harga barang: ")
                while True:
                    gudang = inputString("Masukkan letak gudang: ").title()
                    if gudang not in ["Gudang Aksesoris", "Gudang Suku Cadang"]:
                        print("Gudang yang terdapat hanya Gudang Aksesoris dan Gudang Suku Cadang")
                        continue
                    break
                barang_tambahan = {
                    "Nama" : nama,
                    "Kode SKU" : 10011 + len(daftar_suku_cadang), #memastikan SKU agar tetap unik
                    "Stok" : qty,
                    "Satuan" : satuan,
                    "Harga" : harga,
                    "Gudang" : gudang
                }
                daftar_suku_cadang.append(barang_tambahan)
                while True:
                    simpan = inputString("Simpan data ini? (Ya/Tidak): ")
                    if simpan == "ya":
                        print("Barang baru berhasil ditambahkan ke dalam daftar")
                        print(tabulate(daftar_suku_cadang,headers="keys",tablefmt="fancy_grid"))  
                        break  
                    elif simpan == "tidak":
                        print("Barang batal disimpan.")
                        break
                    else:
                        print("Hanya menerima jawaban ya/tidak.")
                if not melanjutkan_menu("Apakah anda ingin menambah barang lainnya? (Ya/Tidak): "):
                    break
                
        elif pilih == 2:
            if melanjutkan_menu("Apakah anda ingin keluar dari menu menambah barang?(Ya/Tidak): "):
                break
        else:
            print("Angka tidak terdapat dalam sub menu.")
            
        
# DELETE MENU
# Untuk Menghapus Barang Dari Daftar (Menu 4)
def menghapus_barang():
    while True:
        print('''Silahkan pilih sub menu yang ingin dijalankan: 
            1. Menghapus Berdasarkan SKU
            2. Menghapus Berdasarkan Nama
            3. Kembali Ke Menu Utama''')
        pilih = inputAngka("Masukkan sub menu yang ingin di jalankan: ")
        if pilih == 1:
            while True:
                print(tabulate(daftar_suku_cadang,headers="keys",tablefmt="fancy_grid"))
                SKU = inputAngka("Masukkan kode SKU barang yang ingin dihapus: ")
                found = False
                for value in daftar_suku_cadang:
                    if value["Kode SKU"] == SKU:
                        found = True
                        print("Barang ditemukan")
                        print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                        daftar_suku_cadang.remove(value)
                        while True:
                            simpan = inputString("Apakah anda yakin ingin menghapus barang ini?(Ya/Tidak): ").lower()
                            if simpan == "ya":
                                print("Barang berhasil dihapus.")
                                print(tabulate(daftar_suku_cadang,headers="keys",tablefmt="fancy_grid"))
                                break
                            elif simpan == "tidak":
                                print("Barang batal dihapus")
                                break
                            else:
                                print("Hanya menerima jawaban ya/tidak")
                if found:
                        if not melanjutkan_menu("Apakah anda ingin melanjutkan menu menghapus barang? (ya/tidak): "):
                            break
                else:
                    print("Barang tidak ditemukan, silahkan coba lagi.")
                    

        if pilih == 2:
            while True:
                print(tabulate(daftar_suku_cadang,headers="keys",tablefmt="fancy_grid"))
                nama = inputString("Masukkan nama barang yang ingin dihapus: ")
                found = False
                for value in daftar_suku_cadang:
                    if value["Nama"].lower() == nama.lower():
                        found = True
                        print("Barang ditemukan")
                        print(tabulate([value],headers="keys",tablefmt="fancy_grid"))
                        daftar_suku_cadang.remove(value)
                        while True:
                            simpan = inputString("Apakah anda ingin menhapus barang ini? (Ya/Tidak): ").lower()
                            if simpan == "ya":
                                print("Barang berhasil di hapus")
                                print(tabulate(daftar_suku_cadang,headers="keys",tablefmt="fancy_grid"))
                                break
                            elif simpan == "tidak":
                                print("Barang batal dihapus")
                                break
                            else:
                                print("Hanya menerima jawaban ya/tidak")
                if found:
                        if not melanjutkan_menu("Apakah anda ingin melanjutkan menu merubah barang? (ya/tidak): "):
                            break
                else:
                    print("Barang tidak ditemukan, silahkan coba lagi.")

        elif pilih == 3:
            if melanjutkan_menu("Apakah anda ingin keluar dari menu menghapus barang?(Ya/Tidak): "):
                main_menu()
        else:
            print("Angka tidak terdapat dalam sub menu.")

main_menu()                           

                        
            


                        
    


    

    