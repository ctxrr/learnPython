if __name__ == '__main__':
    print 'absolute path'
    from cat import cat
else:
    print 'relative path'
    from .cat import cat
def dog():
    print 'wang wang wang'

dog()
cat()
