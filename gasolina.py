import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Lendo o arquivo csv
gasolina = pd.read_csv('gasolina.csv')

#Criando o gráfico de linha
plt.figure(figsize=(10,6))
sns.lineplot(x='dia', y='venda', data=gasolina, marker='o')

#Adicionando titulo e rotulos
plt.title('Preço médio da gasolina em São Paulo - Julho 2021 (dias 1-10)')
plt.xlabel('Dia')
plt.ylabel('Preço de venda (R$)')

#Salvando o gráfico como imagem
plt.savefig('gasolina.png')

#Exibindo o gráfico
plt.show()
