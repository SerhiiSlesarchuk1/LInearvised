import funktsioonid as f

def menuu():
    while True:
        print("""
1. Lisa kontakt
2. Kuva kontaktid
3. Otsi kontakti
4. Kustuta kontakt
5. Muuda kontakti
6. Sorteeri kontaktid
7. Saada e-kiri
8. Välju
        """)
        valik=input("Vali tegevus: ")
        if valik=="1":
            nimi=input("Nimi: ")
            telefon=input("Telefon: ")
            email=input("Email: ")
            f.lisa_kontakt(nimi, telefon, email)
        elif valik=="2":
            f.kuva_kontaktid()
        elif valik=="3":
            nimi=input("Sisesta nimi otsimiseks: ")
            tulemused = f.otsi_kontakt(nimi)
            for k in tulemused:
                print(k)
        elif valik=="4":
            nimi=input("Sisesta kustutatava kontakti nimi: ")
            f.kustuta_kontakt(nimi)
        elif valik=="5":
            vana=input("Vana nimi: ")
            uus_nimi=input("Uus nimi: ")
            uus_tel=input("Uus telefon: ")
            uus_email=input("Uus email: ")
            f.muuda_kontakt(vana, uus_nimi, uus_tel, uus_email)
        elif valik=="6":
            kategooria=input("Sorteeri mille järgi (nimi/telefon/email): ")
            sorted_kontaktid=f.sorteeri_kontaktid(kategooria)
            for k in sorted_kontaktid:
                print(k)
        elif valik=="7":
            nimi=input("Sisesta kontakti nimi: ")
            kontaktid=f.otsi_kontakt(nimi)
            if kontaktid:
                sonum=input("Sisesta sõnum: ")
                f.saada_email(kontaktid[0]["email"], sonum)
            else:
                print("Kontakti ei leitud.")
        elif valik=="8":
            break
        else:
            print("Tundmatu valik.")
menuu()

 