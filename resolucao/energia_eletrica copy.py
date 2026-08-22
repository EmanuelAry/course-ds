import sys

kwH = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
intalcao = sys.argv[2] if len(sys.argv) > 2 else "";
if intalcao.upper() == "R":
    if kwH <= 500:
        valor = kwH * 0.40
    else:
        valor = kwH * 0.65
elif intalcao.upper() == "C":
    if kwH <= 1000:
        valor = kwH * 0.55
    else:
        valor = kwH * 0.60
elif intalcao.upper() == "I":
    if kwH <= 5000:
        valor = kwH * 0.55
    else:
        valor = kwH * 0.60
print(f"O valor a ser pago é: R$ {valor:.2f}");