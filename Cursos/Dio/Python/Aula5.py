import pandas as pd #Importa a biblioteca pandas

df1 = pd.read_excel("D:\!!GTK\Repositórios\Git\Cursos\Dio\Python\Arquivos\Cusro_Python_Pandas_Digital_Innovation-master\datasets\Aracaju.xlsx", encoding = "ISO-8859-1")
df2 = pd.read_excel("D:\!!GTK\Repositórios\Git\Cursos\Dio\Python\Arquivos\Cusro_Python_Pandas_Digital_Innovation-master\datasets\Fortaleza.xlsx", encoding = "ISO-8859-1")
df3 = pd.read_excel("D:\!!GTK\Repositórios\Git\Cursos\Dio\Python\Arquivos\Cusro_Python_Pandas_Digital_Innovation-master\datasets\Natal.xlsx", encoding = "ISO-8859-1")
df4 = pd.read_excel("D:\!!GTK\Repositórios\Git\Cursos\Dio\Python\Arquivos\Cusro_Python_Pandas_Digital_Innovation-master\datasets\Recife.xlsx", encoding = "ISO-8859-1")
df5 = pd.read_excel("D:\!!GTK\Repositórios\Git\Cursos\Dio\Python\Arquivos\Cusro_Python_Pandas_Digital_Innovation-master\datasets\Salvador.xlsx", encoding = "ISO-8859-1")

print(df5.head())
