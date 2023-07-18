n, m = [int(x) for x in input().split()]
res = 0
i = 0
lock = [int(x) for x in input().split()]
while i < n-1:
    res += abs(m - lock[i])
    if lock[i] == lock[i+1]:
        i += 1
    else:
        lock[i+1] += (m-lock[i])
    i += 1
print(res)
