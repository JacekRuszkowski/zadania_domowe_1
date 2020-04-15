# Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
#
# Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.




print ("\nWitamy w programie \"e-szewc\".")

while True:

    # komunikacja z użytkownikiem i sprawdzanie czy podał właściwe dane

    dzien_input = input("\nW jaki dzień oddałeś buty do szewca?\nPodaj numer dnia tygodnia (poniedziałek - 1, wtorek - 2, środa - 3, czwartek - 4, piątek - 5, sobota - 6, niedziela - 7): ")

    if dzien_input.isdecimal():
        dzien = int(dzien_input)

        if dzien > 7:
            print("\nWprawdziłeś liczbę z innego zakresu niż wymagany (od 1 do 7). Spróbuj jeszcze raz.")
            continue

    else:
        print("\nWproadziłeś znak, który nie jest liczbą. Spóbuj jeszcze raz.")
        continue


    czas_naprawy_input = input("\nPodaj ile dni będzie trwała naprawa (maksymalnie 31 dni) : ")

    if czas_naprawy_input.isdecimal():
        czas_naprawy = int(czas_naprawy_input)

        if czas_naprawy > 31:
            print("\nWprawdziłeś liczbę z innego zakresu niż wymagany (od 1 do 31). Spróbuj jeszcze raz.")
            continue

    else:
        print("\nWproadziłeś znak, który nie jest liczbą. Spóbuj jeszcze raz.")
        continue

    # obliczenie kiedy buty będą gotowe

    if czas_naprawy + dzien <= 7:
        wynik = czas_naprawy + dzien

    elif czas_naprawy + dzien >= 7 and czas_naprawy + dzien <= 14:
        wynik = (czas_naprawy + dzien) - 7
    elif czas_naprawy + dzien >= 14 and czas_naprawy + dzien <= 21:
        wynik = (czas_naprawy + dzien) - 14
    elif czas_naprawy + dzien >= 21 and czas_naprawy + dzien <= 28:
        wynik = (czas_naprawy + dzien) - 21
    elif czas_naprawy + dzien >= 28 and czas_naprawy + dzien <= 35:
        wynik = (czas_naprawy + dzien) - 28
    elif czas_naprawy + dzien >= 35 and czas_naprawy + dzien <= 42:
        wynik = (czas_naprawy + dzien) - 35



    # wypisanie wyniku

    print()

    if wynik == 1:
        print("Buty będą do odbioru w poniedziałek.")
    elif wynik == 2:
        print("Buty będą do odbioru we wtorek.")
    elif wynik == 3:
        print("Buty będą do odbioru w środę.")
    elif wynik == 4:
        print("Buty będą do odbioru w czwartek.")
    elif wynik == 5:
        print("Buty będą do odbioru w piątek.")
    elif wynik == 6:
        print("Buty będą do odbioru w sobotę.")
    elif wynik == 7:
        print("Buty będą do odbioru w niedzielę")


    break




