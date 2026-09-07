import sys


def perfeito(n):
    div = []
    for i in range(1, n):
        if (n % i == 0):
            div.append(i)

    if (sum(div) == n):
        print(f"{n} é perfeito")
    else:
        print(f"{n} não é perfeito")

    print(f"Divisores de {n}: {div}")

perfeito(int(sys.argv[1]))