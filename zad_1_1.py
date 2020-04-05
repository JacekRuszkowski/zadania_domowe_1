

#//////////////   CZĘŚĆ 1   ///////////

# Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.


cena = float(input("Podaj cenę za kilogram ziemniaków: "))

koszt_ziemniakow = cena * 5

print(f"Za 5 kilko ziemniaków trzeba zapłacić {koszt_ziemniakow:.2f} zł.")

print()
print()


#//////////////   CZĘŚĆ 2   ///////////


# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.


cena_za_kilo = float(input("Podaj cene za kilogram ziemniaków: "))
ile_kilo = float(input("Ile kilo ziemniaków chcesz kupic?: "))

koszt = cena_za_kilo * ile_kilo

print(f"Kupujesz {ile_kilo:.1f} kg ziemniaków. Do zapłaty jest {koszt:.2f} zł")

print()
print()



#//////////////   CZĘŚĆ 3   ///////////


# Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić,
# ile kosztuje kilo bananów i ile kilo bananów chce kupić. Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
# I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.

cena_kilo_zimniakow = float(input("Podaj cene za kilogram ziemniaków: "))
ile_ziemniakow = float(input("Ile kilo ziemniaków chcesz kupic?: "))

cena_kilo_bananow = float(input("Podaj cene za kilogram bananow: "))
ile_bananow = float(input("Ile kilo bannow chcesz kupic?: "))

koszt_ziemniaki = cena_kilo_zimniakow * ile_ziemniakow
koszt_banany = cena_kilo_bananow * ile_bananow
koszt_calkowity = koszt_ziemniaki + koszt_banany

print()

print(f"Kupujesz {ile_ziemniakow:.1f} kg ziemniaków oraz {ile_bananow:.1f} kg bananów. Do zapłaty jest {koszt_calkowity:.2f} zł")

print()

if koszt_ziemniaki > koszt_banany:
    print ("Za ziemniaki zapłacisz więcej")
else:
    print ("Za ziemniaki zapłacisz więcej")


