# Parte 3 - Diccionarios

def create_inventory(items):
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def add_items(inventario, items):
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1
    return inventario


def decrement_items(inventario, items):
    for item in items:
        if item in inventario:
            if inventario[item] > 0:
                inventario[item] -= 1
    return inventario


def remove_item(inventario, item):
    if item in inventario:
        del inventario[item]
    return inventario


def list_inventory(inventario):
    result = []
    for item, cantidad in inventario.items():
        if cantidad > 0:
            result.append((item, cantidad))
    return result


def find_max_value(diccionario):
    if len(diccionario) == 0:
        return ""
    max_key = ""
    max_val = None
    for key, val in diccionario.items():
        if max_val is None or val > max_val:
            max_val = val
            max_key = key
    return max_key


def reverse_dict(diccionario):
    result = {}
    for key, val in diccionario.items():
        if val in result:
            result[val] = result[val] + key
        else:
            result[val] = key
    return result


def word_frequency(palabras):
    if palabras == "" or len(palabras) == 0:
        return {}
    freq = {}
    for word in palabras:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


def find_biggest_expense(gastos):
    if len(gastos) == 0:
        return ""
    max_cat = ""
    max_avg = None
    for cat, lista in gastos.items():
        total = 0
        for val in lista:
            total += val
        avg = total / len(lista)
        if max_avg is None or avg > max_avg:
            max_avg = avg
            max_cat = cat
    return max_cat


def sum_expenses(gastos):
    result = {}
    for cat, lista in gastos.items():
        total = 0
        for val in lista:
            total += val
        result[cat] = total
    return result


def sum_expenses_by_type(gastos):
    result = {}
    for cat, lista in gastos.items():
        for tipo, monto in lista:
            if tipo in result:
                result[tipo] += monto
            else:
                result[tipo] = monto
    return result
