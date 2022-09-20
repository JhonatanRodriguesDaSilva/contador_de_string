def contador_letra (texto, letra):
    contador = 0
    for item in texto:
        if item == letra:
            contador += 1
    return contador

print(contador_letra('jhonatan', 'a'))