import random

def dame_un_dado():
    return random.randrange(1,7)

def dame_tirada(cant):
    tirada = []
    for dado in range (0,cant):
        tirada.append(dame_un_dado())
    return tirada

def esEscalera(tirada):
    tirada.sort()
    if (tirada[0]) == (tirada[1]-1) == (tirada[2]-2) == (tirada[3]-3) == (tirada[4]-4):
        return True
    else:
        return False





def obtenerCantidadEnTirada(tirada,cara):
    return tirada.count(cara)

def obtenerPuntajePorTirada(tirada,esPrimeravez):
    puntosAcumulados=0
    dadosAlCubilete= len(tirada)
    repeticionesPorDado=[]
    if esPrimeravez:
        if esEscalera(tirada):
            puntosAcumulados+=1500
            dadosAlCubilete-=len(tirada)
            return puntosAcumulados,dadosAlCubilete
        cantidadDeUnos=obtenerCantidadEnTirada(tirada,1)
        if(cantidadDeUnos>=3):
            puntosAcumulados += 1000
            dadosAlCubilete -= 3
            if(cantidadDeUnos==4):
                puntosAcumulados+=100
                dadosAlCubilete-=1
            if (cantidadDeUnos == 5):
                puntosAcumulados += 200
                dadosAlCubilete -= 2
            if (obtenerCantidadEnTirada(tirada,5)>=0):
                puntosAcumulados += 50 * obtenerCantidadEnTirada(tirada,5)
                dadosAlCubilete -= obtenerCantidadEnTirada(tirada,5)

            return puntosAcumulados, dadosAlCubilete
    else:
        for i in range (0,len(tirada)):
            repeticionesPorDado.append((i+1,obtenerCantidadEnTirada(tirada,i+1)))

        for dadoCantidad in repeticionesPorDado:
            CaraDelDado=dadoCantidad[0]
            cantidad=dadoCantidad[1]
            if (CaraDelDado!=1 and CaraDelDado!=5):
                if cantidad==3:
                    puntosAcumulados+=CaraDelDado * 100
                    dadosAlCubilete-=cantidad
            else:
                if (CaraDelDado==1):
                    puntosAcumulados += cantidad * 100
                    dadosAlCubilete -= cantidad
                if (CaraDelDado== 5):
                    puntosAcumulados += cantidad * 50
                    dadosAlCubilete -= cantidad

    return puntosAcumulados, dadosAlCubilete



print(obtenerPuntajePorTirada([1,2,3,4,5],True))
print(obtenerPuntajePorTirada([1,1,1,1,1],True))

print(obtenerPuntajePorTirada([1,5,5,3,2],False))
print(obtenerPuntajePorTirada([1,1,1,1,2],False))




