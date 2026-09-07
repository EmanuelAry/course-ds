import sys

i = int(sys.argv[1])
a = float(sys.argv[2])
b = float(sys.argv[3])
c = float(sys.argv[4])

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

if a != menor and a != maior:
    meio = a
if b != menor and b != maior:
    meio = b
if c != menor and c != maior:
    meio = c


if i == 1:
    print(f"{menor}, {meio}, {maior}")
if i == 2:
    print(f"{maior}, {meio}, {menor}")
if i == 3:
    print(f"{maior}, {menor}, {meio}")


