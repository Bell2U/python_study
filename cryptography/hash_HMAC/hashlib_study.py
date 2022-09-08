import hashlib
from Crypto.Hash import SHA256

def hashlib_implement():
    hash_object = hashlib.sha256(b'Hello World')
    hex_dig = hash_object.hexdigest()
    print(hex_dig)

    print(hashlib.algorithms_available)
    print(hashlib.algorithms_guaranteed)
hashlib_implement()
