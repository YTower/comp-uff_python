C, V = map(int, input().split())

res = []
pos = []

for i in range(C):
	t = [int(x) for x in (input().split())]
	t_total = 0
	for k in range(V):
		t_total += t[k]
	res.append(t_total)
	pos.append(t_total)
pos.sort()

for i in range(3):
	for k in range(len(pos)):
		if res[k] == pos[i]:
			print(k+1)
			