#loop while
fib1 = 1
fib2 = 1
 
n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
 
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
 
print("Значение этого элемента:", fib2)


#loop for in
fib1 = fib2 = 1
 
n = int(input())
 
print(fib1, fib2, end=' ')
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

#recursia))
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(10))


#Последовательность Фибоначчи определяется так: φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.

n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)