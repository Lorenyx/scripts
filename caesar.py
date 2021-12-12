#!/usr/bin/env python3
from argparse import ArgumentParser

def caeser_cipher(ciphertext: str, shift: int = 13):
    """Shifts the ciphertext by shift amount"""
    print(f'[=] Text shifted by {shift}:')
    for letter in ciphertext:
        BASE = 0 # Starting character for 
        if letter.isupper():
            BASE = ord('A') # ascii value of a

        elif letter.islower():
            BASE = ord('a') # ascii value of A
    
        print( chr( (ord(letter) + shift - BASE) % 26 + BASE ), end='' ) #chr((ord(val[i])-rot - 65) % 26 + 65)
    print()


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('ciphertext', type=str)
    parser.add_argument('--shift', '-s', type=int, default=13)

    args = parser.parse_args()
    #TODO add range of shift for bruteforcing
    if '..' in args.shift:
        s, f = args.shift.split('..')
        for i in range(s, f+1):
            caeser_cipher(args.ciphertext, i)
    else:
        caeser_cipher(args.ciphertext, args.shift)
