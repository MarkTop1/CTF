# -*- coding: utf-8 -*-
import random, base64
from hashlib import sha1

def crypt(data, key):
    """RC4 algorithm"""
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)

def tencode(data, key, encode=base64.b64encode, salt_length=16):
    """RC4 encryption with random salt and final encoding"""
    salt = ''
    for n in range(salt_length):
        salt += chr(random.randrange(256))
    data = salt + crypt(data, sha1(key + salt).digest())
    if encode:
        data = encode(data)
    return data

def tdecode(data, key, decode=base64.b64decode, salt_length=16):
    """RC4 decryption of encoded data"""
    if decode:
        data = decode(data)
    salt = data[:salt_length]
    return crypt(data[salt_length:], sha1(key + salt).digest())


if __name__=='__main__':
    # 需要加密的数据
    data = '0xBE,0x8D,0xF5,0x67,0x02,0xC6,0x88,0x7B,0x7C,0xA0,0x99,0x74,0xF2,0xBD,0xF7,0xD0,0x5E,0x3A,0x38,0x5B,0xF4,0xE1,0x92,0x53,0x44,0x8E,0xFE,0x7E,0xA8,0x2D,0xF1,0x1B,0x02,0x95,0x6D,0x66,0xA6,0x8D,0xD5,0x92'
    # 密钥
    key = 'areyouctfer'

    # 加码
    encoded_data = tencode(data=data, key=key)
    print(encoded_data)
    # 解码
    decoded_data = tdecode(data=encoded_data, key=key)
    print(decoded_data)
