kwH = float(input("Digite a quantidade de kWh consumidos: "));
intalcao = input("Informe o tipo de Intalação R - Residencial, C - Comercial ou I - Industrial: ");
if intalcao == "R":
    if kwH <= 500:
        valor = kwH * 0.40
    else:
        valor = kwH * 0.65
elif intalcao == "C":
    if kwH <= 1000:
        valor = kwH * 0.55
    else:
        valor = kwH * 0.60
elif intalcao == "I":
    if kwH <= 5000:
        valor = kwH * 0.55
    else:
        valor = kwH * 0.60
print(f"O valor a ser pago é: R$ {valor:.2f}");