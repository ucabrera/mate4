import pandas as pd
import matplotlib.pyplot as plt

# Lectura de archivo
df = pd.read_csv('ratings.csv')
x_quality = df["quality"]
y_helpfulness = df["helpfulness"]
y_clarity = df["clarity"]
y_easiness = df["easiness"]

# Estadísticos
x_quality_mean = x_quality.mean()
y_helpfulness_mean = y_helpfulness.mean()
y_clarity_mean = y_clarity.mean()
y_easiness_mean = y_easiness.mean()

x_quality_diff = x_quality - x_quality_mean
y_helpfulness_diff = y_helpfulness - y_helpfulness_mean
y_clarity_diff = y_clarity - y_clarity_mean
y_easiness_diff = y_easiness - y_easiness_mean

sxx = (x_quality_diff ** 2).sum()

syy_helpfulness = (y_helpfulness_diff **2 ).sum()
syy_clarity = (y_clarity_diff ** 2).sum()
syy_easiness = (y_easiness_diff ** 2).sum()

sxy_helpfulness = (x_quality_diff * y_helpfulness_diff).sum()
sxy_clarity = (x_quality_diff * y_clarity_diff).sum()
sxy_easiness = (x_quality_diff * y_easiness_diff).sum()

b1_helpfulness = sxy_helpfulness/sxx
b1_clarity = sxy_clarity/sxx
b1_easiness = sxy_easiness/sxx

b0_helpfulness = y_helpfulness_mean - b1_helpfulness * x_quality_mean
b0_clarity = y_clarity_mean - b1_clarity * x_quality_mean
b0_easiness = y_easiness_mean - b1_easiness * x_quality_mean

#Varianza
sce_helpfulness = (syy_helpfulness - (sxy_helpfulness ** 2) / sxx)
sce_clarity = (syy_clarity - (sxy_clarity ** 2) / sxx)
sce_easiness = (syy_easiness - (sxy_easiness ** 2) / sxx)

sigma_helpfulness = sce_helpfulness / (x_quality.count() - 2)
print("La varianza de helpfulness es: " + str(sigma_helpfulness))
sigma_clarity = (syy_clarity - (sxy_clarity ** 2) / sxx) / (x_quality.count() - 2)
print("La varianza de clarity es: " + str(sigma_clarity))
sigma_easiness = (syy_easiness - (sxy_easiness ** 2) / sxx) / (x_quality.count() - 2)
print("La varianza de easiness es: " + str(sigma_easiness))

print()
#Coeficiente de determinación
print("El coeficiente de determinación de helpfulness es: " + str(1 - (sce_helpfulness / syy_helpfulness)))
print("El coeficiente de determinación de clarity es: " + str(1 - (sce_clarity / syy_clarity)))
print("El coeficiente de determinación de easiness es: " + str(1 - (sce_easiness / syy_easiness)))

def modelo(x, ordenada_al_origen, pendiente):
  return ordenada_al_origen + pendiente * x

# Grafico de la recta
fig, axis = plt.subplots()
axis.scatter(x_quality, y_helpfulness, marker="o", color="black")
estimada = [modelo(x, b0_helpfulness, b1_helpfulness) for x in x_quality]
axis.plot(x_quality, estimada, linestyle="-", marker=None, color="orange")
plt.xlabel('Eje x - Quality')
plt.ylabel('Eje y - Helpfulness')
axis.set_title("ŷ = " + str(b0_helpfulness) + " + " + str(b1_helpfulness) + "x")
plt.show()

fig, axis = plt.subplots()
axis.scatter(x_quality, y_clarity, marker="o", color="black")
estimada = [modelo(x, b0_clarity, b1_clarity) for x in x_quality]
axis.plot(x_quality, estimada, linestyle="-", marker=None, color="orange")
plt.xlabel('Eje x - Quality')
plt.ylabel('Eje y - Clarity')
axis.set_title("ŷ = " + str(b0_clarity) + " + " + str(b1_clarity) + "x")
plt.show()

fig, axis = plt.subplots()
axis.scatter(x_quality, y_easiness, marker="o", color="black")
estimada = [modelo(x, b0_easiness, b1_easiness) for x in x_quality]
axis.plot(x_quality, estimada, linestyle="-", marker=None, color="orange")
plt.xlabel('Eje x - Quality')
plt.ylabel('Eje y - Helpfulness')
axis.set_title("ŷ = " + str(b0_helpfulness) + " + " + str(b1_helpfulness) + "x")
plt.show()