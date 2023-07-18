def criar_matriz(largura,altura,entrada_x,entrada_y,saida_x,saida_y,mapa,larg_mapa):
    for i in range(largura):
        for j in range(altura):
            if (i+1)%2 == 0 and (j+1)%2 == 0:
                larg_mapa.append('A')
            elif i+1 == entrada_x and j+1 == entrada_y:
                larg_mapa.append('E')
            elif i+1 == saida_x and j+1 == saida_y:
                larg_mapa.append('S')
            else:
                larg_mapa.append(' ')
        mapa.append(larg_mapa)
        larg_mapa = []
    
def contar_armarios(mapa,largura,altura):
    armarios = 0
    for i in range(largura-1):
        for j in range(altura-1):
            if mapa[i][j] == 'A':
                armarios += 1
    return(armarios)
                
            
def maior_caminho(armarios,entrada_x,saida_x,entrada_y,saida_y,largura,altura,map_a,map_b,dist_a,dist_b):
    if largura in map_a or altura in map_a:
        if abs(entrada_x-saida_x) in dist_a and abs(entrada_y-saida_y) in dist_a:
            caminho = ((largura*altura)-2)-(armarios * 2)
        elif abs(entrada_x-saida_x) in dist_a and abs(entrada_y-saida_y) in dist_b:
            caminho = ((largura*altura))-(armarios * 2)
        elif abs(entrada_x-saida_x) in dist_b and abs(entrada_y-saida_y) in dist_a:
            caminho = ((largura*altura))-(armarios * 2)
        elif abs(entrada_x-saida_x) in dist_b and abs(entrada_y-saida_y) in dist_b:
            caminho = ((largura*altura)-2)-(armarios * 2)
    else:
        if abs(entrada_x-saida_x) in dist_a and abs(entrada_y-saida_y) in dist_a:
            caminho = ((largura*altura))-(armarios * 2)
        elif abs(entrada_x-saida_x) in dist_a and abs(entrada_y-saida_y) in dist_b:
            caminho = ((largura*altura)-2)-(armarios * 2)
        elif abs(entrada_x-saida_x) in dist_b and abs(entrada_y-saida_y) in dist_a:
            caminho = ((largura*altura)-2)-(armarios * 2)
        elif abs(entrada_x-saida_x) in dist_b and abs(entrada_y-saida_y) in dist_b:
            caminho = ((largura*altura))-(armarios * 2)
    return(caminho)

def main():
    largura,altura = [int(x) for x in input().split()]
    entrada_x,entrada_y = [int(e) for e in input().split()]
    saida_x,saida_y = [int(s) for s in input().split()]
    mapa = []
    larg_mapa = []
    dist_a = [2,6,10]
    dist_b = [0,4,8]
    map_a = [3,7,11]
    map_b = [1,5,9]
    criar_matriz(largura,altura,entrada_x,entrada_y,saida_x,saida_y,mapa,larg_mapa)
    armarios = contar_armarios(mapa,largura,altura)
    caminho = maior_caminho(armarios,entrada_x,saida_x,entrada_y,saida_y,largura,altura,map_a,map_b,dist_a,dist_b)
    print(caminho)

main()
