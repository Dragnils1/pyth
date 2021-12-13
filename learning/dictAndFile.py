#!/usr/bin/env python

dict = {}

dict[0] = 'one'
dict['sec'] = 'secund'
dict['a'] = ['sad', 1]

for key in dict:
    print(key)

for key in dict.values(): print(key)

dict.keys()
dict.values()

print (dict.items())

for k, v in dict.items(): print (k, '>', v)

hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string

print(s)


var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print (list)      ## ['b']

dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print (dict)      ## {'a':1, 'c':3}