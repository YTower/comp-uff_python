dinheiro,operacoes = [int(x) for x in input().split()]

d = dinheiro
e = dinheiro
f = dinheiro

for i in range(operacoes):
    operacao = input().split()
    
    if len(operacao) == 3:
        tipo = operacao[0]
        jogador = operacao[1]
        valor = int(operacao[2])
        
        if tipo == 'C':
            if jogador == 'D':
                d -= valor
            elif jogador == 'E':
                e -= valor
            elif jogador == 'F':
                f -= valor
        if tipo == 'V':
            if jogador == 'D':
                d += valor
            elif jogador == 'E':
                e += valor
            elif jogador == 'F':
                f += valor
    
    if len(operacao) == 4:
        tipo = operacao[0]
        recebedor = operacao[1]
        pagador = operacao[2]
        valor = int(operacao[3])
        
        if tipo == 'A':
            if recebedor == 'D':
                d += valor
                if pagador == 'E':
                    e -= valor
                elif pagador == 'F':
                    f -= valor
            elif recebedor == 'E':
                e += valor
                if pagador == 'D':
                    d -= valor
                elif pagador == 'F':
                    f -= valor
            elif recebedor == 'F':
                f += valor
                if pagador == 'E':
                    e -= valor
                elif pagador == 'D':
                    d -= valor
print(d,e,f)
        