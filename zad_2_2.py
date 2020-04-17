# Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje
# w tylu liniach "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:
# ​
# ```
#     *
#   * * *
# * * * * *


from random import randint

x = randint (5,10)

print(f"\nChoinka będzie składać się z {x} linijek.")



for x in range(x+1):
    # print(x)

    i = ((x * 2) -1)

    tree = (i * "* ")

    print(f"{tree:^40}")




