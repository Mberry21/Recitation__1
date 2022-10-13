# Division of PEMaCS
# CSCI-121 Elements of Computer Programming II
# Recitation 1 - Encryption with a password
# ********************************************************

import string

alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}


def encrypt(message, password):
    encrypted_message = ''
    m = 0
    for i in message:
        if m == len(password):
            m = 0
        x = alphabet[(ordinal_value[i] + ordinal_value[password[m]]) % len(alphabet)]
        encrypted_message += x
        m+= 1

    return encrypted_message


def decrypt(message, password):
    decrypted_message = ''
    m = 0
    for i in message:
        if m == len(password):
            m = 0
        k = password[m % len(password)]
        x = alphabet[(ordinal_value[i]- ordinal_value[k]) % len(alphabet)]
        m +=1
        decrypted_message += x

    return decrypted_message

print(ordinal_value)
print(encrypt('Mercury','Password'))