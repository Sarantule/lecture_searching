from pathlib import Path
import json

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
    vpravo = len(sekvence)-1
    while vlevo <= vpravo:
        uprostred = (vlevo + vpravo) //2
        if sekvence[uprostred] == hled_cislo:
            return uprostred
        elif sekvence[uprostred] < hled_cislo:
            vlevo = uprostred + 1
        else:
            vpravo - uprostred-1
    return None




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
    cislo = 5
    index = binary_search(serazene,cislo)
    print(index)



if __name__ == "__main__":
    main()
