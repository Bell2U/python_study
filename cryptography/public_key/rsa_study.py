from pk_number_theory import z_star
from random import choice

from Crypto.PublicKey import RSA   # https://www.dlitz.net/software/pycrypto/api/current/
from Crypto.Cipher import PKCS1_OAEP


def simple_example():
    # 1. generate two large prime, let n = pq
    p = 17
    q = 31
    n = p*q

    # 2. select some e coprime to theta_n_star
    phi_n = (p-1)*(q-1)
    theta_n_star, theta_theta_n = z_star(phi_n)
    e = choice(theta_n_star)
    # e = 7
    
    # 3. find d such that ed == 1 mod theta_n
    d = pow(e, theta_theta_n-1, phi_n)
    assert e*d % phi_n == 1

    public_key = (n, e)
    private_key = (n, d)

    # for simplistiy, all the messages chosen here are integer.
    # message must less than n !!!!
    msg = 2
    # msg = n-1
    # msg = n       # will fail
    # msg = n+1     # will fail too

    encrypted_msg = pow(msg, public_key[1], public_key[0])
    decrypted_msg = pow(encrypted_msg, private_key[1], private_key[0])
    # print(decrypted_msg, n)
    print(n, phi_n, encrypted_msg)
# simple_example()

def convert_integer_to_bytes_test():
    # undone
    a = 5
    b = 6
    a_b = bytes(a)
    b_b = bytes(b)
    c_b = a_b + b_b
    print(a_b, b_b, c_b, sep='\n')
    c = int.from_bytes(c_b, "little")
    assert c == 11, f"c == {c}"
# convert_integer_to_bytes_test()

def generate_RSA_key_object():
    # https://www.dlitz.net/software/pycrypto/api/current/

    """
    A wrong way of doing RSA encyption:

    key = RSA.generate(2048)   # key is a RSA object https://www.dlitz.net/software/pycrypto/api/current/, click Crypto.PublicKey.RSA
    msg = b"That's my message"
    encrypted_msg = key.encrypt(msg, k)   # Attention: this function performs the plain, primitive RSA encryption (textbook). In real applications, you always need to use proper cryptographic padding, and you should not directly encrypt data with this method. Failure to do so may lead to security vulnerabilities. It is recommended to use modules Crypto.Cipher.PKCS1_OAEP or Crypto.Cipher.PKCS1_v1_5 instead.

    the right way of implementing this: https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html
    """

    # generate a RSA key pair and save it to a file
    # refers to https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html#module-Crypto.PublicKey.RSA
    key = RSA.generate(2048)     # Rsakey object https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html#Crypto.PublicKey.RSA.RsaKey
    
    # define file path
    private_key_file = './public_key/private.pem'
    public_key_file = './public_key/public.pem'

    # store the private key into a file
    f = open(private_key_file, 'wb')
    f.write(key.export_key('PEM'))
    f.close()
    # store the public key into a file
    f = open(public_key_file, 'wb')
    f.write(key.public_key().export_key())   # default formate is "PEM"
    f.close()

    # read the private key back
    f = open(private_key_file, 'r')
    private_key = RSA.import_key(f.read())
    # read the public key back
    f = open(public_key_file, 'r')
    public_key = RSA.import_key(f.read())
    print(type(private_key), private_key, sep='\t')
    print(type(public_key), public_key, sep='\t')

    # Variables:
    [key.n, key.e, key.d, key.p, key.q, key.u]
    # n (integer) – RSA modulus
    # e (integer) – RSA public exponent
    # d (integer) – RSA private exponent
    # p (integer) – First factor of the RSA modulus
    # q (integer) – Second factor of the RSA modulus
    # u – Chinese remainder component (p−1mod q)
    
    # # keys.exportKey() for the private key, keys.publickey().exportKey() for the public key.  https://stackoverflow.com/questions/9197507/saving-rsa-keys-to-a-file-using-pycrypto
    # notice that:
    assert key.n == key.p * key.q
    
    theta_n = (key.p-1)*(key.q-1)
    # assert key.e*key.d % theta_n == 1   # sometimes it will raise a assertion error, sometimes it won't, strange
    # m, tn = z_star(key.n)
    # assert theta_n == tn
# generate_RSA_key_object()

def encryption_and_decryption_based_on_RSA_keys():
    # https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html

    # encrypt via public key
    message = b'You can attack now!'
    pub_key = RSA.import_key(open('public_key/public.pem').read())
    cipher = PKCS1_OAEP.new(pub_key)
    cipher_text = cipher.encrypt(message)

    # decrypt via private key
    priv_key = RSA.import_key(open('public_key/private.pem').read())
    cipher = PKCS1_OAEP.new(priv_key)
    decipher_text = cipher.decrypt(cipher_text)
    assert message == decipher_text, f"decipher text is {decipher_text}"
# encryption_and_decryption_based_on_RSA_keys()
