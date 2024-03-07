from PIL import Image
from Crypto.Cipher import AES
import os

key = os.urandom(16)

def pad(data):
    return data + b"\x00" * (16 - len(data) % 16)

def encrypt_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data))

def encrypt_cbc(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.encrypt(pad(data))


with Image.open('foto1.jpeg') as im:
    data = im.tobytes()

encrypted_ecb_data = encrypt_ecb(data, key)
encrypted_cbc_data = encrypt_cbc(data, key)

with Image.frombytes('RGB', im.size, encrypted_ecb_data) as im_ecb:
    im_ecb.save('imagen_ecb1.jpg')

with Image.frombytes('RGB', im.size, encrypted_cbc_data) as im_cbc:
    im_cbc.save('imagen_cbc1.jpg')


with Image.open('Logo-UVG.webp') as im:
    data1 = im.tobytes()
    
encrypted_ecb_data = encrypt_ecb(data1, key)
encrypted_cbc_data = encrypt_cbc(data1, key)


with Image.frombytes('RGB', im.size, encrypted_ecb_data) as im_ecb:
    im_ecb.save('imagen_ecb2.webp')

with Image.frombytes('RGB', im.size, encrypted_cbc_data) as im_cbc:
    im_cbc.save('imagen_cbc2.webp')


with Image.open('tux.ppm') as im:
    data1 = im.tobytes()
    
encrypted_ecb_data = encrypt_ecb(data1, key)
encrypted_cbc_data = encrypt_cbc(data1, key)


with Image.frombytes('RGB', im.size, encrypted_ecb_data) as im_ecb:
    im_ecb.save('imagen_ecb3.ppm')

with Image.frombytes('RGB', im.size, encrypted_cbc_data) as im_cbc:
    im_cbc.save('imagen_cbc3.ppm')

Image.open('imagen_ecb3.ppm').show()
Image.open('imagen_cbc3.ppm').show()