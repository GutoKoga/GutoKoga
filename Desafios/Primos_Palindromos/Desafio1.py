# Desafio 1: Achar o primeiro primo palíndromo de 9 dígitos.
arquivo = open("pi.txt", "r")
achei = 0
pi = arquivo.read()
final_arquivo = len(pi) - 8
for loop in range(final_arquivo):
    teste = pi[loop:loop+9]
    if teste == teste[::-1]:
        arquivo_primos = open("primos.txt", "r")
        while len(teste) > 1:
            divisor = int(arquivo_primos.readline())
            if int(teste) % int(divisor) == 0:
                break
            else:
                if int(teste) <= int(divisor) ** 2:
                    print(loop, teste)
                    achei = 1
                    break
        arquivo_primos.close()
    if achei == 1:
        break
