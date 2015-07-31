"""
Arguments are passed by assignment. The rationale behind this is twofold:

    1.the parameter passed in is actually a reference to an object (but the reference is passed by value)
    2.some data types are mutable, but others aren't

So:(Very important!!!)

    1.If you pass a mutable object into a method, the method gets a reference to that same object
     and you can mutate it to your heart's delight, but if you rebind the reference in the method,
     the outer scope will know nothing about it, and after you're done, the outer reference will
     still point at the original object.

    2.If you pass an immutable object to a method, you still can't rebind the outer reference,
     and you can't even mutate the object.

To make it even more clear, let's have some examples.
"""

# A.List - a mutable typedef add_list1(p):

#   1.Let's try to modify the list that was passed to a method:
def try_to_change_list_contents(the_list):
    print 'got', the_list
    the_list.append('four') # You can also use other list method such as pop and so on
    print 'changed to', the_list

#   2.test the result
outer_list = ['one', 'two', 'three']
print 'before, outer_list =', outer_list
try_to_change_list_contents(outer_list)
print 'after, outer_list =', outer_list
print '------------------------------------------------------------'
print ''

#   3.Since the parameter passed in is a reference to outer_list, not a copy of it, we can use the
#     mutating list methods to change it and have the changes reflected in the outer scope.

#   --------------------------------------------------------------------------------------------------------------

#   4.Now let's see what happens when we try to change the reference that was passed in as a parameter:
def try_to_change_list_reference(the_list):
    print 'got', the_list
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print 'set to', the_list

#   5.test the result
outer_list = ['we', 'like', 'proper', 'English']
print 'before, outer_list =', outer_list
try_to_change_list_reference(outer_list)
print 'after, outer_list =', outer_list
print '------------------------------------------------------------'
print ''

#   6.Since the the_list parameter was passed by value, assigning a new list to it had no effect that
#     the code outside the method could see. The the_list was a copy of the outer_list reference,
#     and we had the_list point to a new list, but there was no way to change where outer_list pointed.

#   --------------------------------------------------------------------------------------------------------------

# B.String - an immutable type
#   It's immutable, so there's nothing we can do to change the contents of the string

#   1.Now, let's try to change the reference
def try_to_change_string_reference(the_string):
    print 'got', the_string
    the_string = 'In a kingdom by the sea'
    print 'set to', the_string

#   2.test the result
outer_string = 'It was many and many a year ago'
print 'before, outer_string =', outer_string
try_to_change_string_reference(outer_string)
print 'after, outer_string =', outer_string
print '------------------------------------------------------------'
print ''

