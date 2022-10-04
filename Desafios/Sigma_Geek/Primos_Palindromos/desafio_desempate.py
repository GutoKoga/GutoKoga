'''
Desafio de desempate: Achar o próximo número da sequencia.
961212169 = 37
102454201 = 19
337515733 = 37
347676743 = 47
?????????

Segundo o vencedor, o próximo número é um número primo palíndromo de 9 dígitos cuja soma dos próprios números também é um primo.

Acredito que seja o número 350454053, cuja soma é 29.
'''

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
                    achei = 1
                    break
        arquivo_primos.close()
    if achei == 1:
        achei = 0
        digito2 = 0
        for digito in teste:
            digito2 = digito2 + int(digito)
        arquivo_primos = open("primos.txt", "r")
        while len(teste) > 1:
            divisor = int(arquivo_primos.readline())
            if int(digito2) % int(divisor) == 0:
                break
            else:
                if int(digito2) <= int(divisor) ** 2:
                    print(teste, "=", digito2)
                    break
        arquivo_primos.close()