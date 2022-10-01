#Declarar variáveis em uma linha
age, name = (23, 'Augusto')

#Variáveis => snake_case
#CONSTANTES => MAIÚSCULAS

print("10/2 =",10/2," divisão com uma barra retorna float")
print("10//2 =",10//2," divisão com duas barras retorna inteiro")

#Atribuição
saldo = 500 #Simples
print(saldo)
saldo += 200
print(saldo)
saldo -= 100
print(saldo)
saldo //= 5
print(saldo)
saldo %= 100
print(saldo)
saldo **= 2
print(saldo)

#Operadores
curso = "Curso de Python"
nome_curso = curso
print(curso is nome_curso) # is = ==
print(curso == nome_curso)
print("Python" in curso) # Verifica se contem

#If ternário
status = "Sucesso" if saldo > age else "Falha"
print(status)

#for
#texto = input("Informe um texto: ")
texto = "Augusto"
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()

#Strings
print("upper converte todas as letras para maiúsculo. Ex. = ",curso.upper())
print("lower converte todas as letras para minúsculo. Ex. = ",curso.lower())
print("title converte as primeiras letras para maiúsculo, e o resto para minúsculo. Ex. = ",curso.title())
espacos = "   Espacos   "
print(espacos)
print("strip remove todos os espacos. Ex. = ", espacos.strip())
print("lstrip remove todos os espacos a esqurda. Ex. = ", espacos.lstrip())
print("rstrip remove todos os espacos a direita. Ex. = ", espacos.rstrip())
teste = "Teste"
print("center =", teste.center(10,"#"))
print("join =", ".".join(teste))

#%
nome = "Augusto"
idade = 43
profissao = "Técnico Eletrônico"
linguagem = "Python"
dados = {"nome": "Augusto", "idade": 43, "profissao": "Técnico Eletrônico", "linguagem": "Python"}

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))
print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}." .format(nome, idade, profissao, linguagem))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**dados))
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

#Fatiamento
nome = "Augusto Ryuiti Koga"
print("nome[0] =", nome[0])
print("nome[-1] =", nome[-1])
print("nome[:7] =", nome[:7])
print("nome[8:] =", nome[8:])
print("nome[8:14] =", nome[8:14])
print("nome[8:14:2] =", nome[8:14:2])
print("nome[:] =", nome[:])
print("nome[::-1] =", nome[::-1])

valores = input().split()
print(f"{int(valores[0])*int(valores[1])/12:.3f}")
