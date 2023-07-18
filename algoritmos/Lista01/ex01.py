testes = int(input())
robo_x = 0
movimentos = []
for i in range(0, testes):
    instrucoes = int(input())
    for j in range(instrucoes):
        instrucao = input().split()
        if instrucao[0] == 'SAME':
            instrucao.append(movimentos[int(instrucao[2])-1])
            if instrucao[3] == 'LEFT':
                robo_x -= 1
            elif instrucao[3] == 'RIGHT':
                robo_x += 1
            movimentos.append(instrucao[3])
        else: 
            instrucao == instrucao
            if instrucao[0] == 'LEFT':
                robo_x -= 1
            elif instrucao[0] == 'RIGHT':
                robo_x += 1
        
            movimentos.append(instrucao[0])
    print(robo_x)
    robo_x = 0
    movimentos = []
    