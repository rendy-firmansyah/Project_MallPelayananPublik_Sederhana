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
            print("Anda telah keluar dari program")
            import sys
            sys.exit()
        def pengajuanPermohonan(self):
            global savePeople_data
            savePeople_data = LinkedList()
            dataOne = input("Masukkan NIK : ")
            savePeople_data.insert_at_start(dataOne)
            dataTwo = input("Masukka No.KTP : ")
            savePeople_data.insert_at_start(dataTwo)
            dataThree = input("Masukkan Tempat, Tanggal Lahir : ")
            savePeople_data.insert_at_start(dataThree)
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
                pass
            elif inputMenu == 2:
                pass
            elif inputMenu == 3:
                pass
            elif inputMenu == 4:
                pass
            elif inputMenu == 5:
                pass
            elif inputMenu == 6:
                pass
            else:
                print("Mohon maaf pilihan menu tidak ada")
        def menu(self):
            global savePeople_data
            import os
            os.system("cls")
            print("======================================")
            print("     MALL PELAYANAN PUBLIK JEMBER     ")
            print("======================================")
            print("| 1. Tambah Antrian                  |")
            print("| 2. Lihat Daftar Antrian            |")
            print("| 3. Panggil Antrian                 |")
            print("| 4. Pengajuan Permohonan            |")
            print("| 5. Data Permohonan                 |")
            print("| 6. Keluar Program                  |")
            print("======================================")
                
            inputProgram = int(input("Pilih Daftar Menu : "))
            if inputProgram == 1:
                dataAntrian = input("Masukkan nama antrian : ")
                self.enqueue(dataAntrian)
            elif inputProgram == 2:
                self.lihatAntrian()
            elif inputProgram == 3:
                self.dequeue()
            elif inputProgram == 4:
                self.menuPengajuan()
                
            elif inputProgram == 5:
                savePeople_data.cetakPermohonan()
            elif inputProgram == 6:
                self.exit()
            else:
                print("Mohon maaf pilihan menu tidak sesuai !")
                print("Tekan enter untuk kembali ke menu")
                input()
                self.menu
    tes = antrianQueue()
    tes.menu()
except ValueError:
    print("Program Not Responding")
