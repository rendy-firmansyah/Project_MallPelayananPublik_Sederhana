
try:
    class Node: #Buat LinkedListnya
        def __init__(self, dataLis):
            self.item = dataLis
            self.ref = None
            
    class LinkedList:
        def __init__(self):
            self.nodeAwal = None
        
        def cetakPermohonan(self):
            if self.nodeAwal is None:
                print("List has no element")
                return
            else:
                n = self.nodeAwal
                while n is not None:
                    print(n.item , " ")
                    n = n.ref
            input()
            self.menu()

        def insert_at_start(self, data):
            nodeBaru = Node(data)
            nodeBaru.ref = self.nodeAwal
            self.nodeAwal= nodeBaru
        
        def insert_at_end(self, data):
            new_node = Node(data)
            if self.nodeAwal is None:
                self.nodeAwal = new_node
                return
            n = self.nodeAwal
            while n.ref is not None:
                n= n.ref
            n.ref = new_node;
    
    class antrianQueue:
        def __init__(self,n=50):
            self.size = n
            self.sizeIn = 0
            self.data = []
        def antrianFull(self):
            if self.sizeIn == self.size:
                return True
            else:
                return False
        def antrianKosong(self):
            if self.sizeIn == 0:
                return True
            else:
                return False
        def enqueue(self,name):
            if self.antrianFull():
                print("Mohon Maaf Sementara Ini Antrian Sudah Terlalu Penuh")
                print("Silahkan Menunggu Terlebih Dahulu ! Terima Kasih.")
            else:
                self.data.append(name)
                self.sizeIn = len(self.data)
                print(name,"Telah berhasil ditambahkan ke antrian.")
            print("Tekan enter untuk lanjut")
            input()
            self.menu()
        def dequeue(self):
            if self.antrianKosong():
                print("Antrian masih dalam keadaan kosong")
                return None
            else:
                clearData = self.data.pop(0)
                self.sizeIn == len(self.data)
                print("Antrian dengan nama :", clearData)
                print("Dimohon untuk melakukan konfirmasi")
                print("Antrian setelah ini adalah :", self.data)
            print("Tekan enter untuk lanjut")
            input()
            self.menu()
        def lihatAntrian(self):
            if self.antrianKosong():
                print("Saat ini antrian masih kosong")
            else:
                print("========== DAFTAR ANTRIAN MALL PELAYANAN PUBLIK ==========")
                number = 1
                for i in self.data:
                    print(" "+str(number)+". ",i)
                    number += 1
                print("Total antrian saat ini :", len(self.data))
            print("Tekan enter untuk lanjut")
            input()
            self.menu()
        def exit(self):
            print("Terima Kasih telah menggunakan Mall Pelayanan Publik Jember")
            import sys
            sys.exit()
        def pengajuanPermohonanKK(self):
            global savePeople_data
            savePeople_data = LinkedList()
            dataOne = input("Masukkan NIK : ")
            savePeople_data.insert_at_start(dataOne)
            dataTwo = input("Masukka No.KTP : ")
            savePeople_data.insert_at_end(dataTwo)
            dataThree = input("Masukkan Tempat, Tanggal Lahir : ")
            savePeople_data.insert_at_end(dataThree)
            print("======= Data telah masuk ke dalam layanan ========")
            print("====== Mohon tunggu proses permohonan anda =======")
            print("Tekan enter untuk lanjut")
            input()
            self.menu()
        def pengajuanPermohonanKTP(self):
            global savePeople_data
            savePeople_data = LinkedList()
            dataOne = input("Masukkan Nama Lengkap : ")
            savePeople_data.insert_at_start(dataOne)
            dataTwo = input("Masukka No.KK : ")
            savePeople_data.insert_at_end(dataTwo)
            dataThree = input("Masukka Gol. Darah : ")
            savePeople_data.insert_at_end(dataThree)
            dataFour = input("Masukkan Tempat, Tanggal Lahir : ")
            savePeople_data.insert_at_end(dataFour)
            dataFive = input("Masukkan Nomor Telepon : ")
            savePeople_data.insert_at_end(dataFive)
            print("======= Data telah masuk ke dalam layanan ========")
            print("====== Mohon tunggu proses permohonan anda =======")
            print("Tekan enter untuk lanjut")
            input()
            self.menu()

        def pengajuanPermohonanAktaKelahiran(self):
            global savePeople_data
            savePeople_data = LinkedList()
            dataOne = input("Masukka No.KK :  ")
            savePeople_data.insert_at_start(dataOne)
            dataTwo = input("Masukkan Nama Lengkap Ibu :")
            savePeople_data.insert_at_end(dataTwo)
            dataThree = input("Masukkan NIK Ibu: ")
            savePeople_data.insert_at_end(dataThree)
            dataFour = input("Masukkan Nama Anak  ")
            savePeople_data.insert_at_end(dataFour)
            dataFive = input("Masukkan Tempat, Tanggal Lahir :")
            savePeople_data.insert_at_end(dataFive)
            dataSix = input("Masukkan Jenis Kelamin : ")
            savePeople_data.insert_at_start(dataSix)
            dataSeven = input("Masukkan Anak ke : ")
            savePeople_data.insert_at_end(dataSeven)
            dataEight = input("Masukkan Nama Saksi: ")
            savePeople_data.insert_at_end(dataEight)
            dataNine = input("Masukkan NIK Saksi : ")
            savePeople_data.insert_at_end(dataNine)
            dataTen = input("Masukkan Nomor Akta Pernikahan : ")
            savePeople_data.insert_at_end(dataTen)
            print("======= Data telah masuk ke dalam layanan ========")
            print("====== Mohon tunggu proses permohonan anda =======")
            print("Tekan enter untuk lanjut")
            input()
            self.menu()

        def pengajuanPermohonanAktaPernikahan(self):
            global savePeople_data
            savePeople_data = LinkedList()
            dataOne = input("Masukkan Nomor Surat Bukti Perkawinan :  ")
            savePeople_data.insert_at_start(dataOne)
            dataTwo = input("Masukkan Nomor Akte pria :")
            savePeople_data.insert_at_end(dataTwo)
            dataThree = input("Masukkan Nomor Akte Wanita : ")
            savePeople_data.insert_at_end(dataThree)
            dataFour = input("Masukkan No Surat Keterangan Lurah:  ")
            savePeople_data.insert_at_end(dataFour)
            dataFive = input("Masukkan NIK Pria :")
            savePeople_data.insert_at_end(dataFive)
            dataSix = input("Masukkan NIK Wanita : ")
            savePeople_data.insert_at_start(dataSix)
            dataSeven = input("Masukkan Nama saksi 1 : ")
            savePeople_data.insert_at_end(dataSeven)
            dataEight = input("Masukkan Nama Saksi 2: ")
            savePeople_data.insert_at_end(dataEight)
            dataNine = input("Masukkan NIK Saksi 1: ")
            savePeople_data.insert_at_end(dataNine)
            dataTen = input("Masukkan NIK Saksi 2: ")
            savePeople_data.insert_at_end(dataTen)
            print("======= Data telah masuk ke dalam layanan ========")
            print("====== Mohon tunggu proses permohonan anda =======")
            print("Tekan enter untuk lanjut")
            input()
            self.menu()


        def pengajuanPermohonanKIA(self):
            global savePeople_data
            savePeople_data = LinkedList()
            dataOne = input("Masukka NIK Ayah :  ")
            savePeople_data.insert_at_start(dataOne)
            dataTwo = input("Masukkan Nama Ayah:")
            savePeople_data.insert_at_end(dataTwo)
            dataThree = input("Masukkan NIK Ibu: ")
            savePeople_data.insert_at_end(dataThree)
            dataFour = input("Masukkan Nama Ibu  ")
            savePeople_data.insert_at_end(dataFour)
            dataFive = input("Masukkan Nomor Akta Kelahiran :")
            savePeople_data.insert_at_end(dataFive)
            dataSix = input("Masukkan No KK : ")
            savePeople_data.insert_at_start(dataSix)
            print("======= Data telah masuk ke dalam layanan ========")
            print("====== Mohon tunggu proses permohonan anda =======")
            print("Tekan enter untuk lanjut")
            input()
            self.menu()

        def menuPengajuan(self):
            import os
            os.system("cls")
            print("======================================")
            print("     MALL PELAYANAN PUBLIK JEMBER     ")
            print("======================================")
            print("| 1. Pembuatan KTP                   |")
            print("| 2. Pembuatan Kartu Keluarga        |")
            print("| 3. Pembuatan Akta Kelahiran        |")
            print("| 4. Pengurusan Akta Perkawinan      |")
            print("| 5. Pengurusan KIA                  |")
            print("| 6. Keluar Program                  |")
            print("======================================")
            
            inputMenu = int(input("Pilih Daftar Menu : "))
            if inputMenu == 1:
                self.pengajuanPermohonanKTP()
            elif inputMenu == 2:
                self.pengajuanPermohonanKK()
            elif inputMenu == 3:
                self.pengajuanPermohonanAktaKelahiran()
            elif inputMenu == 4:
                self.pengajuanPermohonanAktaPernikahan()
            elif inputMenu == 5:
                self.pengajuanPermohonanKIA()
            elif inputMenu == 6:
                self.exit
            else:
                print("Mohon maaf pilihan menu tidak ada")
        def menuCostumer(self):
            global savePeople_data
            import os
            os.system("cls")
            print("======================================")
            print("     MALL PELAYANAN PUBLIK JEMBER     ")
            print("======================================")
            print("| 1. Ambil  Antrian                  |")
            print("| 2. Keluar                          |")
            print("======================================") 
              
            inputProgram = int(input("Pilih Daftar Menu : "))
            if inputProgram == 1:
                dataAntrian = input("Masukkan nama antrian : ")
                self.enqueue(dataAntrian)
                input()
                self.menu()
            else:
                self.exit()
        
        def menu(self):
            global savePeople_data
            import os
            os.system("cls")
            print("======================================")
            print("     MALL PELAYANAN PUBLIK JEMBER     ")
            print("                 ADMIN                ")
            print("======================================")
            print("| 1. Lihat Daftar Antrian            |")
            print("| 2. Panggil Antrian                 |")
            print("| 3. Pengajuan Permohonan            |")
            print("| 4. Data Permohonan                 |")
            print("| 5. Keluar Program                  |")
            print("======================================")
                
            inputProgram = int(input("Pilih Daftar Menu : "))
            if inputProgram == 1:
                self.lihatAntrian()
            elif inputProgram == 2:
                self.dequeue()
            elif inputProgram == 3:
                self.menuPengajuan()
                
            elif inputProgram == 4:
                savePeople_data.cetakPermohonan()
                input()
                self.menu()
            elif inputProgram == 5:
                self.exit()
            else:
                print("Mohon maaf pilihan menu tidak sesuai !")
                print("Tekan enter untuk kembali ke menu")
                input()
                self.menu()
    tes = antrianQueue()
    tes.menuCostumer()
except ValueError:
    print("Program Not Responding")