from pathlib import Path
import json
import time
import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence


#ukol 1-Načtení dat ze souboru
def read_data(file_name, klic):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    #ja
    with open(file_path, "r", encoding = "utf-8") as file:
        data = json.load(file)
        if klic not in data:
            return None
        return data[klic]
    #konec ukolu 1



#ukol 2-Sekvenční vyhledávání
def linear_search(sekvence, hledane_cislo):
    seznam_pozic = []
    pocet_vyskytu = 0
    for i in range(len(sekvence)):
        if sekvence[i] == hledane_cislo:
            seznam_pozic.append(i)
            pocet_vyskytu += 1
    return {"positions": seznam_pozic, "count": pocet_vyskytu}
#konec ukolu 2




#ukol 3-Binární vyhledávání
def binary_search(sekvence, hled_cislo):
    vlevo = 0
    vpravo = len(sekvence) - 1
    while vlevo <= vpravo:
        uprostred = (vlevo + vpravo) // 2
        if sekvence[uprostred] == hled_cislo:
            return uprostred
        elif sekvence[uprostred] < hled_cislo:
            vlevo = uprostred + 1
        else:
            vpravo = uprostred - 1
    return None
#konec ukolu 3



#ukol 4-Měření času běhu
def measure_time():
    delky = [100, 500, 1000, 5000, 10000]
    linearni = []
    binarni = []
    for delka in delky:
        nesez_data = unordered_sequence(delka)
        seraz_data = ordered_sequence(delka)
        moje_cislo = seraz_data[-1]
        soucet_linearni = 0
        soucet_binarni = 0

        for _ in range(50):
            zacatek = time.perf_counter()
            linear_search(nesez_data, moje_cislo)
            soucet_linearni += time.perf_counter() - zacatek
            zacatek = time.perf_counter()
            binary_search(seraz_data, moje_cislo)
            soucet_binarni += time.perf_counter() - zacatek

        linearni.append(soucet_linearni / 50)
        binarni.append(soucet_binarni / 50)

    #Vykreslim
    plt.plot(delky, linearni, label="Linear search")
    plt.plot(delky, binarni, label="Binary search")
    plt.xlabel("Velikost vstupu")
    plt.ylabel("Cas v sekundach")
    plt.title("Porovnani casu")
    plt.legend()
    plt.show()
#konec ukolu4



#ukol 5-Vyhledávání vzorů v DNA
def pattern_search(sekvence, hled_vzor):
    pozice = set()
    for i in range(len(sekvence)-len(hled_vzor)+1):
        shodujese = True
        # ukol 6
        for j in range(len(hled_vzor)):
            if sekvence[i +j] != hled_vzor[j]:
                shodujese = False
                break #zapomínám!!!!
        if shodujese:
            pozice.add(i)
    return pozice


def main():
    #pass
    #ukol1
    nacteni_dat = read_data("sequential.json", "unordered_numbers")
    print(nacteni_dat)
    #ukol2
    hled_cislo = 7 #zvolila jsem si
    sekv_vyhledani = linear_search(nacteni_dat, hled_cislo)
    print(sekv_vyhledani)
    #ukol3
    serazene = read_data("sequential.json", "ordered_numbers")
    print(serazene)
    cislo = 7
    index = binary_search(serazene,cislo)
    print(index)
    #ukol5
    dna = read_data("sequential.json", "dna_sequence")
    hled_vzor = "ATA"
    pozice = pattern_search(dna, hled_vzor)
    print(pozice)
    # ukol4 - spis musi byt na konci
    measure_time()


if __name__ == "__main__":
    main()
