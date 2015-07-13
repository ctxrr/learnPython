"""
    This module show 4 different ways to iterate in python
"""
# There are four ways to build an iterative function:

# create a generator (uses the yield keyword)
# use a generator expression (genexp)
# create an iterator (defines __iter__ and __next__ (or next in Python 2.x))
# create a function that Python can iterate over on its own (defines __getitem__)

### 1.iterator protocol (this is the tradition way to iterate)
#   iterator protocol means they provide two methods __iter__() and  next(). 
#   The __iter__ returns the iterator object and is implicitly called at the start of loops. 
#   The next() method returns the next value and is implicitly called at each loop increment.  
#   next() raises a StopIteration exception when there are no more value to return, which is implicitly captured by looping constructs to stop iterating.

class uc_iter():
    def __init__(self, text):
        self.text = text
        self.index = 0
    def __iter__(self):
        return self
    def next(self):
        try:
            result = self.text[self.index].upper()
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

### 2.generator (it is the most popular way)
def uc_gen(text):
    for char in text:
        yield char.upper()

### 3.generator expression
def uc_genexp(text):
    return (char.upper() for char in text)

### 4.getitem method
class uc_getitem():
    def __init__(self, text):
        self.text = text
    def __getitem__(self, index):
        result = self.text[index].upper()
        return result

### test code
if __name__ == '__main__':   
    for iterator in uc_gen, uc_genexp, uc_iter, uc_getitem:
        for ch in iterator('abcde'):
            print ch,
        print
