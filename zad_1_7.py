# Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena. Wyświetl odpowiedni komunikat.
#
# Przykład:
# Co chcesz kupić? - ziemniaki
# Podaj cenę towaru - 5
# Podaj ilość towaru - 10
#
# Za ziemniaki, który chcesz kupić, zapłacisz 50 zł

print()
print("Witamy w internetowym warzywniaku.")

print()

towar = input("Podaj nazwę towaru: ")
cena = float(input(f"Wybrany towar - {towar}. Jaka jest cena za kilogram (PLN)? "))
ilosc = float(input(f"{towar} - cena za kg wynosi {cena:.2f} zł. Ile kilogramów chcesz kupić? "))

koszt = cena * ilosc

print()
print(f"Toje zamówienie:\n{towar} w ilości {ilosc} kg. Do zapłaty jest {koszt} zł.")