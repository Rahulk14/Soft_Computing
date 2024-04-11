# -*- coding: utf-8 -*-
"""fuzzy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iUWAxeaNy13jhkbkEIfsHSz241Wz8z_m
"""

!pip install -U scikit-fuzzy

# Import necessary libraries
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Define input universe
x = np.arange(0, 11, 1)

# Define fuzzy sets
A = fuzz.trimf(x, [0, 2, 4])  # Fuzzy set A
B = fuzz.trimf(x, [3, 6, 9])  # Fuzzy set B

# Plot fuzzy sets
plt.figure()
plt.plot(x, A, 'b', linewidth=1.5, label='A')
plt.plot(x, B, 'r', linewidth=1.5, label='B')
plt.title('Fuzzy Sets')
plt.legend()
plt.show()

# Perform union operation
union = np.fmax(A, B)

# Perform intersection operation
intersection = np.fmin(A, B)

# Perform difference operation (A - B)
difference = np.fmax(A, np.fmin(B, 1 - A))

# Perform complement operation
complement_A = 1 - A
complement_B = 1 - B

# Plot union, intersection, difference, and complement
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, union, 'g', linewidth=1.5, label='Union')
plt.title('Union of Fuzzy Sets')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, intersection, 'm', linewidth=1.5, label='Intersection')
plt.title('Intersection of Fuzzy Sets')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, difference, 'y', linewidth=1.5, label='Difference (A - B)')
plt.title('Difference of Fuzzy Sets')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x, complement_A, 'c', linewidth=1.5, label='Complement of A')
plt.plot(x, complement_B, 'k', linewidth=1.5, label='Complement of B')
plt.title('Complement of Fuzzy Sets')
plt.legend()

plt.tight_layout()
plt.show()