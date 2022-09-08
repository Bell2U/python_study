import json, base64
from Crypto.Hash import SHA256

"""this file is to figure out how to store bytes into json string
"""

def store_bytes_in_str():
    bytes_data = SHA256.new(b'123sss').digest()[:10]
    sb = str(bytes_data)
    print(sb)
    print(type(sb))
# store_bytes_in_str()

def decode_any_bytes_via_ascii():
    """
    base64: This module provides functions for encoding binary data to printable ASCII 
    characters and decoding such encodings back to binary data.
    https://docs.python.org/3/library/base64.html
    """
    bytes_data = SHA256.new(b'123sss').digest()[:10]
    b64 = base64.b64encode(bytes_data)
    string_data = b64.decode("ascii")
    encode_b64 = string_data.encode("ascii")
    decoded_data = base64.b64decode(encode_b64)
    print(f"Original bytearray: {bytes_data} {type(bytes_data)}")
    print(f"Base64 bytearray: {b64} {type(b64)}")       # can be decoded by ascii, no more UnicodeDecodeError!!!!!
    print(f"String data: {string_data} {type(string_data)}")
    print(f"Encoded string data: {encode_b64} {type(encode_b64)}")
    print(f"Decoded bytearray: {decoded_data} {type(decoded_data)}")
# decode_any_bytes_via_ascii()
