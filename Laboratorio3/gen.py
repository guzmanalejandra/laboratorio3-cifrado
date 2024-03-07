import random
from cypher import *
from binary import *

def generar_keystream(longitud):
    keystream = ''
    for _ in range(longitud):
        keystream += chr(random.randint(0, 255))
    return keystream

def cifrar_mensaje(mensaje, keystream):
    mensaje_binario = text_to_binary(mensaje)
    keystream_binario = text_to_binary(keystream)
    return xor_cadenas(mensaje_binario, keystream_binario)


def descifrar_mensaje(mensaje_cifrado, keystream):
    keystream_binario = text_to_binary(keystream)  
    mensaje_descifrado_binario = xor_cadenas(mensaje_cifrado, keystream_binario)
    return bin_to_text(mensaje_descifrado_binario) 