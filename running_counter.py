# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 22:21:07 2018

@author: durus
"""

import numpy as np

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
    bits = 100

    accuracies = [-1] * 20
    for i in range(20):
        x, running_count, a = generate_data(bits)
        guesses = generate_guess(a, bits)
        accuracies[i] = count_correct(x, guesses, bits)
    
    average = (np.sum(accuracies))/(20*bits)
    print("Accuracy without w: " + str(average))

if __name__ == "__main__":
    main()