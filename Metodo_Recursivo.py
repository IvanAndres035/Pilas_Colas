class Metodo_Recursivo:

    __ArregloV = []
    __b = int(0)
    __Producto = int(1)

    def __init__(self, ArregloV ,b):
        self.__ArregloV = ArregloV
        self.__b = b

    def Multiplicar(self):
        for i in range(0, len(self.__ArregloV)):
            if self.__ArregloV[i] > self.__b:
                self.__Producto = self.__Producto * self.__ArregloV[i]

    def getProductos(self):
        return self.__Producto


elemento =  Metodo_Recursivo([1,2,3,4,5,6,7,8],4)
elemento.Multiplicar()
print(elemento.getProductos())


#Practicas
""" 
self.__numeros = input("Numeros del arreglo son: ")
self.__ArregloV.append(self.__numeros)
self.__b = int(input("Numero constante: "))
"""

#ahorita
'''
if (self._b <= 1):
                return self._b
            else:
                return self._b * (self._b - 1)
'''