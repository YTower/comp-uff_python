teste = 1
rodadas = int(input())
while 0 < rodadas < 1000:
    print('Teste',teste)
    p1 = input()
    if 1 > len(p1) > 10 or not p1.isalpha():
        quit()
    p2 = input()
    if 1 > len(p2) > 10 or not p2.isalpha():
        quit()
    while rodadas:
        game = input()
        game = game.split()
        if len(game) != 2:
            quit()
        res = 0
        for num in game:
            num = int(num)
            if 0 > num > 5:
                quit()
            res += num
        if res % 2 == 0:
            print(p1)
        else:
            print(p2)
        rodadas -= 1
    print()
    teste += 1
    rodadas = int(input())