
# Utiliidi komplekt (CLI)

Kodune töö: väike utiliitide kogumik (CLI), mis sisaldab:
1. Ühikute konverter (temperatuur, pikkus, mass)
2. Valuutakursi kalkulaator (kasutab exchangerate.host API-t; internet vajalik)
3. Parooli generaator / juhuarvude tegija
4. KMI kalkulaator (kehamassiindeks) + soovitus
5. Laenu kalkulaator (annuiteet) — *“oma soovil programm”*

## Käivitamine

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python main.py
```

> NB! Valuutakalkulaatori jaoks on vajalik internetiühendus. Kasutatakse tasuta `https://api.exchangerate.host/latest` endpointi ja standardset `urllib` moodulit (lisadependentse pole).

## Projekti struktuur

```
utility-suite/
  main.py
  ui.py
  util/
    __init__.py
    converters.py   # ühikute teisendused
    currency.py     # valuutakursid (exchangerate.host)
    password.py     # parooli generaator + juhuarv
    bmi.py          # KMI
    loan.py         # annuiteetlaenu kalkulaator
  README.md
  requirements.txt
```

## Koodistiil ja põhimõtted
- **DRY**: korduv loogika keskendatud util-modulitesse (nt teisendused).
- **Selged nimed**: funktsioonid ja klassid kirjeldavad eesmärki.
- **Vead**: sisendi kontroll ja arusaadavad veateated CLI-s.
- **Laiendatavus**: uusi ühikuid/valikuid saab hõlpsalt lisada.
- **Testitavus**: tuumloogika on UI-st lahus (funktsioonid importitavad).

## GitHub
Laadi kogu kaust üles GitHubi. Soovi korral lisa `screenshots/` või `tests/` kaust.
```bash
git init
git add .
git commit -m "Utility suite: converter, currency, password/random, BMI, loan"
git branch -M main
git remote add origin <sinu-repo-url>
git push -u origin main
```
