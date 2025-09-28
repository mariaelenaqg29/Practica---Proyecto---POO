class Serie:
    def __init__(self, n):
        self.n = n
        self.lista = []

    def generar(self):
        if self.n == 1:
            self.lista = [2]
        else:
            self.lista = [2, 5]
            for i in range(2, self.n):
                self.lista.append(self.lista[i-1] + self.lista[i-2])

    def mostrar(self):
        print(f"\nLOS {self.n} PRIMEROS TÉRMINOS DE LA SERIE SON: ")
        print(self.lista)

while True:
    n = int(input("INGRESAR EL NÚMERO DE TÉRMINOS : "))
    if n >= 1:
        break

serie = Serie(n)  
serie.generar()   
serie.mostrar()    