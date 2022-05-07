T = int(input())

for i in range(T):
    count = 0
    n = int(input())
    arrey = list(map(int, input().split(maxsplit = n)))
    def loop (arr):
        m = max(arr)
        for inx, elem in enumerate(arr):
            if (inx + 1 < len(arr)):
                sum = elem + arr[inx + 1]
                if((sum <= m) and (arr[-1] != 0)):
                    global count 
                    count += 1
                    arr[inx] = sum
                    arr.remove(arr[inx + 1])
                    loop(arr)
        else:
            if(len(arr) > 1):
                if((arr[-1] != arr [0]) and (arr[-1] != 0)):
                    count += 1
                    arr[0] = arr[0] + arr[1]
                    arr.remove(arr[1])
                    loop(arr)

    loop(arrey)
        
    print(count)