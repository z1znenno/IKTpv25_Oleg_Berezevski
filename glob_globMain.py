import glob_glob

while True:
    laiend = input("Sisestage mis fail teile on vaja(txt, py, java): ")
    if laiend not in ["py", "txt", "java", ".txt", ".py", ".java"]:
        print("Ma ei team mis laiend see on! Proovi uuesti.")
    else:
        break
koik_failid = glob_glob.leia_projeektifailid(laiend)
while True:
    valik = input(f"Mis fail tahate lugeda(1-{len(koik_failid)}): ")
    if valik.isdigit():
        valik = int(valik)
        valik = valik - 1
        break
    else:
        print("Proovige uuesti!")
marked_word = input("Mis sõna te otsite failis? ")
sisu, read, tuhi_read, minu_sõna = glob_glob.loe_failist(koik_failid[valik], marked_word)
print(sisu)
print(read)
print(tuhi_read)
print(minu_sõna)
nimi = "Analüüsi_Raportid"
glob_glob.loo_raporti_kataoog(nimi, sisu, read, tuhi_read, minu_sõna)
taht = input("Mis fail tahate leia? ")
fail = glob_glob.leia_failid_algustahega(taht)
print(fail)
otsitav_fail = input("Sisestaotsitava faili nimi (nt. minu_fail.txt): ")
tulemus = glob_glob.otsi_faili(otsitav_fail)
print(tulemus)
