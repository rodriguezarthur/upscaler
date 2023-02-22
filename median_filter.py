import cv2
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import sys

def voisin1(t, i, j):
    i += 1
    j += 1
    return [t[i+1][j], t[i+1][j-1], t[i][j-1], t[i-1][j-1], t[i-1][j], t[i-1][j+1], t[i][j+1], t[i+1][j+1], t[i][j]]


def voisin2(t, i, j):
    i += 2
    j += 2
    return [t[i+1][j], t[i+1][j-1], t[i][j-1], t[i-1][j-1], t[i-1][j], t[i-1][j+1], t[i][j+1], t[i+1][j+1], t[i][j], t[i-2][j], t[i-2][j+1],
            t[i-2][j+2], t[i-1][j+2], t[i][j+2], t[i+1][j+2], t[i+2][j +
                                                                     2], t[i+2][j+1], t[i+2][j], t[i+2][j-1], t[i+2][j-2], t[i+1][j-2],
            t[i][j-2], t[i-1][j-2], t[i-2][j-2], t[i-2][j-1]]
    
def tri_rapide(l):
    n = len(l)
    if n <= 1:
        return l
    else:
        l1, l2 = [], []
        for i in range(1, n):
            if l[i] > l[0]:
                l2.append(l[i])
            else:
                l1.append(l[i])
        return tri_rapide(l1)+[l[0]]+tri_rapide(l2)

def mediane(l):
    n = len(l)
    if n % 2 != 0:
        med = l[(n-1)//2]
    else:
        med = (l[(n//2)-1]+l[n//2])/2
    return med


def medianfilter(t):
    n = len(t)
    m = len(t[0])
    t = t.tolist()
    for i in range(n):
        t[i] = [[0,0,0],[0,0,0]] + t[i] + [[0,0,0],[0,0,0]]
    t = [[[0,0,0] for i in range(len(t[0])+4)]] + [[[0,0,0] for i in range(len(t[0])+4)]] + t + [[[0,0,0] for i in range(len(t[0])+4)]] + [[[0,0,0] for i in range(len(t[0])+4)]]
    
    m = [[[0,0,0] for i in range(m)] for j in range(n)]
    for i in range(len(m)):
        for j in range(len(m[0])):
            r, g, b = [], [], []
            v = voisin2(t,i,j)
            for pixel in v:
                r.append(pixel[2])
                g.append(pixel[1])
                b.append(pixel[0])
            m[i][j][0] = mediane(tri_rapide(r))
            m[i][j][1] = mediane(tri_rapide(g))
            m[i][j][2] = mediane(tri_rapide(b))
    return m