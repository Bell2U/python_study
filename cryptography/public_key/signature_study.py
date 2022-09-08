# reference: https://pycryptodome.readthedocs.io/en/latest/src/signature/signature.html
# PKCS#1 v1.5 and PKCS#1 PSS (RSA), which one is better? https://crypto.stackexchange.com/questions/48407/should-i-be-using-pkcs1-v1-5-or-pss-for-rsa-signatures

from Crypto.Signature import pkcs1_15
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

import sys, os, pathlib, string, random


def PKCS_1_v1_5():
    # RSA key pairs:
    publickey = './public.pem'
    privatekey = './private.pem'
    
    # sign the message
    message = b'To be signed'
    key = RSA.import_key(open(privatekey).read())
    h = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(h)

    # verify the signature
    key = RSA.import_key(open(publickey).read())
    h = SHA256.new(message)
    verifier = pkcs1_15.new(key)
    try:
        verifier.verify(h, signature)
        print("The signature is valid.")
    except ValueError or TypeError:
        print("The signature is not valid.")
# PKCS_1_v1_5()

def PKCS_1_PSS():
    # RSA key pairs:
    publickey =  pathlib.Path().absolute().joinpath('cryptography/public_key/public.pem')
    privatekey = os.path.join(os.path.dirname(os.path.abspath(__file__)), "private.pem")

    # sign the message
    message = b'This is the FBI...\nContrl + Alt + Delete\nkill skynet\nrm -rf /skynet\n'
    key = RSA.import_key(open(privatekey).read())
    h = SHA256.new(message)
    signature = pss.new(key).sign(h)
    print(signature)

    # verify the signature
    key = RSA.import_key(open(publickey).read())
    h = SHA256.new(message)
    verifier = pss.new(key)
    try:
        verifier.verify(h, signature)
        # verifier.verify(SHA256.new('12345'), signature)
        print("The signature is authentic.")
    except (ValueError, TypeError):
        print("The signature is not authentic.")
PKCS_1_PSS()


def generate_random_string(alphabet=None, length=8, exact=False) -> str:
    if not alphabet:
        alphabet = string.ascii_letters + string.digits
    """
    The line below is called a list comprehension and is the same as:
    letters = []
    for i in range(length):
        # Select a random letter from the alphabet and add it to letters
        letters.append(random.choice(alphabet))
    # Join the letters together with no separator
    return ''.join(letters)
    """
    if not exact:
        length = random.randint(length-4 if length-4 > 0 else 1,length+4)
    return ''.join(random.choice(alphabet) for x in range(length))

def PKCS_1_PSS_signature_length():
    # https://www.cryptsoft.com/pkcs11doc/v230/group__SEC__11__1__17__PKCS____1__RSA__PSS__SIGNATURE__WITH__SHA__1____SHA__256____SHA__384__OR__SHA__512.html
    # https://crypto.stackexchange.com/questions/3505/what-is-the-length-of-an-rsa-signature
    # https://www.google.com/search?q=PSS+signature+length&sxsrf=ALeKk036-r4Em09soivjVQ1IQmR41PNihQ%3A1620613254031&ei=hpiYYMuvAeKP4-EP9Yim4AM&oq=PSS+signature+length&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEAUQHjoICAAQBxAFEB5QzYYcWO-iHGC_qBxoAHAAeACAAe0CiAGiDZIBAzMtNZgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwjLiszqhr7wAhXixzgGHXWECTwQ4dUDCA4&uact=5
    # RSA key pairs:
    publickey =  pathlib.Path().absolute().joinpath('cryptography/public_key/public.pem')
    privatekey = os.path.join(os.path.dirname(os.path.abspath(__file__)), "private.pem")

    # sign the message
    message = generate_random_string(length=100).encode('ascii')
    try:
        key = RSA.import_key(open(privatekey).read())
    except FileNotFoundError:
        print(f'FileNotFoundError!, current directory is {sys.path[0]}')
        return
    h = SHA256.new(message)
    signature = pss.new(key).sign(h)
    print(len(signature))   # 256
# PKCS_1_PSS_signature_length()
