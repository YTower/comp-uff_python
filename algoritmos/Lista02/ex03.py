div,n_div,mult,n_mult = [int(x) for x in input().split()]
numero = -1
if div != n_div and mult != n_mult:
    i = div
    while i <= mult:
      if i%div == 0 and i % n_div != 0 and mult % i == 0 and n_mult % i != 0:
        numero = i
        break
      i += div
print(numero)
