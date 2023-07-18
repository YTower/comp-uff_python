while True:
    movimentos = 0
    x1,y1,x2,y2 = [int(x) for x in input().split()]
    if x1 == y1 == x2 == y2 == 0:
        break
    else:
        if x1 == x2 and y1 == y2:
            movimentos = 0
            print(movimentos)
        elif x1 == x2 or y1 == y2:
            movimentos = 1
            print(movimentos)
        else:
            for k in range(8):
                if x2 == x1 - k and y2 == y1+k:
                    movimentos = 1
                elif x2 == x1 + k and y2 == y1-k:
                    movimentos = 1
                elif x2 == x1 + k and y2 == y1+k:
                    movimentos = 1
                elif x2 == x1 - k and y2 == y1-k:
                    movimentos = 1
            if movimentos == 0:
                movimentos = 2
            print(movimentos)
            