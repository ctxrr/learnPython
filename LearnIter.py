"""
	This module is a short course about iterate in python
"""
# 1:define a class with __iter__ method
class TestIter:
    def __iter__(self):
        yield 1
        yield 2
        yield 3

# 2:you will not get a generator after you creat a instance
a=TestIter()
print type(a) #its type is 'instance',not 'generator'!

# 3:but for...in can help you iterate automatic
for i in a:
	print i

# 4:we can use traditional way to generate a generator from a instance which class defined __iter__
b=iter(a)
print type(b) #now its type is 'generator',yeah!

# 5:of course you can iterate an generator
print b.next()
print b.next()
print b.next()

# 6:now let's see what happen in function with keyword 'yield'
def foo():
	yield 1
	yield 2
	yield 3

# 7:when you call the function,you will get a generator immediately!This is different from class
print type(foo)
print type(foo()) # you got a generator!

# 8:now we replace 'yield' with 'return' and call the function again
def fee():
	return 0

print type(fee)
print type(fee()) # you got a 'int',because fee() return 0

# 9:guess why print '1' 3 times?
print foo().next() # call foo first time.get generator No.1
print foo().next() # call foo second time.get generator No.2
print foo().next() # call foo third time.get generator No.3

# 10:this is the right way to use a generator 
c=foo() # call foo only once to get generator c
print c.next() # iterate c
print c.next() # iterate c
print c.next() # iterate c