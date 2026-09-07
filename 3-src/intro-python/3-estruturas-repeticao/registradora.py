codigo = int(input('Código do produto: '))
total = 0

while codigo != 0:
    if codigo != 1 and codigo != 2 and codigo != 3 and codigo != 5 and codigo != 9:
        print('Código inválido!')
    else:
        quantidade = int(input('Quantidade: '))
        if codigo == 1:
            preco = 0.5
        elif codigo == 2:
            preco = 1.0
        elif codigo == 3:
            preco = 4.0
        elif codigo == 5:
            preco = 7.0
        else:
            preco = 8.0
        total = total + (quantidade * preco)
    
    codigo = int(input('Código do produto: '))

print(f'Total: R$ {total:.2f}')