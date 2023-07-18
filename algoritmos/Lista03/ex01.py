V = int(input())
P = int(input())

    
if (V % P == 0):
    for i in range(P):
        print(V // P)
else:
    parcelas_maiores = V % P
    for i in range(parcelas_maiores):
        print(V // P + 1)
    for i in range(P - parcelas_maiores):
        print(V // P)
        