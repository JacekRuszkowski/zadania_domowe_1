# Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?),
# a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
#
# Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
#
# Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:
#
# ```
# import math
#
# x = math.sqrt(10)
# ```

# P=p(p−a)(p−b)(p−c)

import math


while True:

    pierwszy = (input("Podaj pierwszy bok trójkąta: "))
    drugi = (input("Podaj drugi bok trójkąta: "))
    trzeci = (input("Podaj trzeci bok trójkąta: "))



    if pierwszy.isdecimal() and drugi.isdecimal() and trzeci.isdecimal():
        a = float(pierwszy)
        b = float(drugi)
        c = float(trzeci)

        if a + b > c and b + c > a and c + a > b:
            p = (a + b + c) / 2
            pole_trojkata = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"Pole trójkąta o podanych bokach wynosi {pole_trojkata:.2f}")
            break
        else:
            print(f"Z podanych boków nie da się utworzyć trójkąta. Podaj inne liczby.")
            continue
    else:
        print ("Jeden z podanych boków nie jest liczbą. Spróbuj jeszcze raz.")


