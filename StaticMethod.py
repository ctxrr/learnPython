"""This module is about the usage of Static method in python

    You can get more help from:http://stackoverflow.com/questions/735975/static-methods-in-python
"""
class Foo():
    # use staticmethod as a decorator
    @staticmethod
    def thestaticmethod(x):
        print x
    # use staticmethod as a function if you have to support old versions of Python
    #thestaticmethod = staticmethod(thestaticmethod)

if __name__ == '__main__':
    Foo.thestaticmethod(2)

