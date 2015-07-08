class Instance:
	def __init__(self,e):
		self.element = e

	def add(self,e):
		self.element = Instance(e)

class Obj:
    def __init__(self):
        self.name = 'wayne'
        self.age = 27

    def reassign(self):
        self = 10
        print self
        print type(self)

    def rename(self):
        self.name = 'ctxrr'
        self.age = 20

    def showinfo(self):
        print 'name is:',self.name
        print 'age is:',self.age

if __name__ == '__main__':
    #-----------class Instance----------------------------------------------------------------
    print "Test for class Instance................................"
    a=Instance(None)
    a.add(1)
    print a.element
    print a
    print ''
    #-----------class Obj----------------------------------------------------------------
    print "Test for class Obj................................"
    a=Obj()
    a.showinfo()
    a.rename()
    a.showinfo()
    a.reassign()
    print type(a)
    a.showinfo()
