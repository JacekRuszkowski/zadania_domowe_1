### Zadanie 1.8 | Kalkulator lat psich (ok. 0,5 godz.)

# Zakładamy, że 1 ludzki rok, to 5 lat psich.
#
# Za pomocą konsoli wczytaj imię i wiek psa.
#
# Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.
#
# Przykład:
# Podaj imię psa - Burek
# Podaj wiek psa - 3
#
# Gdyby Burek był człowiekiem, miałby 15 lat.

print()
print('Witaj w kalkulatorze psich lat.')
print()

imie = input("Podaj imię swojego pupila: ")
wiek_psa = float(input("Podaj wiek swojego psa: "))

wiek_ludzki = wiek_psa*5


print()

print(f"W przeliczeniu na ludzkie {imie} ma {wiek_ludzki} lat.")