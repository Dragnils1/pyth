arr = ['i am str', '20', 10, 20**1]
arr2 = ['allibaba tvar', 1]
a = 'all is ok'
#brute force list
for i in arr:
    print(i + i)

#find elem in list
if '20' in arr:
    print('i am find 20')

#diaposon of numbers
for i in range(1, 10):
    print(i)

#using condition with while
i = 0
while i < len(arr):
    print (arr[i])
    i = i + 3

arr.append(a)
arr.insert(0, a)
arr.extend(arr2)
arr.index(a)
arr.remove(a)
arr.pop(0)

#print from ... to ...
print (arr[1:3])

#delete and append on range
ab = ['delete and append']
arr[1:2] = ab

for i in arr:
    if(isinstance(i, int)):
        arr.remove(i)

sorted(arr, key=len)

print(arr)



#create new list, 3 examples:

nums = [1, 2, 3, 4]

squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]


strs = ['hello', 'and', 'goodbye']

shouting = [ s.upper() + '!!!' for s in strs ]
## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']


## Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]  ## [2, 1]

## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
## ['APPLE', 'BANANA']