def suma(lista):
    if lista == []:
        return 0
    return lista[0][0] + suma(lista[1:])

print suma([(3,"p"),(7,"t"),(5,"d")])


