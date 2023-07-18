N = int(input('Número de rodadas: '))
while 0 < N <= 10:
    p1_score = 0
    p2_score = 0
    while N:
        game = input('Números jogados: ')
        game = game.split()
        for num in game:
            num = int(num)
            if 0 > num > 10:
                quit()
        if game[0] > game[1]:
            p1_score += 1
        elif game[0] < game[1]:
            p2_score += 1
        N -= 1
    print()
    print(f'Score Jogador #1: {p1_score} | Jogador #2: {p2_score}')
    print()
    N = int(input('Número de rodadas: '))
    