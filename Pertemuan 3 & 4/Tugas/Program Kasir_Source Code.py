pilihan="y"
while pilihan=="y":
    print("===================================================")
    print("                  OMAGAD MILK ")
    print("===================================================")

    pembeli = input("Masukkan nama anda     : ")
    alamat= str(input("Masukkan alamat anda   : "))
    telp= int(input("Masukan no telpon      : "))

    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("==================================================")
    print("             List Menu Susu OMAGAD ")
    print("==================================================")
    print("""
    1. OMAGAD BREAD : Rp 7.000
    2. OMAGAD ICE MILK CHOCOLATE: Rp 13.000
    3. OMAGAD ICE MILK VANILLA: Rp 10.000
    4. OMAGAD ICE MILK STRAWBERRY: Rp 13.000
    5. OMAGAD ICE MILK CHOCOLATE & VANILLA: Rp 18.000
    6. OMAGAD ICE MILK STRAWBERRY & VANILLA: Rp 18.000""")

    print("==================================================")
    pesan=input("masukkan nomor list pesanan         = ")
    print("==================================================")
    jumlahpesan=int(input("masukkan jumlah pesanan  = "))

    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    harga1=7000
    harga2=13000
    harga3=10000
    harga4=13000
    harga5=18000
    harga6=18000
    if pesan == "1":
        listnama= "OMAGAD BREAD"
        listharga= "7000"
        harga=(7000*jumlahpesan)
        ppn= int(harga * 0.1)
        totalharga=int(harga+ppn)
    elif pesan == "2":
        listnama= "OMAGAD ICE MILK CHOCOLATE"
        listharga= "13000"
        harga = (13000*jumlahpesan)
        ppn = int(harga * 0.1)
        totalharga =int(harga+ppn)
    elif pesan == "3":
        listnama= "OMAGAD ICE MILK VANILLA"
        listharga= "10000"
        harga=int(10000*jumlahpesan)
        ppn = int(harga * 0.1)
        totalharga=int(harga+ppn)
    elif pesan == "4":
        listnama= "OMAGAD ICE MILK STARWBERRY"
        listharga= "13000"
        harga=int(13000*jumlahpesan)
        ppn = int(harga * 0.1)
        totalharga=int(harga+ppn)
    elif pesan == "5":
        listnama= "OMAGAD ICE MILK CHOCOLATE & VANILLA"
        listharga= "18000"
        harga=int(18000*jumlahpesan)
        ppn = int(harga * 0.1)
        totalharga = int(harga+ppn)
    elif pesan == "6":
        listnama= "OMAGAD ICE MILK STRAWBERRY & VANILLA"
        listharga= "18000"
        harga=int(18000*jumlahpesan)
        ppn = int(harga * 0.1)
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        listharga= "-"
        harga = "-"
        ppn = "-"
        totalharga = "-"
        pilihan=str(input("""
        Wahhh, menu ini tidak tersedia, 
        silahkan Coba lagi Y/N ="""))
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n====================================================================")
    print("====================== S T R U K   B E L I =========================")
    print("=================== O M A G A D   C O F F E E ======================")
    print("====================================================================")
    print("====================================================================")
    print("""\t Jalan Raya Jatidiri, RT. 13 / RW. 04, 
\t Jatidiri, Pondok Rumah, RT.009/RW.005, 
\t Jaticaka, Kec. Pd. Gede, Kota Bks, 
\t Jawa Barat 13077  No.Telp 0877-5690-2245""")
    print("=====================================================================")
    import datetime
 
    x = datetime.datetime.now()
    print(x.strftime("%c"))
    
    print("=====================================================================")

    format_str=f"Atas Nama       : {pembeli}"
    print(format_str)

    format_str2=f"Alamat          : {alamat}"
    print(format_str2)
    
    format_str3=f"Nomor Telpon    : {telp}"
    print(format_str3)
    
    print("=====================================================================")
    print("Menu                        :",listnama)
    print("Harga per Menu              : Rp.",listharga," x ", jumlahpesan)

    print("=====================================================================")
    print("Harga Total                 : Rp.", harga)
    print("PPN                         : Rp.",ppn)
    print("---------------------------------------------------------------------")
    print("Total Harga Yang Harus Di Bayar             : Rp.",totalharga)
    print("---------------------------------------------------------------------")
    print("SEMOGA HARIMU MENYENANGKAN:)")
    print("\n")
    pilihan=str(input("apakah anda ingin order kembali Y/N ="))