# Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza, ile trzeba zapłacić. Zasady są takie:
#
# - nieletni (poniżej 18 roku życia) płacą 100 zł za noc
# - dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
# 	- 200 zł za noc, jeśli nocują jedną noc
# 	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
# 	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
# - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
#
# Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.

wiek = int(input("Podaj swój wiek: "))
ile_nocy = int(input("Podaj ile nocy spędzisz w hotelu: "))

if wiek <= 18:
    koszt_noclegu = 100 * ile_nocy

if 18 <= wiek < 65:
    if ile_nocy == 1:
        koszt_noclegu = 200
    elif 2 <= ile_nocy < 5:
        koszt_noclegu = 180 * ile_nocy
    elif ile_nocy >= 5:
        koszt_noclegu = 150 * ile_nocy

if wiek >= 65:
    if ile_nocy == 1:
        koszt_noclegu = 200 - (200*0.1)
    elif 2 <= ile_nocy < 5:
        koszt_noclegu = 180 * ile_nocy - (180 * ile_nocy * 0.1)
    elif ile_nocy >= 5:
        koszt_noclegu = 150 * ile_nocy - (150 * ile_nocy * 0.1)

print(f"Za nocleg zpałacisz {koszt_noclegu} zł.")


