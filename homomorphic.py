from nose.tools import assert_raises
from phe import paillier
import sys

a = 5
b = 10

pub, priv = paillier.generate_paillier_keypair(n_length=128)

#ca, cb = paillier.PaillierPublicKey.encrypt(pub, a), paillier.PaillierPrivateKey.encrypt(pub, b)

ca = pub.encrypt(a)
cb = pub.encrypt(b)

print("A: ", a)
print("B: ", b)

print("Cipher A: ", ca)
print("Cipher B: ", cb)

cs = paillier.EncryptedNumber.__add__(ca, cb)
s = paillier.PaillierPrivateKey.decrypt(priv, cs)
print(cs)
print("Result (Add)", s)

cs = paillier.EncryptedNumber.__add__(ca, b)
s = paillier.PaillierPrivateKey.decrypt(priv, cs)
print("Result (Add)", s)

cs = paillier.EncryptedNumber.__mul__(ca, b)
s = paillier.PaillierPrivateKey.decrypt(priv, cs)
print("Result (Mul)", s)



