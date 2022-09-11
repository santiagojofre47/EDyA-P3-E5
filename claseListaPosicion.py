import numpy as np



class ListaSecuecial:
    __maximo = None
    __ult = None
    __lista = None
    
    def __init__(self, maximo = 10):
        self.__lista = np.empty(maximo,dtype=int)
        self.__maximo = maximo
        self.__ult = 0
    
    def lleno(self):
        return (self.__ult > self.__maximo-1)
    
    def vacio(self):
        return (self.__ult == 0)
            
    def shift(self,i):
        j = self.__ult
        while j > i:
            self.__lista[j] = self.__lista[j-1]

            j-=1
            
    def suprimir(self,posicion):
        if not self.vacio():
            if (posicion) >= 1 and (posicion) <= self.__ult:
                for i in range(self.__ult):
                    if i == posicion-1:
                        self.rshift(i)
                        self.__ult-=1
                    
    def rshift(self,i):
        while i < self.__ult:
            self.__lista[i] = self.__lista[i+1]
            i+=1

    def insertar(self,elemento,p):
        assert isinstance(elemento, int)
        if not self.lleno():
            if (p) >= 1 and (p) <= self.__ult+1:
                i = 0
                encontro = False
                while not encontro:
                    if i == p-1:
                        self.shift(i)
                        self.__lista[i] = elemento
                        self.__ult+=1
                        encontro = True
                    else:
                        i+=1
                    
            
            else:
                print('ERROR: posicion no valida')
        else:
            print('ERROR: no hay espacio')
    
    def recorrer(self):
        if not self.vacio():
            for i in range(self.__ult):
                print(self.__lista[i])
        else:
            print('ERROR: Lista vacia!')
    
    def recuperar(self, p):
        val = None
        if not self.vacio():
            if p >= 0 and p <= self.__ult-1:
                    val = self.__lista[p]
        return val
    
    def buscar(self, elemento):
        encontro = False
        i = 0
        val = None
        while not encontro and i<=self.__ult-1:
            if self.__lista[i] == elemento:
                encontro = True
                val = i
            else:
                i+=1
        
        return val
    def primer_elemento(self):
        val = None
        if not self.vacio():
            val = self.__lista[0]
        else:
            print('ERROR: Lista vacia!')
        return val
    
    def ultimo_elemento(self):
        val = None
        if not self.vacio():
            val = self.__lista[self.__ult-1]
        else:
            print('ERROR: Lista vacia!')
        return val
    
    def siguiente(self, p):
        if not self.vacio():
            val = None
            if p-1 >= 0 and p-1 < self.__ult-1:

                val = p+1
            else:
                print('ERROR: No hay mas elementos despues de la posicion ingresada!')
        else:
            print('ERROR: Lista vacia!')
    

    def anterior(self, p):
        if not self.vacio():
            val = None
            if p-1 > 0 and p-1 <= self.__ult-1:
                val = p-1
            else:
                print('ERROR: No hay una posicion anterior a la ingresada!')
        else:
            print('ERROR: Lista vacia!')
    
    def buscar_repetido(self,p):
        elemento = self.recuperar(p)
        encontro = False
        i = 0
        while i < self.__ult and not encontro:
            if (self.recuperar(i)== elemento) and p != i:
                self.suprimir(p+1)
                encontro = True
            else:
                i+=1

    def suprimir_repetidos(self):
        if not self.vacio():
            i = 0
            while i < self.__ult:
                posi = self.buscar_repetido(i)
                i+=1
  
    
