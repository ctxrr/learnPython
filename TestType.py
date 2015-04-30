"""This module contain some test app about python types and their size"""
from types import *
from sys import getsizeof as gs
import sys
import decimal

def foo(item):
	"""To check what type the argument is"""
	if type(item) is IntType:
		print 'int'
	elif type(item) is ListType:
		print 'list'
	else:
		print type(item)

def type_size():
	"""Test different size of Python built-in types on different CPU
	   You can run it on windows x86 x64 MacOs Linux etc.
	"""
	d = {
		"int": 0,
		"float": 0.0,
		"dict": dict(),
		"set": set(),
		"tuple": tuple(),
		"list": list(),
		"str": "a",
		"unicode": u"a",
		"decimal": decimal.Decimal(0),
		"object": object(),
		"none":None
	}
	for k, v in sorted(d.iteritems()):
		print k, sys.getsizeof(v)

def size_of_list():
	a=[]
	for i in range(10):
		print "size of list when adding None into list:",gs(a)
		a.append(None)
	print ''

	b=[]
	for i in range(10):
		print "size of list when adding str into list:",gs(b)
		b.append('hello')
	print ''

	c=[]
	for i in range(10):
		print "size of list when adding interger into list:",gs(c)
		c.append(100)

"""Test app from here...
"""
if __name__ =="__main__" :
	"""Test foo"""
	print "Going to show fun foo's running result..."
	print "type of foo(1)'s argument:",
	a=foo(1)
	print "type of foo([1,2,3])'s argument:",
	foo([1,2,3])
	print "type of foo('a')'s argument:",
	foo('a')
	print 'type of the return of foo:',type(a)
	print '-----------------------------------------------'

	"""Test type_size"""
	print "Going to show fun type_size's running result..."
	type_size()
	print '-----------------------------------------------'
	
	"""Test size_of_list"""
	print "Going to show fun size_of_list's running result..."	
	size_of_list()
	print '-----------------------------------------------'