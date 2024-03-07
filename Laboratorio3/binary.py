def text_to_binary(texto):
    return ['{:08b}'.format(ord(c)) for c in texto]

def bin_to_text(binario):
    return ''.join(chr(int(b, 2)) for b in binario)