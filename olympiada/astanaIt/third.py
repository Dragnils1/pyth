a = list(map(str, input().split()))

if ((a[0] == 'R' and a[1] == 'R') or (a[0] == 'S' and a[1] == 'P') or (a[1] == 'S' and a[0] == 'P')):
    print('R')
elif((a[0] == 'P' and a[1] == 'P') or (a[0] == 'S' and a[1] == 'R') or (a[1] == 'S' and a[0] == 'R')):
    print('P')
else:
    print('S')