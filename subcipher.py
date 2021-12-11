#!/usr/bin/env python3
from argparse import ArgumentParser

def subcipher(text: str, keys: dict):
    print("[=] Substituted text is:")
    for c in text:
        if c.isalpha():
            print( keys[c], end='' )
        else:
            print(c, end='')
    print()


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('text', type=str)
    parser.add_argument('--key-file', '-f', type=str, default=13)

    args = parser.parse_args()

    with open(args.key_file, 'r') as fp:
        _keys = {}

        for line in fp.readlines():
            k, v = line.split('=')
            _keys[k.strip()] = v.strip()

        subcipher(args.text, _keys)

    # GANG MAY KNOW YOUR IDENTITY ABORT ABORT MEET AT SAFE HOUSE B