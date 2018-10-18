# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 22:21:07 2018

@author: durus
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_data(n):
    """ Generate initial data
        Parameters:
            n - size
    """
    
    x = np.random.randint(2, size = n)
    running_count = np.cumsum(x)    #This computes the array of prefix sums of x.
    z = np.random.randint(2, size = n)
    a = running_count + z
    return x, running_count, a

def generate_guess(a, bits):
    """ Generate guesses
        Parameters:
            a - noisy data
            bits - number of bits
    """
    data = a
    guesses = [-1] * bits
    count = 0
    
    for i in range(bits):
        a[i] = a[i] - count
        if a[i] < 0:
            a[i] += 1
            a[i - 1] = 0
            count = count - 1
            
        if data[i] == 0:
            guesses[i] = 0
        elif data[i] == 1:
            guesses[i] = 1
            count += 1 
        elif data[i] == 2:
            guesses[i] = 1
            count += 1
    return guesses

def count_correct(x, guesses, bits):
    """ Return the number of correct guesses
        Parameters:
            x - original bits
            guesses - vector of guesses
            bits - number of bits
    """
    
    correct = 0
    for i in range(bits):
        if x[i] == guesses[i]:
            correct += 1
    return correct

def generate_w(x, bits):
    """ Generate initial guess vector
        Parameters:
            x - initial data
    """
    w  = [-1] * bits
    
    for i in range(bits):
        rand = np.random.rand()
        if rand <= (2/3):
            w[i] = x[i]
        else:
            if x[i] == 0:
                w[i] = 1
            else:
                w[i] = 0
    
    return w

def main():
    n = [100, 500, 1000, 5000]
    accuracies = [[0 for x in range(20)] for y in range(4)]
    averages = []
    
    for i in range(20):
        for j in range(4):
            x, running_count, a = generate_data(n[j])
            guesses = generate_guess(a, n[j])
            accuracies[j][i] = count_correct(x, guesses, n[j])

    for i in range(4):
        averages.append(sum(accuracies[i])/(20 * n[i]))
    
    print(averages)
    plt.scatter(n, averages)
    plt.xlabel("Size of data")
    plt.ylabel("Average accuracy")

if __name__ == "__main__":
    main()