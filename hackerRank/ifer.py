#!/bin/python3

n = int(input("введите число:").strip())

if ((n <= 5 and n >= 2) or (n >= 20)):
    print("Not Weird")
elif((n % 2 != 0) or (n % 2 == 0 and n >= 6 and n <= 20)):
    print('Weird')

   