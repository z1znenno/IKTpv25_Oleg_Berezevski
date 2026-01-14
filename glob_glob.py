import os
import glob

def leia_projeektifailid(laiend : str) -> list:
    if not laiend.startswith("."):
        laiend = "." + laiend
    failid = glob.glob("*" + laiend)
    for e in failid:
        print(e)
    return failid

def loe_failist(failinimi : str, mark : str) -> list:
    """
    Loeb faili read ja tagastab need listina
    """
    kokku_rida = 0
    tuhi_rida = 0
    marked_words = 0
    loend = []
    with open(failinimi, "r") as f:
        for rida in f:
            loend.append(rida.strip())
            kokku_rida += 1
            if rida in ["", " ", "\n"]:
                tuhi_rida += 1
        marked_words = loend.count(mark)
    return loend, kokku_rida, tuhi_rida, marked_words

def loo_raporti_kataoog(nimi, mis_sisse, read, tuhi_read, minu_sõnu):
    if not os.path.exists(nimi):
        print("Loome uus kataloog...")
        os.mkdir(nimi)
        print("Uus kataloog on loodud")
    os.chdir(nimi)
    loend = []
    loend.append(str(mis_sisse))
    loend.append(str(read))
    loend.append(str(tuhi_read))
    loend.append(str(minu_sõnu))
    with open("Analüüs", "w") as f:
        for rida in loend:
            f.write(rida + "\n")
    print("Sinu analüüs asub kataloogis: Analüüsi_Raportid")

def leia_failid_algustahega(taht : str):
    return glob.glob(f"{taht}*.*")

def otsi_faili(faili_nimi, otsingu_tee="."):
    for juur, kaustad, failid in os.walk(otsingu_tee):
        if faili_nimi in failid:
            return os.path.join(juur, failinimi)
    return "Faili ei leitud"