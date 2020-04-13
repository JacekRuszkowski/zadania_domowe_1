# Założenia:
# 	- 0-6   - wiek przedszkolny - cena biletu: 0
# 	- 7-17  - wiek szkolny      - cena biletu: 2.28
# 	- 18-64 - wiek dorosły      - cena biletu: 3.80
# 	- +65   - wiek emerytalny   - cena biletu: 1.90
#
# Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
#
# Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.

print()
print("Witam w internetowym sklepie z biletami.")
print()

while True:

    wiek_input = (input("Podaj wiek: "))
    ile_biletow_input = (input("Podaj ilośc biletów: "))

    if wiek_input.isdecimal() and ile_biletow_input.isdecimal():

        wiek = float(wiek_input)
        ile_biletow = float(ile_biletow_input)


        if 0 <= wiek <= 6:
            cena_biletu = 0
        elif 7 <= wiek <= 17:
            cena_biletu = 2.28
        elif 18 <= wiek <= 64:
            cena_biletu = 3.80
        elif wiek >= 65:
            cena_biletu = 1.90

        do_zaplaty = ile_biletow * cena_biletu

        print()
        print(f"Koszt wszystkich biletów to {do_zaplaty:.2f} zł. \nDziękuję i zapaszam ponownie.")

        break

    else:
        print("Nie wprowadziłes poprawny danych. Poproszę o podanie liczb całkowitych.")

        continue


