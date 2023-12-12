mahasiswa=[]
def data_masuk():
   nama  = input("Masukkan Nama Mahasiswa: ")
   nilai1=int(input("Masukkan Nilai Praktikum 1: "))
   nilai2=int(input("Masukkan Nilai Praktikum 2: "))
   nilai3=int(input("Masukkan Nilai Praktikum 3: "))
   list=[nama,nilai1,nilai2,nilai3]
   mahasiswa.insert(len(mahasiswa),list)
   main()

def data():
    print(" NAMA |","PRAK 1|","PRAK 2|","PRAK 3|")
    for i in mahasiswa:
        print(i[0],"",i[1],"\t",i[2],"\t",i[3])
    main()

def nilaimahasiswa():
    for i in range(len(mahasiswa)):
        total = sum(mahasiswa[i][1:])  
        rata_rata = total / (len(mahasiswa[i]) - 1) 
        print(mahasiswa[i][0], "=", rata_rata)
    main()

def nilaipraktikum():
    total_praktikum = [0, 0, 0]
    for i in range(len(mahasiswa)):
        for j in range(1, 4):
            total_praktikum[j - 1] += mahasiswa[i][j]
    rata_praktikum = [total / len(mahasiswa) for total in total_praktikum]
    for i, rata in enumerate(rata_praktikum):
        print(f"Nilai rata-rata praktikum {i + 1} = {rata}")
    main()

def nilairatarata():
    nama_cari = input("Masukkan Nama Mahasiswa yang ingin dicari rata-ratanya: ")
    found = False
    for i in range(len(mahasiswa)):
        if mahasiswa[i][0] == nama_cari:
            total = sum(mahasiswa[i][1:])
            rata_rata = total / len(mahasiswa[i][1:])
            print("Rata-rata nilai untuk", nama_cari, "adalah:", rata_rata)
            found = True
            break
    
    if not found:
        print("Mahasiswa dengan nama", nama_cari, "tidak ditemukan.")
    main()

def update_nilai():
    update=input("Nama Yang Dicari :")
    nilai=int(input("Ingin Update nilai Praktikum ke-: "))
    nilai_baru=int(input("Nilai Baru: "))
    for i in mahasiswa:
        if i [0]==update:
            i[nilai]=nilai_baru
    main()

def main():
    print("Program Membuat List")
    print("1.Memasukkan nama dan nilai")
    print("2.Lihat data")
    print("3.Nilai rata-rata mahasiswa")
    print("4.Nilai rata-rata setiap praktikum mahasiswa")
    print("5.Mencari nilai rata-rata dari setiap mahasiswa")
    print("6.Mengubah nilai mahasiswa")
    print("7.Keluar")
    pilih=int(input("Silahkan pilih (ketik 7 jika ingin keluar):"))
    if pilih==1:
        data_masuk()
    elif pilih==2:
        data()
    elif pilih==3:
        nilaimahasiswa()
    elif pilih==4:
        nilaipraktikum()
    elif pilih==5:
        nilairatarata()
    elif pilih==6:
        update_nilai()
    elif pilih==7:
        exit()
    else:
        print("Keyword yang kamu masukan salah!")
        pilih=int(input("Silahkan pilih (ketik 7 jika ingin keluar):"))
main()
