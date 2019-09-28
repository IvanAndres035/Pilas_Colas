class Metodo_Recursivo:

    __ArregloV = []
    __b = int(0)
    __Producto = int(1)

#METODO CONSTRUCTOR CON EL ARREGLO Y EL NUMERO DE B
    def __init__(self, ArregloV ,b):
        self.__ArregloV = ArregloV
        self.__b = b

#METODO MULTIPLICAR, EN EL QUE SE REALIZA LA OPERACION DE FORMA ITERATIVA  LA SOLUCION DEL PROGRAMA
    def Multiplicar(self):
#CICLO FOR; FOR I EN EL RANGO DE  0 HASTA LA LECTURA DEL ARREGLOV.
        for i in range(0, len(self.__ArregloV)):

#SI LOS ELEMENTOS DEL ARREGLOV, SON MAYORES A "B"
          if self.__ArregloV[i] > self.__b:

#EL PRODUCTO ES IGUAL AL EL PRODUCTO PO LOS ELEMENTOS DEL ARREGLOV
                self.__Producto = self.__Producto * self.__ArregloV[i]

#METODO PARA OBTENER EL PRODUCTO DE LA OPERACION REALIZADA ANTERIOMENTE
    def getProductos(self):
        return self.__Producto

elemento =  Metodo_Recursivo([10,2,11,3,9,2,-1,4],4)
elemento.Multiplicar()
print(elemento.getProductos())
