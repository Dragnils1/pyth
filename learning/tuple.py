#!/usr/bin/env python

tuple = ('sad', 1, 2)
#tuple (кортеж) couldn2t be changed

print(len(tuple))
print(tuple[2])

#we should use "," if we want create tuple with one element length
tuple = ('hi',)   ## size-1 tuple

(x, y, z) = (42, 13, "hike")
print (z)  ## hike
(err_string, err_code) = 'kokose'  ## Foo() returns a length-2 tuple