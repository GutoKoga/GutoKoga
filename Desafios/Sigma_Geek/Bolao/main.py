import pandas as pd

df = pd.read_csv('bolao.csv')
print(df.head())

import random

class Team:
  BEST_SCORE = 1837.6 # Brasil (BRA)

  # TODO: Definir um construtor com os atributos adequados (tendo em vista o conteúdo de uma célula do CSV)
  def __init__(self, cellData):
    teamData = cellData.split(';')
    self.name = teamData[0]
    self.score = float(teamData[1])

  def motivate(self):
    self.lastMotivation = random.uniform(70, (self.score * 100) / Team.BEST_SCORE)
    return self.lastMotivation
# Mapa em que a chave será a letra do grupo e o valor as seleções (que ordenaremos pelas "melhores").
bestTeamsByGroup = {}
# Percorre o dataframe (dados do CSV) para criar nossos objetos/seleções.
for label, content in df.items():
  # TODO: Instanciar as 4 seleções do grupo, com seus respectivos nomes e score.
  team1 = Team(content[0])
  team2 = Team(content[1])
  team3 = Team(content[2])
  team4 = Team(content[3])
  # TODO: Simular os melhores do grupo com base na motivação de cada seleção.
  #       Calculada a partir do seu ranking FIFA aliado a uma pitada de aleatoriedade.
  bestTeamsByGroup[label] = sorted([ team1, team2, team3, team4 ], key=Team.motivate, reverse=True)

# TODO: Imprimir os grupos, ordenados pelas melhores seleções de cada (apenas 2 se classificam)
for grupo, motivatedTeams in bestTeamsByGroup.items():
  print(f'Grupo {grupo}: ', end="")
  for team in motivatedTeams:
    print(f'{team.name} ({team.lastMotivation:.2f}) ', end="")
  print()