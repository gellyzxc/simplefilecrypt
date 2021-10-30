import pyAesCrypt
import os
import sys
import random

print(f'made by gellyzxc | tg:gekksume')

ARRAY_SYMBOLS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'q', 'w', 'e', 'r', 't', 'y','u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'o', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'm',
    '!', '?'
]

# Получаем кол-во символов

count_symbols = 8

def rand_symbols():
    return ARRAY_SYMBOLS[
        random.randint(0, len(ARRAY_SYMBOLS) - 1)
    ]
passwordgen = ''
for i in range(0, count_symbols):
    passwordgen = passwordgen + f'{rand_symbols()}'

bufferSize = 1024 * 2048
enctype = '.gelly'
type1 = input('ENCRYPT (0) | DECRYPT (1)   ')
if type1 == '0':
    keytype = input('GENERATED KEY (0) | CUSTOM KEY (1)   ')
    if keytype == '0':
        password = passwordgen
    else:
        password = input(f'PASSWORD: ')
    file = input(f'FILE: ')
    fileout = file + enctype
    pyAesCrypt.encryptFile(file, fileout, password, bufferSize)
    print(passwordgen)
    os.remove(file)
if type1 == '1':
    file = input(f'FILE: ')
    password = input(f'PASSWORD: ')
    fileout = file.replace('.gelly', '')
    pyAesCrypt.decryptFile(file, fileout, password, bufferSize)


print(f'done.')

input()
