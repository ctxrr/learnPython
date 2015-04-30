"""This module contain two function about the running time of range and xrange
   You can run this module to compare the speed
"""
from time import time

def test_range(x):
    """Calculate the time using range"""
    start=time()
    for i in range(x):
        pass
    end=time()
    print 'range time:',end-start

def test_xrange(x):
    """Calculate the time using xrange"""
    start=time()
    for i in xrange(x):
        pass
    end=time()
    print 'xrange time:',end-start

if __name__ =='__main__':
    n=100000000
    test_range(n)
    test_xrange(n)
