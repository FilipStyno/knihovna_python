import csv
import json


class KnihovniSystem:
    def __init__(self, nazev_souboru):
        self.soubor = nazev_souboru
        self.knihy = self.nacti_knihy()

    def nacti_knihy(self):
        try:
            with open(self.soubor, 'r', encoding='UTF-8') as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            print('Soubor nebyl nalezen')
        except Exception as e:
            print(f'Sry, nevim co se posralo: {e}')
        return []

    def zapis_do_json(self, nazev_json_souboru):
        try:
            with open(nazev_json_souboru, 'w', encoding='UTF-8') as json_file:
                json.dump(self.knihy, json_file, ensure_ascii=False, indent=4)
            print(f'Knihy byly úspěšně zapsány do {nazev_json_souboru}')
        except Exception as e:
            print(f'Chyba při zápisu do JSON souboru: {e}')


system = KnihovniSystem('knihy.csv')

system.zapis_do_json('vypis.json')

if system.knihy:
    print("První kniha v souboru:")
    print(system.knihy[0]['nazev_knihy'])
