N = int(input())

for i in range(N):
    M = int(input())
    f = list(map(int, input().split()))
    f2 = sorted(f, reverse = True)
    count = 0
    for i in range(M):
        if f[i] == f2[i]:
            count += 1
    print(count)
