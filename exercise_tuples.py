# Parte 1 - Tuplas

def get_coordinate(registro):
    return registro[1]


def convert_coordinate(coordenada):
    return (coordenada[0], coordenada[1])


def create_record(registro_azara, registro_rui):
    coord_azara = get_coordinate(registro_azara)
    coord_convertida = convert_coordinate(coord_azara)
    coord_rui = registro_rui[1]
    if coord_convertida == coord_rui:
        return registro_azara + registro_rui
    else:
        return "not a match"


def sum_tuple(numeros):
    total = 0
    for n in numeros:
        total += n
    return total


def count_occurrences(tupla, elemento):
    count = 0
    for item in tupla:
        if item == elemento:
            count += 1
    return count


def find_index(tupla, elemento):
    for i in range(len(tupla)):
        if tupla[i] == elemento:
            return i
    return -1


def filter_positives(numeros):
    result = ()
    for n in numeros:
        if n > 0:
            result = result + (n,)
    return result
