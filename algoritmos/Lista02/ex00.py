teste = 1
while True:
    p = int(input())
    if p == 0:
        break
    print("Teste %d" % teste)
    teste+= 1  
    ordem_ent = input()
    ordem = ordem_ent.split()
    for i in range(0,len(ordem)):
        if ordem[i] == str(i+1):
            print(ordem[i])
    print()
    