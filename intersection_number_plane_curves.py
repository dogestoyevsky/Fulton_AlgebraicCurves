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

# for now, assuming f(0) = 0, can write in translation step later
inPolynomial1 = '3*x**2*y+x+y**4'
inPolynomial2 = '6*x*y+x+8*y**4'

x = Symbol('x')
y = Symbol('y')

f = poly(inPolynomial1,x,y)
g = poly(inPolynomial2,x,y)
#total_degree = F.total_degree()

sumOrder = 0

while f(0,0) == 0 & g(0,0) == 0:
    fPrime = poly(f(x,0),x)
    gPrime = poly(g(x,0),x)
    
    if degree(fPrime) > degree(gPrime):
        hold_fPrime = fPrime
        hold_f = f
        fPrime = gPrime
        f = g
        gPrime = hold_fPrime
        g = hold_f
      
    while degree(fPrime) > 0
        f = f/LC(fPrime)
        g = g/LC(gPrime)
        degDifference = degree(gPrime) - degree(fPrime)
        h = g - x**degDifference * f
        hPrime = poly(f(x,0),x)
        
    sumOrder += degree(gPrime)
    f = f/y
        

        
        
   