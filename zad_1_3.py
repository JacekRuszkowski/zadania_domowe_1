# Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
# oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).

print()

masa = float(input("Podaj swoją wagę: "))
wzrost = float(input("Podaj swój wzrost: "))

BMI = masa/(wzrost/100)**2

print()

print(f"Twój wskaźnik BMI to {BMI:.2f}")

if BMI < 18.5:
    print("Masz niedowagę.\nTwój organizm potrzebuje więcej kalorii. Zadbaj o ich odpowiednią ilość.")
elif 18.5 <= BMI <= 24.9:
    print("Twoja waga jest prawidłowa.\nJesteś w dobrej formie. Kontunuuj zdrowe odżywianie")
elif 25 <= BMI <= 29.9:
    print("Masz nadwagę.\nDostarczasz organizmowi za dużo kalorii. Zadbaj o zdrową dietę oraz regularny wysiłek fizyczny.")
elif BMI > 30:
    print("Cierpisz na otyłość.\nSkontaktuj się z lekarzem lub dietetykiem gdyz Twoje życie może być zagrożone. Otyłośc jest przyczyną wielu poważnych chorób.")

# print(0 <= liczba <= 10)


# BMI < 18,5	niedowaga
# 18,5 ≤ BMI ≤ 24,9	waga prawidłowa
# 25 ≤ BMI ≤ 29,9	nadwaga
# BMI > 30 otyłość


