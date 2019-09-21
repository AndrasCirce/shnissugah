from analizador_lexico import AnalizadorLexico
from gramatica import SeparadorGramatica

class AnalizadorSintactico:

    def __init__(self):
        self.gramatica = SeparadorGramatica()
        self.lexico = AnalizadorLexico()
        self.matriz = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 4, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 5, 0, 0, 6, 0, 0, 7, 0, 0, 0, 0, 0],
            [0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 10, 0, 9, 0, 0, 0, 0],
            [0, 0, 11, 0, 0, 0, 11, 0, 0, 0, 11, 0, 0, 0],
            [0, 0, 0, 0, 12, 0, 0, 13, 0, 0, 0, 0, 0, 0],
            [0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0],
            [0, 0, 0, 0, 16, 0, 0, 16, 0, 0, 0, 15, 15, 0],
            [0, 0, 18, 0, 0, 0, 17, 0, 0, 0, 19, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 21, 0],
            [22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def lldriver(self):
        if len(self.lexico.tabla_errores) > 0: #si la tabla de errores esta vacia, continua
            return

        no_terminales = self.gramatica.no_terminales #lista columnas
        terminales = self.gramatica.terminales #lista filas
        stack = ['program'] #introduce simbolo inicial en pila vacia
        x = stack[0]  #asigna x a la parte alta de la pila
        a = self.lexico.siguiente() #asigna a el token de entrada
        print(x, a) #imprime parte alta de pila y token a leer

        while len(stack) > 0: #mientras la pila no este vacia
            if x in self.gramatica.no_terminales: #si x esta en los no terminales
                if self.matriz[no_terminales.index(x)][terminales.index(a)] != 0: #y si la posicion de a y x no es 0 
                    produccion = self.gramatica.get_produccion(self.matriz[no_terminales.index(x)][terminales.index(a)] - 1)
                    #print(produccion)
                    x = produccion[0]
                    # Ciclo de push
                    for element in produccion:
                        stack.append(element)
                else:
                    print('Error de sintáxis 1') #simbolo inexistente
                    #print(stack) #imprime la pila
                    return
            else:
                if x == a:
                    #print(stack)
                    stack.pop()
                    a = self.lexico.siguiente()
                else:
                    print('Error de sintáxis 2')
                    #print(stack)
                    return

        print('Sintáxis correcta')

def main():
    asintactico = AnalizadorSintactico()
    asintactico.lldriver()

if __name__ == '__main__':
    main()

