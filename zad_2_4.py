### Zadanie 2.4 | Zgadnij liczbę z zakresu
# ​
# Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
# Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
# Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
# ​
# Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją i pełni w informatyce bardzo ważną rolę.
# Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024).
# Collapse


from random import randint

liczba = randint(0,1000)


liczba_user = None
proby = 0

while liczba_user != liczba:

    liczba_user = int(input("\nZgadnij jaką wylosowałem liczbę: "))

    if liczba_user > liczba:
        print ("Twoja liczba jest za duża. Próbuj dalej.")

    elif liczba_user < liczba:
        print ("Twoja liczba jest za mała. Próbuj dalej.")

    else:
        print("\nBrawo! To jest  ta liczba!")

    proby += 1

print (f"Liczba prób: {proby}")

