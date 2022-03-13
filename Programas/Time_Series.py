import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series


serie = pd.read_csv("../CSV/TS_d_1.csv", delimiter = ",",parse_dates=[0], index_col=0)

'''
print(serie.head(5)) #Ver primeros 3
print(type(serie))


#Da ccantidad,promedio, desvaicion, min, max, cuartiles
#print(TS_d_1.describe())

print("Promedio: ",serie["temperatura"].mean())
print("Mediana : ",serie["temperatura"].median())
print("Desviación estándar: ",serie["temperatura"].std())

#Ejemplo Datos enero del 2004
print(serie.loc['2004-01'])


#Promedio por mes
print(serie.groupby(by=[serie.index.month]).mean())


#Pruebas Ignorar
monthlyDataframe = pd.DataFrame()
monthlyDataframe['month'] = [serie.index[i].month for i in range (len(serie))]
monthlyDataframe['temperature'] = [serie['temperatura'][i] for i in range (len(serie))]
#print(monthlyDataframe)


#Lag Features crear DataFrame con los valores y un Lag=5
temps = pd.DataFrame(serie.values)
log = pd.concat([temps.shift(5),temps.shift(4),temps.shift(3),temps.shift(2),temps.shift(1), temps], axis=1)
log.columns = ['t-4','t-3','t-2','t-1','t','t+1']
print(log.head(10))


#DataFrame con los valores, y un ancho de ventana de 3. Tenga las columnas: 'mínimo','media','máximo','t+1'

temps = pd.DataFrame(serie.values)
widthWindow = 3
#Corrimiento debe ser el valor de ancho de ventana - 1
shifted = temps.shift(widthWindow-1)
window = shifted.rolling(window=widthWindow)
#Se sacan el min,max y mean de la venatana
minimum = window.min()
means = window.mean()
maximum = window.max()
#Se cincatenan en el data dataframe
dataframe = pd.concat([minimum,means,maximum,temps], axis=1)
dataframe.columns = ['min','mean','max','t+1']
print(dataframe.head(10))




#A la variable series, aplíquele la instrucción series.plot().
#¿Qué puede decir del comportamiento de los datos según este gráfico?

serie.plot()
plt.show()



#Agrupe los datos y muestre un gráfico similar al de la seccion 6.4 de las lecturas (Stacked lines plots).
#¿Puede hacer algún comentario del comportamiento anual de los datos?
#IGNORAR ESTE PUNTO DE MOMENTO PORQUE DA ERROR 
groupsByYear = serie.groupby(pd.Grouper(freq='A'))
years = pd.DataFrame()
for name,group in groupsByYear:
    print(name.year,"\n",group.values)
    print("-----------------------------------")
    #years[name.year] = group.values
print(years.head(10))
#years.plot(subplots = True, legend = False)
#pd.show()

'''


