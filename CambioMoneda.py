def monedas():
    lista=[2,1,0.5,0.2,0.1,0.05,0.02,0.01]
    return lista
def monto():
    monto = 7.34
    return monto
def algoritmo_voraz(monedas,monto):
    cambio=[0,0,0,0,0,0,0,0]
    suma=0
    i=0

    while(suma<monto):
        while(i<len(monedas)):
            if(round(suma+monedas[i],2) <=monto):
                suma=round(suma+monedas[i],2)
                cambio[i]=cambio[i]+1
            else:
                i=i+1
    
    return cambio

def salida(monedas,monto):
    cambio=algoritmo_voraz(monedas,monto)
    print("La solucion encontrada es: ")

    for i in range(len(cambio)):
        if(cambio[i]==1):
            print(f"  {cambio[i]} moneda de {monedas[i]}")
        elif(cambio[i] >= 1):
            print(f"  {cambio[i]} moneda de {monedas[i]}")

    print(f"\nArreglo cambio: {cambio}")

#invocacion de metodos
monedas=monedas()
monto=monto()
salida(monedas,monto)