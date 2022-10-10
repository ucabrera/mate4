import math
import numpy as np
from matplotlib import pyplot as plt

def graficoGradiente(punto_inicial):
    X = np.linspace(-1, 6)
    Y = np.linspace(-1, 4)
    X, Y = np.meshgrid(X,Y)
    Z = np.sin((X**2 + Y**2)/5)
    etiquetas = ['Eje x', 'Eje y', 'z=seno(x^2 + y^2)/5']
  
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.plot_wireframe(X,Y,Z)
    ax.set_xlabel(etiquetas[0])
    ax.set_ylabel(etiquetas[1])
    ax.set_zlabel(etiquetas[2]);
    
    ax1 = fig.add_subplot(1, 2, 2)
    
    pr, ph = np.gradient(Z,0.05,0.05)
    ax1.contour(X,Y,Z,20)
    ax1.quiver(X,Y,pr,ph)
    ax1.set_xlabel(etiquetas[0])
    ax1.set_ylabel(etiquetas[1])
    
    plt.show()
    coord = punto_inicial

    return([coord[0], coord[1], [ax, ax1]])    

def graficarPaso(punto_anterior, punto_actual, h):
    ax = h[0]
    ax1 = h[1]
    
    XL = ax.get_xlim()
    YL = ax.get_ylim()
    ZL = ax.get_zlim()
    
    menores = [XL[0], YL[0], ZL[0]]
    mayores = [XL[1], YL[1], ZL[1]]
    
    punto_actual1 = np.max(np.matrix([punto_actual,  menores]),axis=0).tolist()[0]
    punto_actual1 = np.min(np.matrix([punto_actual1, mayores]),axis=0).tolist()[0]
    
    punto_anterior1 = np.max(np.matrix([punto_anterior,  menores]),axis=0).tolist()[0]
    punto_anterior1 = np.min(np.matrix([punto_anterior1, mayores]),axis=0).tolist()[0]
        
    ax.plot3D([punto_anterior1[0],punto_actual1[0]],[punto_anterior1[1],punto_actual1[1]],[punto_anterior1[2],punto_actual1[2]],color='r',lw=1, ls='-', marker='o', markersize=2)
    
    XL = ax1.get_xlim()
    YL = ax1.get_ylim()
    
    menores = [XL[0], YL[0]]
    mayores = [XL[1], YL[1]]
        
    punto_actual2 = np.max(np.matrix([punto_actual[:2],  menores]),axis=0).tolist()[0]
    punto_actual2 = np.min(np.matrix([punto_actual2[:2], mayores]),axis=0).tolist()[0]
    
    punto_anterior2 = np.max(np.matrix([punto_anterior[:2],  menores]),axis=0).tolist()[0]
    punto_anterior2 = np.min(np.matrix([punto_anterior2[:2], mayores]),axis=0).tolist()[0]
    
    ax1.plot([punto_anterior2[0],punto_actual2[0]],[punto_anterior2[1],punto_actual2[1]],color='r',lw=1, ls='-', marker='o', markersize=2)
    plt.draw()
    plt.pause(.01)
    
    
def descensoPorGradiente(punto_inicial, alfa, tolerancia, iteraciones):
    [x, y, h] = graficoGradiente(punto_inicial)
    z = np.sin((x ** 2 + y ** 2)/5)
    pasos = 0
    cambioZ = 1

    while (pasos < iteraciones) and (cambioZ > tolerancia):
        punto_anterior = [x, y, z]

        gradiente_x = (2 * x * np.cos((x ** 2 + y ** 2) / 5)) / 5
        gradiente_y = (2 * y * np.cos((x ** 2 + y ** 2) / 5)) / 5
    
        x = x - alfa * gradiente_x
        y = y - alfa * gradiente_y
        z = np.sin((x ** 2 + y ** 2) / 5)

        cambioZ = math.fabs(z - punto_anterior[2])
        graficarPaso(punto_anterior, [x, y, z], h)
        pasos = pasos + 1
    
    print('El valor de x es: ', x)
    print('El valor de y es: ', y)
    print('El valor de z es: ', z)
    print("Pasos dados = ", pasos)

descensoPorGradiente([3, 0], 0.2, 10**-5, 50)
descensoPorGradiente([1, 1], 0.2, 10**-5, 50)

    
