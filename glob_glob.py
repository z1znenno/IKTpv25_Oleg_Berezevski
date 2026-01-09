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

def loo():
    pass