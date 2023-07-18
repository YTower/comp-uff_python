colisao = 0
x0a,y0a,x1a,y1a = [int(x) for x in input().split()]
x0b,y0b,x1b,y1b = [int(x) for x in input().split()]


if x0a <= x0b <= x1a:
    if y0a <= y0b <= y1a:
        colisao = 1
    elif y0b <= y0b <= y1b:
        colisao = 1
elif x0b <= x0a <= x1b:
    if y0b <= y0a <= y1b:
        colisao = 1
    elif y0b <= y0b <= y1b:
        colisao = 1
        
elif x0a == y0a == x1a == y1a == x0b == y0b == x1b == y1b:
    colisao = 1
print(colisao)
