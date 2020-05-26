#!/usr/bin/env python

from paillier.paillier import *
import time
from random import *


print "Generating keypair..."
priv, pub = generate_keypair(512)

pp = preprocess(pub)

t1 = time.time()

for i in range(100):
    x = randint(0,1000000)
    #print "x =randint(0,100)", x
    #print "Encrypting x..."
    cx = encrypt_efficient(pub, x, pp)

t2 = time.time()
print "Encryption time ", (t2-t1)/100

#print "cx =", cx
t1 = time.time()
for j in range(1):
    y = randint(0,100)
    #print "y =", y
    #print "Encrypting y..."
    cy = encrypt(pub, y)
    #print "cy =", cy
t2 = time.time()
print "Encryption time traditional ", (t2-t1)

print "Computing cx + cy..."
cz = e_add(pub, cx, cy)
print "cz =", cz

print "Decrypting cz..."
z = decrypt(priv, pub, cz)
print "z =", z

print "Computing decrypt((cz + 2) * 3) ..."
t1 = time.time()
print "result =", decrypt(priv, pub,
                          e_mul_const(pub, e_add_const(pub, cz, 2), 3))
t2 = time.time()
print "Decryption time ", t2-t1