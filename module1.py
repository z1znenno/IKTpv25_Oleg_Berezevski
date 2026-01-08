def kirjuta_failisse(failinimi : str, loend : list):
    while True:
        reziim = input("Sisesta faili avamise reziim (w - kirjutamine, a - lisamine): ")
        if reziim not in ["w", "a"]:
            print("Vale reziim! Proovi uuesti.")
        else:
            break
    n = len(loend)
    # if n != 0:
    #     with open(failinimi + ".txt", reziim, encoding="utf-8") as f:
    #         for e in loend:
    #             f.write(e + "\n")
    for i in range(4):
        element = input("Sisesta rida, mis faili lisada: ")
        loend.append(f"{element}")
    with open(failinimi + ".txt", reziim, encoding="utf-8") as f:
        #f.writelines(loend)
        for rida in loend:
            f.write(rida + "\n")

def loe_failist(failinimi : str) -> list:
    """
    Loeb faili read ja tagastab need listina
    """
    loend = []
    with open(failinimi + ".txt", "r", encoding="utf-8") as f:
        for rida in f:
            loend.append(rida.strip())
    return loend
loend = ["Rida 1", "Rida 2"]
failinimi = input("Sisesta faili nimi (ilma laiendita): ")
kirjuta_failisse(failinimi, loend)
sisu = loe_failist(failinimi)
print("Faili sisu: ")
#1. Variant
print(sisu)
#2. Variant
for rida in sisu:
    print(rida)