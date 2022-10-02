import pandas as pd #Importa a biblioteca pandas

lista = [1, 2, 3]
tuplas = ("Banana", "Maçã", 10, 50)
dicionario = {"Maçã":20, "Banana":10, "Laranja":15, "Uva":5}

lista[0] = 0 #Substitui o primeiro item da lista
lista.remove(0) #Remove o número 0
print(len(lista)) #Retorna o tamanho da lista
print(3 in lista) #Retorna se existe o elemento na lista
print(max(lista)) #Retorna o maior da lista
print(min(lista)) #Retorna o menor da lista
lista.append(4) #Insere o elemento na lista
lista.extend([5,6]) #Quando temos que inserir mais de um elemento
print(lista.count(4)) #Mostra quantos elementos contem na lista
lista.sort() #Ordena a lista
print(lista)

dicionario["Maçã"] = 25 #Substitui o valor do item
print(dicionario.keys())
print(dicionario.values())
dicionario.setdefault("Limão", 22)
print(dicionario)

#PANDAS
df = pd.read_csv("D:\!!GTK\Repositórios\Git\Cursos\Dio\Python\Arquivos\Cusro_Python_Pandas_Digital_Innovation-master\datasets\Gapminder.csv", error_bad_lines=False, sep=";")
df = df.rename(columns={"country":"Pais","continent":"Continente","year":"Ano","lifeExp":"Expectativa de vida","pop":"Pop Total","gdpPercap":"PIB"})
print(df.head(10))
print(df.shape) #Total de linhas e colunas
print(df.columns) #Retorna as colunas
print(df.dtypes) #Retorna com os tipos dos dados
print(df.tail(10)) #Default = 5
print(df.describe()) #Descrição dos dados das colunas
print(df["Continente"].unique()) #Lista todos continentes apenas uma vez
oceania = df.loc[df["Continente"] == "Oceania"]
print(oceania.head())
print(oceania["Continente"].unique())
print(df.groupby("Continente")["Pais"].nunique())
print(df.groupby("Ano")["Expectativa de vida"].mean())
print(df["PIB"].mean())
print(df["PIB"].sum())