from bip32utils import BIP32Key
from bip32utils import BIP32_HARDEN
from bip32utils import Base58
import os, bip39

import codecs
import hashlib
import ecdsa
import base58


def read():
    # Read the BIP39 seed word list 
    # (english seed words here)
    with open('english.txt') as f:
        bip39_list = f.readlines()    
    bip39_list = [w.strip('\n') for w in bip39_list]

    # Read the "text of interest"
    # (where seed words are planned to be inspected)
    with open('text.txt') as f:
        text = f.readlines()    
    text = ''.join(text).replace('\n',' ').replace("“",'').replace("”",'').replace(",",'').replace('.','')

    # Filter the text words - remain only the words from BIP39 list
    seedWords = [w for w in text.split(' ') if w in bip39_list]

    print(seedWords)

read()



