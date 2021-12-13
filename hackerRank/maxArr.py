b = input('length').split()
a = list(map(int, input('элементы массива').split()))

a.insert(0, a[a.index(max(a))])


#vark variant

a = sorted([x for x in range(-1, 10)], reverse=True)

print(a)