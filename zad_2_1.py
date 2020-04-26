# Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby
# i pyta jaka jest ich suma (nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
# Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.

from random import randint

liczba_1 = randint(0,100)
liczba_2 = randint(0,100)

print()

print("Witaj w progamie 'zagadka matematyczna'.\nProgram wylosuje dwie liczy, a Ty podaj ich sumę ")

print()

while True:

    wynik = int(input(f"Ile wynosi {liczba_1} + {liczba_2}? "))
    print()

    if wynik == liczba_1 + liczba_2:
        print("Brawo! To jest poprawna odpowiedź.")
        print()
        break

    else:
        print ("Spróbuj jeszcze raz.")
        continue