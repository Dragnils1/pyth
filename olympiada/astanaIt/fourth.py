x = input()

b = list(map(int, x))
v = 0

if(b[-1] == 0):
    for i in b[::-1]:
        if i == 0:
            v = v + 1
        else:
            break
    for i in range(v):
        b.insert(0, 0)
    x = ''.join(map(str, b))
    

a = "Yes" if x == x[::-1] else "No"

print(a)