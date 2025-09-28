
from util import converters, currency, password, bmi, loan
from util.password import PasswordOptions
from util.loan import LoanInput

def menu():
    print("=== Utiliidi komplekt ===")
    print("1) Ühikute konverter")
    print("2) Valuutakursi kalkulaator")
    print("3) Parooli generaator / juhuarv")
    print("4) KMI kalkulaator")
    print("5) Laenu kalkulaator (annuiteet)")
    print("0) Välju")
    return input("Vali [0-5]: ").strip()

def units_menu():
    print("""--- Ühikute konverter ---
Valikud:
  t - temperatuur (C, F, K)
  l - pikkus (mm, cm, m, km, in, ft, yd, mi)
  m - mass (mg, g, kg, t, oz, lb)
""")
    kind = input("Vali tüüp [t/l/m]: ").strip().lower()
    value = float(input("Väärtus: "))
    src = input("Lähteühik: ").strip()
    dst = input("Sihtühik: ").strip()
    if kind == "t":
        res = converters.convert_temperature(value, src, dst)
    elif kind == "l":
        res = converters.convert_length(value, src, dst)
    elif kind == "m":
        res = converters.convert_mass(value, src, dst)
    else:
        print("Tundmatu valik")
        return
    print(f"Tulemus: {res} {dst}")

def currency_menu():
    print("--- Valuutakursi kalkulaator ---")
    amount = float(input("Summa: "))
    src = input("Lähte valuuta (nt EUR): ").strip().upper()
    dst = input("Siht valuuta (nt USD): ").strip().upper()
    try:
        res = currency.convert(amount, src, dst)
        print(f"{amount} {src} = {res:.2f} {dst}")
    except Exception as e:
        print(f"Viga: {e} (kontrolli internetiühendust ja valuutakoode)")

def password_menu():
    print("""--- Parooli generaator / juhuarv ---
    """)
    mode = input("Vali [p]arool või [j]uhuarv: ").strip().lower()
    if mode == "j":
        a = int(input("Alamäär (kaasaarvatud): "))
        b = int(input("Ülamäär (kaasaarvatud): "))
        print(f"Juhuarv: {password.random_int(a, b)}")
        return
    length = int(input("Pikkus (nt 16): "))
    opts = PasswordOptions(
        length=length,
        uppercase=input("Suur tähed? (y/n) ").strip().lower() != "n",
        lowercase=input("Väiksed tähed? (y/n) ").strip().lower() != "n",
        digits=input("Numbrid? (y/n) ").strip().lower() != "n",
        symbols=input("Sümbolid? (y/n) ").strip().lower() != "n",
        avoid_ambiguous=input("Väldi segadusttekitavaid märke (O/0, l/1 jne)? (y/n) ").strip().lower() != "n",
    )
    print("Parool:", password.generate_password(opts))

def bmi_menu():
    print("--- KMI kalkulaator ---")
    w = float(input("Kaal (kg): "))
    h = float(input("Pikkus (cm): "))
    try:
        res = bmi.bmi_calc(w, h)
        print(f"KMI: {res.bmi} — {res.category}")
        print(f"Soovitus: {res.advice}")
    except Exception as e:
        print("Viga:", e)

def loan_menu():
    print("--- Laenu kalkulaator (annuiteet) ---")
    p = float(input("Laenu põhisumma (€): "))
    r = float(input("Aastane intressimäär (%): "))
    y = int(input("Aastad: "))
    res = loan.annuity(LoanInput(principal=p, annual_rate=r, years=y))
    print(f"Kuine makse: {res.monthly_payment} €")
    print(f"Intress kokku: {res.total_interest} €")
    print(f"Kokku tasutud: {res.total_paid} €")

def main():
    while True:
        choice = menu()
        if choice == "1":
            units_menu()
        elif choice == "2":
            currency_menu()
        elif choice == "3":
            password_menu()
        elif choice == "4":
            bmi_menu()
        elif choice == "5":
            loan_menu()
        elif choice == "0":
            print("Head aega!")
            break
        else:
            print("Tundmatu valik.")
        print()

if __name__ == "__main__":
    main()
