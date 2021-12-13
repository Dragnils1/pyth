a, b = map(int, input().split())

counter = 0

for i in range(1, a + 1):

   for j in range(1, a + 1):

       for k in range(1, a + 1):

           if i + j + k <= a and i * j * k <= b:

               counter += 1

print(counter)