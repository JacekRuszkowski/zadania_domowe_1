# Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
#
# Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.




print ("Witamy w programie \"e-szewc\".")
print()

dzien = int(input("W jaki dzień oddałeś buty do szewca?\nPodaj numer dnia tygodnia (poniedziałek - 1, wtorek - 2, środa - 3, czwartek - 4, piątek - 5, sobota - 6, niedziela - 7): "))

print()

czas_naprawy = int(input("Podaj ile dni będzie trwała naprawa: "))

if czas_naprawy != 7:
    print("Podaj cyfrę z przedziału 1-7")

print()

if czas_naprawy + dzien <= 7:
    wynik = czas_naprawy + dzien

else:
    wynik = ((czas_naprawy + dzien) -7)

if wynik == 1:
    print("Buty będą do odbioru w poniedziałek.")
elif wynik== 2:
    print("Buty będą do odbioru we wtorek.")
elif wynik== 3:
    print("Buty będą do odbioru w środę.")
elif wynik == 4:
    print("Buty będą do odbioru w czwartek.")
elif wynik == 5:
    print("Buty będą do odbioru w piątek.")
elif wynik == 6:
    print("Buty będą do odbioru w sobotę.")
elif wynik == 7:
    print("Buty będą do odbioru w niedzielę")


