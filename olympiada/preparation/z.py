n, k = map(int, input().split())
a = list(map(int, input().split()))
if k == 1:
    print(1, 1)
    quit()
ibest = 0
jbest = 1
count = [0] * k
count[a[ibest] - 1] += 1
sht = 0
while sht != (k - 1):
    if count[a[jbest] - 1] == 0:
        sht += 1
    count[a[jbest] - 1] += 1
    jbest += 1
jbest -= 1
min_len = jbest - ibest + 1
i = ibest
j = jbest
while j < n and i < n:
    if count[a[i] - 1] >= 2:
        i += 1
        count[a[i - 1] - 1] -= 1
        if j - i + 1 < min_len:
            min_len = j - i + 1
            jbest = j
            ibest = i
    else:
        j += 1
        if j >= n:
            break
        count[a[j] - 1] += 1
 
print(ibest + 1, jbest + 1)
