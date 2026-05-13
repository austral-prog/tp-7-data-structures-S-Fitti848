# Parte 2 - Sets

ALCOHOLS = {
    "scotch", "whiskey", "vodka", "gin", "rum", "tequila",
    "brandy", "cognac", "mezcal", "bourbon", "beer", "wine",
    "champagne", "absinthe", "vermouth", "kahlua", "amaretto",
    "sake", "port", "sherry", "grappa", "cachaca",
}


def clean_ingredients(nombre_plato, ingredientes):
    return (nombre_plato, set(ingredientes))


def check_drinks(nombre_bebida, ingredientes):
    for ingrediente in ingredientes:
        if ingrediente in ALCOHOLS:
            return nombre_bebida + " Cocktail"
    return nombre_bebida + " Mocktail"


def unique_chars(texto):
    result = set()
    for c in texto:
        result.add(c)
    return result


def sum_set(numeros):
    total = 0
    for n in numeros:
        total += n
    return total


def common_elements(set_a, set_b):
    result = set()
    for elem in set_a:
        if elem in set_b:
            result.add(elem)
    return result
