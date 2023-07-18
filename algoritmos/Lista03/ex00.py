N = int(input())

I = list(map(int, input().split()))

s = 0

for e in I:
    s += e - 1
print(s) 
