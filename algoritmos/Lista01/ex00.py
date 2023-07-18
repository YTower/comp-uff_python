# Ler valores L, C, M e N
num_linhas, num_colunas, num_linhas_lote, num_colunas_lote = map(int, input().split())
plantacao = []
for lin in range(num_linhas):
    linha = list(map(int, input().split()))
    plantacao.append(linha)
maior_conhecido = -1
for lin_lote in range(num_linhas // num_linhas_lote):
    for col_lote in range(num_colunas // num_colunas_lote):
        soma = 0
        for lin in range(lin_lote * num_linhas_lote, (lin_lote * num_linhas_lote) + num_linhas_lote):
            for col in range(col_lote * num_colunas_lote, (col_lote * num_colunas_lote) + num_colunas_lote):
                soma += plantacao[lin][col]
        if soma > maior_conhecido:
            maior_conhecido = soma
print(maior_conhecido)
