N, K = map(int, input('Кол-во деревьев и цветов: ').split())
a = list(map(int, input('Аллея: ').split()))
i, j = 0, N
ans_i, ans_j = 1, N
ans_len = N
while i < N - K + 1:
    if len(set(a[i:j])) == K:
        section = len(a[i:j])
        if section < ans_len:
            ans_i, ans_j = i + 1, j
            ans_len = section
        j -= 1
    else:
        i += 1
        j = N
print(ans_i, ans_j)
