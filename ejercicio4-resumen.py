import statsmodels.api as sm
import pandas as pd

#Datos
df = pd.read_csv('ratings.csv')
x_quality = df["quality"]
y_helpfulness = df["helpfulness"]
y_clarity = df["clarity"]
y_easiness = df["easiness"]

#Para utilizar el comando OLS de statsmodels, es necesario incluir los "Intercept" 
#(lo hacemos incluyendo un vector de unos)
ones = [1 for x in range(0, len(df["quality"]))]
df_ajust = list(zip(ones, x_quality))

print(sm.OLS(y_helpfulness, df_ajust).fit().summary2())
print(sm.OLS(y_clarity, df_ajust).fit().summary2())
print(sm.OLS(y_easiness, df_ajust).fit().summary2())