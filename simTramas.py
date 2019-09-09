#Víctor Hugo Flores Pineda 155990
#Rebeca Baños
#Python 3
import numpy as np 
import matplotlib.pyplot as plt 

#Genera las tramas de longitud aleatoria con bits aleatorios
def generarTramas():
    tramas = list()
    rand = np.random.randint(5,11,10000)
    for i in range(0,9999):
        tramas.append(list(np.random.bytes(rand[i])))
    return tramas    


#Calcula la distribución de las tramas y muestra una gráfica
def longTramas(tramas):
        count = np.zeros(20)
        max = 0
        for trama in tramas:
                if len(trama)>max:
                        max = len(trama)
                index = len(trama)
                count[index] = count[index]+1
        min = 0
        for n in count:
                if n != 0:
                        break
                min = min +1
        xAxis = np.linspace(min,max,max-min+1)
        yAxis = count[min:max+1]
        plt.figure()
        plt.stem(xAxis,yAxis)
        plt.ylim(0,1900)
        plt.title('Distribución de longitud de tramas')

#Se genera el byte stuffing
def byteStuffing(tramas):
        byteIni = 245     #representacion ascii de (§)
        byteFin = 208     #representacion ascii de (ð)
        esc = 27         #representación ascii de ESC
        for trama in tramas:
                aux = 0
                tramaIter = iter(trama)
                for b in tramaIter:
                        if b == byteIni or b == byteFin or b == esc :
                                trama.insert(aux,esc)
                                aux = aux + 1
                                b = next(tramaIter)
                        aux + aux+1
                trama.insert(0,byteIni)
                trama.append(byteFin)
        return tramas   

#Genera un cierto porcentaje de error en las tramas
#Y muestra la cantidad de errores, así como errores por trama
def errPorcen(porcentaje,tramas):
        totBytes = 0
        for trama in tramas:
                totBytes = totBytes + len(trama)
        cantErr = round(porcentaje*totBytes)
        distErr = np.random.randint(0,totBytes,cantErr)
        tramasErr = 0
        ErrMin = np.zeros(20)
        ErrMed = np.zeros(20)
        maxMin = 0
        maxMed = 0
        aux = 0
        for trama in tramas:
                badT = False
                ErrXTrama = 0
                for i in range(len(trama)):
                        if aux in distErr:
                                trama[i] =  list(np.random.bytes(1))[0]
                                badT = True
                                ErrXTrama = ErrXTrama + 1
                        aux = aux + 1
                if badT:
                        tramasErr = tramasErr + 1
                if len(trama) == 7:
                        ErrMin[ErrXTrama] = ErrMin[ErrXTrama] + 1
                        if ErrXTrama > maxMin:
                                maxMin = ErrXTrama
                if len(trama) == 10:
                        ErrMed[ErrXTrama] = ErrMed[ErrXTrama] + 1
                        if ErrXTrama > maxMed:
                                maxMed = ErrXTrama
        print("número total de bytes erroneos: " + str(cantErr))
        print("número total de tramas erroneas: " + str(tramasErr))
        minMin = 0
        for n in ErrMin:
                if n != 0:
                        break
                minMin = minMin +1
        xAxis = np.linspace(minMin,maxMin,maxMin-minMin+1)
        yAxis = ErrMin[minMin:maxMin+1]
        plt.figure()
        plt.stem(xAxis,yAxis)
        plt.ylim(0,1500)
        plt.title('Distrubución de errores por trama de longitud mínima para '+str(porcentaje)+' de error')
        minMed = 0
        for n in ErrMed:
                if n != 0:
                        break
                minMed = minMed +1
        xAxis2 = np.linspace(minMed,maxMed,maxMed-minMed+1)
        yAxis2 = ErrMed[minMed:maxMed+1]
        plt.figure()
        plt.stem(xAxis2,yAxis2)
        plt.ylim(0,1500)
        plt.title('Distrubución de errores por trama de longitud media para '+str(porcentaje)+' de error')
        return tramas

#valida los bits de inicio y fin de las tramas y despliega las estadísticas pertinentes
def valTramas(tramas):
        tramasErr = 0
        tramasCorr = 0
        for trama in tramas:
                if trama[0] == 245 and trama[len(trama)-1] == 208:
                        tramasCorr = tramasCorr + 1
                else:    
                        tramasErr = tramasErr + 1
        print("Tramas identificadas correctamente: " + str(tramasCorr))
        print("Tramas descartadas: " + str(tramasErr))
        print("Tasa de tramas descartadas: "+ str(tramasErr/10000))
        


tramas = generarTramas()
longTramas(tramas)
tramasStuffing = byteStuffing(tramas)
longTramas(tramasStuffing)
print("tramas con 0.2 de error")
tramas2 = errPorcen(0.2,tramasStuffing)
valTramas(tramas2)
print("\n")
print("tramas con 0.1 de error")
tramas1 = errPorcen(0.1,tramasStuffing)
valTramas(tramas1)
print("\n")
print("tramas con 0.05 de error")
tramas05 = errPorcen(0.05,tramasStuffing)
valTramas(tramas05)
print("\n")
print("tramas con 0.02 de error")
tramas02 = errPorcen(0.02,tramasStuffing)
valTramas(tramas02)
plt.show()


