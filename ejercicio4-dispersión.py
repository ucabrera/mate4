import pandas as pd
import matplotlib.pyplot as plt

# Lectura de archivo
df = pd.read_csv('ratings.csv')
x_quality = df["quality"]
y_helpfulness = df["helpfulness"]
y_clarity = df["clarity"]
y_easiness = df["easiness"]

# Grafico de dispersión
fig, axis = plt.subplots()
axis.scatter(x_quality, y_helpfulness, marker="o", color="black")
plt.xlabel('Eje x - Quality')
plt.ylabel('Eje y - Helpfulness')
plt.show()

fig, axis = plt.subplots()
axis.scatter(x_quality, y_clarity, marker="o", color="black")
plt.xlabel('Eje x - Quality')
plt.ylabel('Eje y - Clarity')
plt.show()

fig, axis = plt.subplots()
axis.scatter(x_quality, y_easiness, marker="o", color="black")
plt.xlabel('Eje x - Quality')
plt.ylabel('Eje y - Easiness')
plt.show()