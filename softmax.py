import numpy as np

def softmax(x):
    
    x = x - np.max(x, axis = 1)[ : ,None]
    sumvec = np.sum(np.exp(x), axis=1)
    y = np.exp(x)/sumvec[ : ,None]
    
    return y