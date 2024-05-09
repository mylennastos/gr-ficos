import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:/Users/Mylenna/Documents/Teste-LIDAR/Dispositivo_3_0490/Dados.txt", sep=";", names=['Col1', 'Col2'])
df[['Name','Temperatura']] = df['Col2'].str.split(':', expand=True)
df['Temperatura'] = df['Temperatura'].str.replace('C', "")
df['Temperatura'] = pd.to_numeric(df['Temperatura']) 
df = df.drop('Col2', axis=1)

print(df)
# Selecionar linhas pares da coluna 'Col1'
linhas_pares = df.iloc[::2]

# Selecionar linhas ímpares da coluna 'Col1'
linhas_impares = df.iloc[1::2]


print("Linhas Pares:")
print(linhas_pares)

#print("\nLinhas Ímpares:")
#print(linhas_impares)

df_lidar = linhas_impares
df_temperatura_interna_central = linhas_pares

print(df_lidar)
print(df_temperatura_interna_central)

x1 = df_lidar['Col1']
y1 = df_lidar['Temperatura']
x2 = df_temperatura_interna_central['Col1']
y2 = df_temperatura_interna_central['Temperatura']
plt.plot(x1,y1,color='blue')
plt.scatter(x1,y1,color='red')
plt.plot(x2,y2,color='black')
plt.scatter(x2,y2,color='green')
plt.title('Temperatura do LIDAR e Temperatura interna central')
plt.xlabel('DATA_HORA')
plt.ylabel('temperatura em C')
plt.grid()
plt.legend(['temperatura LIDAR','Data', 'temperatura CENTRAL', 'Data'])
plt.show()
