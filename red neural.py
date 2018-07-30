import numpy as np
import random

def nonlin(x,deriv=False):
        if(deriv==True):
            return x*(1-x)
        return 1/(1+np.exp(-x))

np.random.seed(random.seed())

#compuerta xor 
xor = np.array( [[0, 0, 1],
                 [0, 1, -1],
                 [1, 0, 0],
                 [1, 1, 1] ])

xorOut = np.array([[0, 1, 1, 0]]).T

xorsyn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(1000):
        
        xorl0 = xor
        xorl1 = nonlin(np.dot(xorl0, xorsyn0))

        xorl1_error = xorOut - xorl1

        xorl1_delta = xorl1_error * nonlin(xorl1, True)

        xorsyn0 += np.dot(xorl0.T, xorl1_delta)

xorl1 = np.around(xorl1, 1)

#compuerta nand
nand = np.array( [[0, 0, 1],
                 [0, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1] ])

nandOut = np.array([[1, 1, 1, 0]]).T

nandsyn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(1000):
        
        nandl0 = nand
        nandl1 = nonlin(np.dot(nandl0, nandsyn0))

        nandl1_error = nandOut - nandl1

        nandl1_delta = nandl1_error * nonlin(nandl1, True)

        nandsyn0 += np.dot(nandl0.T, nandl1_delta)

nandl1 = np.round(nandl1, 0)

#compuerta not
no = np.array( [[0, 1],
                 [1, 1]])

noOut = np.array([[1, 0]]).T

nosyn0 = 2*np.random.random((2,1)) - 1

for iter in xrange(1000):
        
        nol0 = no
        nol1 = nonlin(np.dot(nol0, nosyn0))

        nol1_error = noOut - nol1

        nol1_delta = nol1_error * nonlin(nol1, True)

        nosyn0 += np.dot(nol0.T, nol1_delta)

nol1 = np.round(nol1, 0)

#compuerta or
o = np.array( [[0, 0, 1],
                 [0, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1] ])

oOut = np.array([[0, 1, 1, 1]]).T

osyn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(1000):
        
        ol0 = o
        ol1 = nonlin(np.dot(ol0, osyn0))

        ol1_error = oOut - ol1

        ol1_delta = ol1_error * nonlin(ol1, True)

        osyn0 += np.dot(ol0.T, ol1_delta)

ol1 = np.round(ol1, 0)

#compuerta and
sand = np.array( [[0, 0, 1],
                 [0, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1] ])

sandOut = np.array([[0, 0, 0, 1]]).T

sandsyn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(1000):
        
        sandl0 = sand
        sandl1 = nonlin(np.dot(sandl0, sandsyn0))

        sandl1_error = sandOut - sandl1

        sandl1_delta = sandl1_error * nonlin(sandl1, True)

        sandsyn0 += np.dot(sandl0.T, sandl1_delta)

sandl1 = np.round(sandl1, 0)

x = input("X: ")
y = input("Y: ")
z = input("Z: ")
w = input("W: ")
u = input("U: ")
v = input("V: ")

xorinput = np.array([x, y, 1])
xoroutput = nonlin(xorinput, 2)
print xoroutput

