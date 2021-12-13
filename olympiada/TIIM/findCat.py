n, m = list(input().split())
print(n, m)

arr = [[a for a in range(0, m)]] * n

arr.append(input())

if (arr):
   print(arr)
else:
    print("нет котиков")
