def suma1(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] + suma1(lista[1:])


def suma2(lista):
    if lista == []:
        return 0
    return lista[0] + suma2(lista[1:])


def suma3(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[-1] + suma3(lista[:-1])


def suma4(lista):
    if lista == []:
        return 0
    return lista[-1] + suma4(lista[:-1])


print(suma1([1, 2, 3]))
print(suma2([1, 2, 3]))
print(suma3([1, 2, 3]))
print(suma4([1, 2, 3]))
