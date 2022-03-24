import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import statsmodels.tsa.stattools as stats

#Se suprime el FutureWarning sobre un elemento deprecated de la biblioteca statsmodel de Pandas
warnings.simplefilter(action='ignore', category=FutureWarning)

#Lectura del archivo
serie = pd.read_csv("TS_d_2.csv", delimiter = ",",parse_dates=[0], index_col=0)
print(serie.head(10)) #Ver primeros 10

#Con la propiedad 'iloc' se seleccionan todos los elementos de la columna 0 de la serie temporal
#Esta transformación es necesaria, ya que el método adfuller() recibe como parámetro un arreglo 1-D
datos = serie.iloc[:,0].values

#Con los datos seleccionados, se aplica el Augmented Dickey-Fuller test
resultado = stats.adfuller(datos)

#Se imprimen los distintos resultados de aplicar el test a la serie temporal
print(f"Valor estadístico del test: {resultado[0]}")
print(f"Valor P: {resultado[1]}")
print("Valores Críticos")
for key,value in resultado[4].items():
  print(f"{key}: {value}")
  
#Se aplica diferenciación a la serie temporal
#El método dropna(), descarta el primer valor que se obtiene como resultado de la diferenciación, el cual es NAN
#Si no se descarta el valor NAN, no se puede pasar los resultados como parámetro del adfuller()
serie_diff = serie.diff().dropna()

#Se selecciona la columna 0 de los datos de la serie con diferenciación
datos_diff = serie_diff.iloc[:,0].values

#Se aplica el Augmented Dickey-Fuller test
resultado_diff = stats.adfuller(datos_diff)

#Se imprimen los resultados obtenidos del test
print(f"Valor estadístico del test: {resultado_diff[0]}")
print(f"Valor P: {resultado_diff[1]}")
print("Valores Críticos")
for key,value in resultado_diff[4].items():
  print(f"{key}: {value}")
  
#Se gráfican ambas series temporales, la original, y la serie con diferenciación
fig, axes = plt.subplots(2, 2)
serie.plot(ax=axes[0,0])
serie.hist(ax=axes[0,1])
serie_diff.plot(ax=axes[1,0])
serie_diff.hist(ax=axes[1,1])
plt.figtext(0.5,0.95, "Serie temporal sin aplicar diferenciación", ha="center", va="top", fontsize=14, color="white")
plt.figtext(0.5,0.5, "Serie temporal con diferenciación", ha="center", va="top", fontsize=14, color="white")
plt.subplots_adjust(hspace = 0.7 )
plt.show()