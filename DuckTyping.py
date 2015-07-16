class Duck:
    def quack(self):
        print "Quack, quack!"

    def fly(self):
        print "Flap, Flap!"

class Person:
    def quack(self):
        print "I'm Quackin'!"

    def fly(self):
        print "I'm Flyin'!"

def in_the_forest(mallard):
    mallard.quack()
    mallard.fly()

if __name__ == '__main__':
    in_the_forest(Duck())
    in_the_forest(Person())
