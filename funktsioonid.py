import json
import os
import smtplib
from email.mime.text import MIMEText

FILENAME="kontaktid.json"

def loe_kontaktid():
    if not os.path.exists(FILENAME):
        with open(FILENAME,"w") as f:
            json.dump([], f)
    with open(FILENAME,"r") as f:
        return json.load(f)

def kirjuta_kontaktid(kontaktid):
    with open(FILENAME,"w") as f:
        json.dump(kontaktid,f,indent=4)

def lisa_kontakt(nimi, telefon, email):
    kontaktid=loe_kontaktid()
    kontaktid.append({"nimi": nimi, "telefon": telefon, "email": email})
    kirjuta_kontaktid(kontaktid)

def kuva_kontaktid():
    kontaktid=loe_kontaktid()
    for k in kontaktid:
        print(f"Nimi: {k['nimi']}, Telefon: {k['telefon']}, Email: {k['email']}")

def otsi_kontakt(nimi):
    kontaktid=loe_kontaktid()
    return [k for k in kontaktid if nimi.lower() in k['nimi'].lower()]

def kustuta_kontakt(nimi):
    kontaktid = loe_kontaktid()
    uus=[k for k in kontaktid if k['nimi'].lower()!=nimi.lower()]
    kirjuta_kontaktid(uus)

def muuda_kontakt(vana_nimi, uus_nimi, uus_telefon, uus_email):
    kontaktid=loe_kontaktid()
    for k in kontaktid:         
        if k['nimi'].lower()==vana_nimi.lower():
            k['nimi']=uus_nimi
            k['telefon']=uus_telefon
            k['email']=uus_email
            break
    kirjuta_kontaktid(kontaktid)

def sorteeri_kontaktid(kategooria):
    kontaktid=loe_kontaktid()
    if kategooria in ["nimi", "telefon", "email"]:
        kontaktid.sort(key=lambda x: x[kategooria])
    return kontaktid

def saada_email(saaja_email, sonum):
    saatja_email="sinu_email@example.com"
    saatja_parool="sinu_parool"
    msg=MIMEText(sonum)
    msg["Subject"]="Tervitus telefoniraamatust"
    msg["From"]=saatja_email
    msg["To"]=saaja_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(saatja_email, saatja_parool)
        server.send_message(msg)

