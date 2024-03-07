def xor_cadenas(palabra, llave):
    
    if len (palabra) < len(llave):
        print("Las cadenas no son del mismo tamaño")
        return
    while len(llave) < len(palabra):
        llave += llave
    resultado = [format(int(a, 2) ^ int(b, 2), '08b') for a, b in zip(palabra, llave)]
    return resultado