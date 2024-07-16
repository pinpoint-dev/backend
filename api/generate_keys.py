import sys
import base64
import hashlib
import random
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def int_to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0' * (len(h) % 2) + h).zfill(length * 2).decode('hex')
    return s if endianess == 'big' else s[::-1]


def to_C_byte_array(adv_key, isV3):
    out = '{'
    for element in range(0, len(adv_key)):
        e = adv_key[element] if isV3 else ord(adv_key[element])
        out = out + "0x{:02x}".format(e)
        if element != len(adv_key) - 1:
            out = out + ','

    out = out + '}'
    return out


def sha256(data):
    digest = hashlib.new("sha256")
    digest.update(data)
    return digest.digest()

MAX_KEYS = 1

prefix = ''

i = 0
while i < 1:
    priv = random.getrandbits(224)
    adv = ec.derive_private_key(priv, ec.SECP224R1(
    ), default_backend()).public_key().public_numbers().x
    if isV3:
        priv_bytes = priv.to_bytes(28, 'big')
        adv_bytes = adv.to_bytes(28, 'big')
    else:
        priv_bytes = int_to_bytes(priv, 28)
        adv_bytes = int_to_bytes(adv, 28)

    priv_b64 = base64.b64encode(priv_bytes).decode("ascii")
    adv_b64 = base64.b64encode(adv_bytes).decode("ascii")
    s256_b64 = base64.b64encode(sha256(adv_bytes)).decode("ascii")

    if '/' in s256_b64[:7]:
        print(
            'Key skipped and regenerated, because there was a / in the b64 of the hashed pubkey :(')
        continue
    else:
        i += 1

    adv = base64.b64decode(adv_b64)