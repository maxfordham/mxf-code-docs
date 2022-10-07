# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Numpy

import numpy as np

# ## vectorisation

# +
import functools as ft
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

def f(x, y=1):
    # return x ** y
    return x ** y

vf = np.vectorize(f)
vf(a, y=2)
# -

# ### array methods
#
#

# +
import numpy as np
import functools as ft
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

def f(x, y):
    return x * y

y = np.array([2, 2, 2, 2])
y = 2
vf = np.vectorize(f)
vf(a, y=y)

#a * y
# -

# ### Working with 3 dimensional arrays

# Mulitplying a and b together (f function) will return the same shape array.
#

# +
a = np.ones([1, 2, 2])
b = np.ones([1, 2, 2]) 
c = np.ones([2, 1, 1])

out = f(a, b)
print(f"Multiping arrays a and b gives the same shape: {out.shape}")
print(out)

out = f(a, c)
print(f"Multiping arrays a and c gives: {out.shape}")
print(out)
# -

a.shape



