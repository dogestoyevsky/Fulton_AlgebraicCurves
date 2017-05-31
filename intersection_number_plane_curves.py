#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 11:51:49 2017

@author: hollymandel
"""

from sympy import *
import numpy as np
import math as math
from IPython import embed

# for now, assuming f(0,0) = 0, can write in translation step later
inPolynomial1 = input('Type polynomial 1:')
inPolynomial2 = input('Type polynomial 2:')

x = Symbol('x')
y = Symbol('y')

f = poly(inPolynomial1,x,y)
g = poly(inPolynomial2,x,y)
#total_degree = F.total_degree()

sumOrder = 0

while (f(0,0) == 0) & (g(0,0) == 0):
    fPrime = sympify(f)
    fPrime = fPrime.subs(y,0)
    fPrime = poly(fPrime,x)
    gPrime = sympify(g)
    gPrime = gPrime.subs(y,0)
    gPrime = poly(gPrime,x)
    
    if degree(fPrime) > degree(gPrime):
        hold_fPrime = fPrime
        hold_f = f
        fPrime = gPrime
        f = g
        gPrime = hold_fPrime
        g = hold_f
      
    while degree(fPrime) > 0:
        f = poly(f/LC(fPrime),x,y)
        g = poly(g/LC(gPrime),x,y)
        degDifference = degree(gPrime) - degree(fPrime)
        h = g - poly(x**degDifference,x,y) * f
        hPrime = sympify(h)
        hPrime = h.subs(y,0)
        hPrime = poly(hPrime,x)

        if degree(fPrime) > degree(hPrime):
            hold_fPrime = fPrime
            hold_f = f
            fPrime = hPrime
            f = h
            hPrime = hold_fPrime
            h = hold_f
        else:
            gPrime = hPrime
            g = h
        
    sumOrder += degree(gPrime)
    f = poly(simplify(f/y),x,y)

    
print('The intersection number of your polynomials at 0 is: \n', sumOrder)

        
        
   