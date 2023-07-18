N = input()
if not N.isdigit():
	quit()
N = int(N)
while 1 <= N <= 10:
	p1_score = 0
	p2_score = 0
	while N > 0:
		game = input()
		game = game.split()
		if len(game) != 2:
			quit()
		for num in game:
			if not num.isdigit():
				quit()
			num = int(num)
			if num < 0 or num > 10:
				quit()
		if game[0] > game[1]:
			p1_score += 1
		elif game[0] < game[1]:
			p2_score += 1
		N -= 1
	print(p1_score, p2_score)
	N = input()
	if not N.isdigit():
		quit()
	N = int(N)