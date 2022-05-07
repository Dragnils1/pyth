n = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = 0

def loop(c):
    global d
    for inx, elem in enumerate(c):
        if(b[inx] != elem):
            b.insert(inx, elem)
            d += 1
            loop(c)

loop(c)
print(d)
