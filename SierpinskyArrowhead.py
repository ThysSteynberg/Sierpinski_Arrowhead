# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:42:24 2020

@author: Thys
"""
import numpy as np
import matplotlib.pyplot as plt

class Triangle():
    """
    Triangle class: holds the three corners as private members, and data as a class variable.
    """
    data = np.array([[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]]])
    def __init__(self, left, right, top):
        self._left = left
        self._right = right
        self._top = top
    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right
    @property
    def top(self):
        return self._top
    
def triRecur(tri, num):
    """
    Creates three new triangles within the given triangle tri, then adds their vertices to Triagle.data
    """
    if(num>0):
        Triangle.data = np.append(Triangle.data, np.array([tri.left, tri.right, tri.top, tri.left]), axis=0)
        tri1 = Triangle(tri.left+(tri.top-tri.left)/2, tri.right+(tri.top-tri.right)/2, tri.top)
        tri2 = Triangle(tri.left, tri.left+(tri.right-tri.left)/2, tri.left+(tri.top-tri.left)/2)
        tri3 = Triangle(tri.left+(tri.right-tri.left)/2, tri.right, tri.right+(tri.top-tri.right)/2)
        triRecur(tri1, num-1)
        triRecur(tri2, num-1)
        triRecur(tri3, num-1)
        
def plot(data):
    """
    Plot the data given as: 
        data is the coordinates of each point. Every triangle has 4 coordinates.
    """
    counter = 0
    xc = np.array([])
    yc = np.array([])
    fig, ax = plt.subplots()  
    plt.figure(dpi=1000) 
    ax.set_aspect(1)
    for dataSection in data:
        counter+=1
        xc = np.append(xc, dataSection[0])
        yc = np.append(yc, dataSection[1])
        if(counter%4 == 0):
            plt.plot(xc, yc,color='red',linewidth = 0.1)
            xc = np.array([])
            yc = np.array([])
    plt.show()
    
"""
Initial call to recursive function.
"""  
tri = Triangle(np.array([[0],[0]]), np.array([[10],[0]]), np.array([[5],[10]]))
triRecur(tri, 10)
plot(Triangle.data)