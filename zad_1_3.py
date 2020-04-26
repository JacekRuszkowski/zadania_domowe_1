# Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
# oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).

print()

masa = float(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w centymetrach: "))

bmi = masa/(wzrost/100)**2

print()

print(f"Twój wskaźnik BMI to {bmi:.2f}")

if bmi < 18.5:
    print("Masz niedowagę.\nTwój organizm potrzebuje więcej kalorii. Zadbaj o ich odpowiednią ilość.")
elif 18.5 <= bmi <= 24.9:
    print("Twoja waga jest prawidłowa.\nJesteś w dobrej formie. Kontunuuj zdrowe odżywianie")
elif 25 <= bmi <= 29.9:
    print("Masz nadwagę.\nDostarczasz organizmowi za dużo kalorii. Zadbaj o zdrową dietę oraz regularny wysiłek fizyczny.")
elif bmi > 30:
    print("Cierpisz na otyłość.\nSkontaktuj się z lekarzem lub dietetykiem gdyz Twoje życie może być zagrożone. Otyłośc jest przyczyną wielu poważnych chorób.")




