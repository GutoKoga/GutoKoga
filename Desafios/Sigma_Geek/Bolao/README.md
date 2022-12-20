# Bolão da Copa com Ciência de Dados - Fase Eliminatória

Peso calculado com o ranking do site Elo e FIFA do dia 02/12/2022, sendo 60% para o ranking Elo e 40% para o ranking da FIFA * 80% no peso final.

Cálculo do peso, ex: Holanda.

Elo = 2047

Fifa = 1694,51

Pontuação máxima Elo = 2137 - Mínimo = 403  - Diferença = 2137 - 403 = 1734 => (2047-403)/(1734/10) =~ 9,48

Pontuação máxima FIFA = 1841,30 - Mínimo = 762,22  - Diferença = 1841,30 - 762,22 = 1079,08 => (1694,51-762,22)/(1079,08/10) =~ 8,64

Peso Holanda = ((9,48 * 0,6) + (8,64 * 0,4)) * 0,8 = 7,32

Peso final = 80% do ranking + 20% de aleatoriedade

  

Placares

Se a diferença entre os pesos finais for menor ou igual a 0,5 = Empate 0x0 => Vitória do maior peso final

Se a diferença entre os pesos finais for maior que 0,5 e menor ou igual a 1,5 = Vitória 1x0

Se a diferença entre os pesos finais for maior que 1,5 = vitória (com placar aleatório entre 2 a 4)x0