if __name__ == '__main__':
    import sys
    sys.path.append('..')
    from animal.dog import *
else:
    from ..animal.dog import *
from boy import boy
def girl():
    print 'i am girl'
    boy()
    cat()
    dog()
girl()
