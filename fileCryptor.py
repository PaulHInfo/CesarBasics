#!/usr/bin/env python3
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def encrypt_file(input_file: str, output_file: str, key: bytes):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    with open(input_file, 'rb') as f_in:
        plaintext = f_in.read()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    with open(output_file, 'wb') as f_out:
        f_out.write(iv)
        f_out.write(ciphertext)
    #Que faire avec la clé ?


#def decrypt_file():
    #TODO

def main():
    #Chemin à revoir -> cd/../../..
    input_file = input("Entrez le chemin du fichier à chiffrer : ")
    output_file = input("Entrez le nom/chemin du fichier de sortie (ex: fichier.bin) : ")
    key = os.urandom(32)
    encrypt_file(input_file, output_file, key)
    print(f"Le fichier '{input_file}' a été chiffré et sauvegardé sous '{output_file}'.")

if __name__ == "__main__":
    main()
