def put_order(value, lista):
    if len(lista) > 0:
        inserted = False
        for i, l in lista:
            if value < l:
                lista.insert(i, value)
                inserted = True
                break
        if not inserted:
            lista.append(value)
    else:
        lista.append(value)

    return lista;        


