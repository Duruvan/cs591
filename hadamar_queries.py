# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:11:37 2018

@author: durus
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def create_hadamard(n):
    """ Create and return a Hadamard matrix
        Paramaters:
            n - Size of the Hadamard matrix
    """
    
    return sp.linalg.hadamard(n)

def create_x(n):
    """ Create and return a column vector in {0,1}^n
        Parameters:
            n - number of rows
    """
    
    return np.random.randint(2, size=n).T

def create_noise(n, var):
    """ Create and return a random vector according to the Gaussian distribution
        Paramaters:
            n - number of rows
            var - variance of the distribution
    """
    
    return np.random.normal(0, var, size=n).T

def mechanism(x, H, Y, n):
    """ Mechanism to release the answer based on parameters 
        Parameters:
            x - data vector
            n - size of data vector
            H - Hadamard matrix of size nxn
            Y - Gaussian noise vector
    """

    return np.divide(np.matmul(H, x), n) + Y

def estimate(a, H):
    z = np.matmul(H, a)
    return np.round(z)

def main():
    n = [128, 512, 2048, 8192]
    std = [0.25, 0.125, 0.0625, 1/32]
    norms= [[0 for x in range(20)] for y in range(4)]
    averages = []
    
    for i in range(20):
        for j in range(len(n)):
            H = create_hadamard(n[1])
            x = create_x(n[1])
            Y = create_noise(n[1], std[j] ** 2)
            a = mechanism(x, H, Y, n[1])
            x_hat = estimate(a, H)
            norms[j][i] = np.linalg.norm(x_hat - x, ord=1)/n[1]
            
    for i in range(4):
        averages.append(sum(norms[i])/20)
        
    plt.scatter(std, averages)
    plt.xlabel("Standard deviation")
    plt.ylabel("Fraction of bits predicted incorrectly")
    
if __name__ == "__main__":
    main()