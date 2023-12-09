import itertools

# Define the word lists
word_list_1 = [
    "abandon", "able", "account", "across", "admit", "adult", "aerobic", "also"
]

word_list_2 = [
    "about", "ancient", "around", "assume", "border", "build", "camera", "cash"
]

word_list_3 = [
    "again", "body", "book", "civil", "during", "father", "home", "letter",
    "message", "method", "mother", "net", "network", "over", "own", "person",
    "private", "risk", "trust", "under", "worth"
]

word_list_4 = [
    "access", "among", "any", "between", "country", "exchange", "hidden", "list",
    "number", "often", "when"
]

word_list_5 = ["art", "make", "text", "way", "where"]

word_list_6 = ["they", "time"]

word_list_7 = ["this", "wealth"]

word_list_8 = ["into", "used", "you"]

word_list_9 = ["have", "people", "story"]

word_list_10 = ["can", "gold"]

word_list_11 = ["that"]

word_list_12 = ["seed"]

# Combine the word lists to create a list of 24 words
word_lists = [
    word_list_1, word_list_2, word_list_3, word_list_4, word_list_5, word_list_6,
    word_list_7, word_list_8, word_list_9, word_list_10, word_list_11, word_list_12
]

mnemonics = list(itertools.product(*word_lists))

# Import BIP32 library
from mnemonic import Mnemonic
import bip32utils

mnemon = Mnemonic('english')
interesting_address = '1K4ezpLybootYF23TM4a8Y4NyP7auysnRo'

# Generate BIP32 master node from each mnemonic phrase
total_iterations = len(mnemonics)
progress_step = total_iterations // 100  # Update progress every 1%

for i, mnemonic in enumerate(mnemonics):
    mnemonic_string = " ".join(mnemonic)
    seed = mnemon.to_seed(mnemonic_string)
    
    root_key = bip32utils.BIP32Key.fromEntropy(seed)
    root_address = root_key.Address()
    # print(root_address)
    if interesting_address == root_address:
        root_public_hex = root_key.PublicKey().hex()
        root_private_wif = root_key.WalletImportFormat()
        print('Root key:')
        print(f'\tAddress: {root_address}')
        print(f'\tPublic : {root_public_hex}')
        print(f'\tPrivate: {root_private_wif}\n')

    child_key = root_key.ChildKey(0).ChildKey(0)
    child_address = child_key.Address()
    if interesting_address == child_address:
        child_public_hex = child_key.PublicKey().hex()
        child_private_wif = child_key.WalletImportFormat()
        print('Child key m/0/0:')
        print(f'\tAddress: {child_address}')
        print(f'\tPublic : {child_public_hex}')
        print(f'\tPrivate: {child_private_wif}\n')

    if i % progress_step == 0:
        progress = (i / total_iterations) * 100
        print(f"Progress: {progress:.2f}%")