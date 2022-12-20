import random
import numpy as np

modelo = open("modelo.csv", "w")

pesos = {
"NED":7.32,
"SEN":6.23,
"ENG":7.20,
"USA":6.54,
"ARG":7.75,
"POL":6.27,
"FRA":7.36,
"AUS":5.96,
"JPN":6.35,
"ESP":7.27,
"MAR":6.44,
"CRO":6.89,
"BRA":8.00,
"SUI":6.81,
"POR":7.11,
"KOR":6.15
}

jogos = {
    1: ["NED", "USA"],
    2: ["ARG", "AUS"],
    3: ["JPN", "CRO"],
    4: ["BRA", "KOR"],
    5: ["FRA", "POL"],
    6: ["ENG", "SEN"],
    7: ["MAR", "ESP"],
    8: ["POR", "SUI"],
}

wins = [
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
]

loses = [
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
"TMN",
]

'''Peso calculado com o ranking do site Elo e FIFA do dia 02/12/2022, sendo 60% para o ranking Elo e 40% para o ranking da FIFA * 80% no peso final.
Cálculo do peso, ex: Holanda.
Elo = 2047
Fifa = 1694,51
Pontuação máxima Elo = 2137 - Mínimo = 403  - Diferença = 2137 - 403 = 1734 => (2047-403)/(1734/10) =~ 9,48
Pontuação máxima FIFA = 1841,30 - Mínimo = 762,22  - Diferença = 1841,30 - 762,22 = 1079,08 => (1694,51-762,22)/(1079,08/10) =~ 8,64
Peso Holanda = ((9,48 * 0,6) + (8,64 * 0,4)) * 0,8 = 7,32
Peso final = 80% do ranking + 20% de aleatoriedade

Placares
Se a diferença entre os pesos finais for menor ou igual a 0,5 = Empate 0x0 => Vitória do maior peso final
Se a diferença entre os pesos finais for maior que 0,5 e menor ou igual a 1,5 = Vitória 1x0
Se a diferença entre os pesos finais for maior que 1,5 = vitória (com placar aleatório entre 2 a 4)x0
'''

for loop in range(1,17):
    a = jogos.get(loop)
    pfa=((pesos.get(a[0])) + (.2 * random.randint(1, 10)))
    pfb=((pesos.get(a[1])) + (.2 * random.randint(1, 10)))
    dif = np.sqrt((pfa - pfb) ** 2)
    if pfa > pfb:
        vitorioso = a[0]
        derrotado = a[1]
    else:
        vitorioso = a[1]
        derrotado = a[0]
    if dif <= 0.5:
        placara = 0
        placarb = 0
    elif dif <= 1.5:
        if pfa - pfb > 0:
            placara = 1
            placarb = 0
        else:
            placara = 0
            placarb = 1
    else:
        if pfa - pfb > 0:
            placara = random.randint(2,4)
            placarb = 0
        else:
            placara = 0
            placarb = random.randint(2,4)
    arquivo = str(loop) + "," + a[0] + "," + str(placara) + "," + a[1] + "," + str(placarb) + "," + vitorioso + "\n"
    modelo.write(arquivo)
    wins[loop - 1] = vitorioso
    loses[loop - 1] = derrotado
    if loop == 8:
        jogos[9] = [wins[0], wins[1]]
        jogos[10] = [wins[2], wins[3]]
        jogos[11] = [wins[4], wins[5]]
        jogos[12] = [wins[6], wins[7]]
    if loop == 12:
        jogos[13] = [wins[8], wins[9]]
        jogos[14] = [wins[10], wins[11]]
    if loop == 14:
        jogos[15] = [wins[12], wins[13]]
        jogos[16] = [loses[12], loses[13]]
modelo.close()
