teste = 1
rodadas = int(input('Insira o número de rodadas: '))
while 0 < rodadas < 1000:
	print('Teste',teste)
	p1 = input('Nome do jogador #1: ')
	if 1 > len(p1) > 10 or not p1.isalpha():
		quit()
	p2 = input('Nome do jogador #2: ')
	if 1 > len(p2) > 10 or not p2.isalpha():
		quit()
	while rodadas:
		game = input('Números jogados: ')
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
			print('O vencedor é: ', p1)
		else:
			print('O vencedor é: ', p2)
		rodadas -= 1 
		
	print()
	ans = input('Deseja jogar novamente? (s/n): ')
	if ans == 's':
		teste += 1
		rodadas = int(input('Insira o número de rodadas: '))
	elif ans == 'n':
		quit()
	else:
		print('erro: valor não definido')
		quit()
