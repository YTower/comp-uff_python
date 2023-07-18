N = int(input())
P = input()
for i in range(N):
    m = int(input())

    if m == 1 and P == 'A':
        P = 'B'
    elif m == 1 and P == 'B':
        P = 'A'

    elif m == 2 and P == 'B':
        P = 'C'
    elif m == 2 and P == 'C':
        P = 'B'

    elif m == 3 and P == 'C':
        P = 'A'
    elif m == 3 and P == 'A':
        P = 'C'

print(P)
