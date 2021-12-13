#!/usr/bin/env python

arr = [['i', 'am', 'first'], ['you', 'are', 'second']]


#1 variant

a = 3
mas = [0] * 3
for i in range(a):
    mas[i] = [1] * 3


#2 variant

a= 3 
mas = [[2] * a for i in range(a)]


#input

# a = int(input())

# mas = []

# for i in range(a):
#     mas.append(list(map(int, input().split())))


#output

for i in range(0, len(mas)):
    for i2 in range(0, len(mas[i])):
        print(mas[i][i2], end=' ') #вместо новой строки делаем разделитель как пробел
    print() # начало новой строки на каждый элемент основного массива
#other variant

for i in mas:
    for i2 in i:
        print(i2, end=' ')
    print()
#other variant with join

for i in mas:
    print(' '.join(list(map(str, i))))



print(mas)