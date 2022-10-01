inicio = 5
divisor = [3]
posicao = 2

print("1 2")
print("2 3")

for dividendo in range(inicio, 100000000000000, 2):
    e_primo = 0
    for loop in range(len(divisor)):
        if dividendo % divisor[loop] == 0:
            break
        else:
            if dividendo <= divisor[loop] ** 2:
                e_primo = 1
                break
    if e_primo == 1:
        e_primo = 0
        posicao += 1
        print(posicao, dividendo)
        divisor.append(dividendo)
