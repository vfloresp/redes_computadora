#Víctor Hugo Flores Pineda 155990
#Rebeca Baños
#Python 3
import numpy as np 
import matplotlib.pyplot as plt 

#Genera las tramas de longitud aleatoria con bits aleatorios
def generarTramas():
    tramas = list()
    rand = np.random.randint(5,11,10000)
    for i in range(0,999):
        tramas.append(list(np.random.bytes(rand[i])))
    distTramas(rand)
    return tramas    

#Calcula la distribución de las tramas y muestra una gráfica
def distTramas(rand):
        count = np.zeros(6)
        for j in rand:
                index = j-5
                count[index] = count[index]+1
        xAxis = np.linspace(5,10,6)  
        plt.stem(xAxis,count)
        plt.ylim(0,1900)
        plt.title('Distribución de longitud de tramas')
        plt.show()
        
#Se genera el byte stuffing
def byteStuffing(tramas):
        byteIni = 245   #representacion ascii de (§)
        byteFin = 208     #representacion ascii de (ð)
        for trama in tramas:
                trama.insert(0,byteIni)
                trama.append(byteFin)   

#Genera un cierto porcentaje de error en las tramas
def errPorcen(porcentaje,tramas):
        cantErrores = tramas*porcentaje
        


tramas = generarTramas()
byteStuffing(tramas)



