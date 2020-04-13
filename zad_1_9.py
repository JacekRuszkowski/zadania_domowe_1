### Zadanie 1.9 FizzBuzz

# Napisz program, który wyświetla liczby od 1 do 100.
# Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
# dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.

for x in range(1,101):
    # if x % 3 != 0 and x % 5 != 0 and x % 15 != 0:
    #     print(x)
    if x % 3 == 0 and x % 5 != 0 and x % 15 != 0:
        print(x, "Fizz")
    elif x % 5 == 0 and x % 15 != 0:
        print(x, "Buzz")
    elif x % 15 == 0:
        print(x, "FizzBuzz")

    else:
        print(x)



