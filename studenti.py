"""
Gestione di una lista di studenti
"""


import json


def aggiungi_studente(studenti, nome, cognome, eta, classe):
    """Aggiunge un nuovo studente alla lista"""
    # SCRIVI QUI IL TUO CODICE
    pass

def cerca_studente(studenti,nome):
    """Ricerca uno studente nella lista"""
    # SCRIVI QUI IL TUO CODICE
    pass

def stampa_studenti(studenti):
    """Stampa la lista degli studenti"""
    # SCRIVI QUI IL TUO CODICE
    pass

def rimuovi_studente(studenti, nome):
    """Rimuove uno studente dalla lista"""
    # SCRIVI QUI IL TUO CODICE
    pass

def main():
    """Funzione principale"""
    # Load studenti from JSON file studenti.json
    # Create the file if it not exists
    studenti = []
    try:
        with open("studenti.json",encoding="utf-8") as f_json:
            studenti = json.load(f_json)
    except FileNotFoundError:
        pass

    # Show an option menù
    while True:
        print()
        print("1. Aggiungi studente")
        print("2. Cerca studente")
        print("3. Rimuovi studente")
        print("4. Stampa studenti")
        print("5. Esci")
        scelta = input("Scelta: ")
        if scelta == "1":
            # SCRIVI QUI IL TUO CODICE
            pass
        elif scelta == "2":
            # SCRIVI QUI IL TUO CODICE
            pass
        elif scelta == "3":
            # SCRIVI QUI IL TUO CODICE
            pass
        elif scelta == "4":
            # SCRIVI QUI IL TUO CODICE
            pass
        elif scelta == "5":
            # SCRIVI QUI IL TUO CODICE
            pass
        else:
            # SCRIVI QUI IL TUO CODICE
            pass


if __name__ == "__main__":
    main()
