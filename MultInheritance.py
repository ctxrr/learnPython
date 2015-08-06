class A:
    def funa(self):
        print 'this is class a'
class B:
    def funb(self):
        print 'this is class b'
    def funa(self):
        print 'this is class bb'

class C1(B,A):
    def func(self):
        print 'this is class c'

class C2(A,B):
    def func(self):
        print 'this is class c'

if __name__ == '__main__':
    c = C1()
    c.funa()
    c.funb()
    c.func()
    print ''

    c = C2()
    c.funa()
    c.funb()
    c.func()
