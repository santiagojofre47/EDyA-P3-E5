from claseListaPosicion import ListaSecuecial

if __name__ == '__main__':
    objLista = ListaSecuecial()
    print('ANTES DE SUPRIMIR REPETIDOS')
    objLista.insertar(10,1)
    objLista.insertar(5,2)
    objLista.insertar(7,3)
    objLista.insertar(5,4)
    objLista.insertar(2,5)
    objLista.insertar(10, 6)
    objLista.recorrer()
    print('DESPUES DE SUPRIMIR REPETIDOS')
    objLista.suprimir_repetidos()
    objLista.recorrer()
  
 
