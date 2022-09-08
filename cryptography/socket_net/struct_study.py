import struct
from Crypto.Hash import SHA256
# reference: https://docs.python.org/3/library/struct.html?highlight=struct#module-struct

def p_up():
    data = 2345676
    p = struct.pack('>I', data)
    print(p, type(p), sep='\n')
    up = struct.unpack('>I', p)
    print(up, type(up), sep='\n')
# p_up()

def byte_obj():
    st = b'1234'
    print(st, type(st), sep='\n')
# byte_obj()

def calcsize_():
    # reference: https://docs.python.org/3/library/struct.html?highlight=struct#format-characters
    print(struct.calcsize('15s'))
    print(struct.calcsize('H'))
    print(struct.calcsize('i'))
# calcsize_()

def multiple_data():
    data = 123.456
    bytes_data = SHA256.new(b'123sss').digest()[:10]
    byte_data2 = b'hellosss sss'
    p = struct.pack('d10ss', data, bytes_data, byte_data2)
    up = struct.unpack('d10ss', p)
    print(data, bytes_data, byte_data2, sep='\n')
    print(up)
# multiple_data()
