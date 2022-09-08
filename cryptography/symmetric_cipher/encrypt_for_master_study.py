from Crypto.Cipher import AES
from Crypto.Random import random, get_random_bytes
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import json, base64

"""
https://www.dlitz.net/software/pycrypto/api/current/
https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
https://stackoverflow.com/questions/1220751/how-to-choose-an-aes-encryption-mode-cbc-ecb-ctr-ocb-cfb
"""

def AES_ECB_mode():
    """a naive mode which have zero security, only been used for teaching
    """
    BLOCK_SIZE = 16     # bytes, any interger multiple of 16 is fine
    randombits = random.getrandbits(32)
    key = SHA256.new(str(randombits).encode('ascii')).digest()
    # print(len(key))

    msg = b'This is the secret message'
    padded_msg = pad(msg, BLOCK_SIZE)

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_message = cipher.encrypt(padded_msg)
    # decrypted_padded_msg = cipher.decrypt(encrypted_message)
    # decrypted_message = unpad(decrypted_padded_msg, BLOCK_SIZE)

    another_cipher = AES.new(key, AES.MODE_ECB)
    decrypted_padded_msg = another_cipher.decrypt(encrypted_message)
    decrypted_message = unpad(decrypted_padded_msg, BLOCK_SIZE)

    print(encrypted_message)
    print(decrypted_message)
# AES_ECB_mode()

def AES_OFB_mode():
    # https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ofb-mode
    
    # encryption
    data = b"secret"
    randombytes = get_random_bytes(16)
    key = SHA256.new(randombytes).digest()
    cipher = AES.new(key, AES.MODE_OFB)
    encrypted_bytes = cipher.encrypt(data)
    iv = cipher.iv
    print(f"Key: {key}")

    # pack the message
    msg = {
        'iv': base64.b64encode(iv).decode('ascii'),
        'encrypted_bytes': base64.b64encode(encrypted_bytes).decode('ascii')
    }
    msg_json = json.dumps(msg)
    print(f"Encryped message: {msg_json}")


    # decryption
    try:
        recv_msg = json.loads(msg_json)
        iv = base64.b64decode(recv_msg['iv'].encode('ascii'))
        cipher_text = base64.b64decode(recv_msg['encrypted_bytes'].encode('ascii'))

        Dcipher = AES.new(key, AES.MODE_OFB, iv=iv)
        plain_text = Dcipher.decrypt(cipher_text)
        print(f"Decrypted message: {plain_text}")
    except (ValueError, KeyError):
        print("Incorrect decryption")

AES_OFB_mode()
