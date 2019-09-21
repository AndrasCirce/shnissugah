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
        no_terminales = self.gramatica.no_terminales #columnas de no terminales
        stack = [] #pila vacia
        stack.append('program') #agrega simbolo inicial a pila
        x = stack[0] #Asigna x a inicio de pila
        a = self.lexico.siguiente() #asigna a a simbolo a leer
        vacio = 'E' #vacio es E

        while len(stack) > 0: #mientras la pila no este vacia
            x = stack[len(stack) - 1] #asigna x a ultimo elemento en pila -1
            #print('----------------------------',x, 'es el ultimo en pila-----------------------------------')
            if x in no_terminales: #si x esta en no terminales
                if self.predict(x, a) != 0: #si la ocurrencia entre ultimo pila y simbolo a leer no es 0 
                    print('ocurrencia ',self.predict(x, a), ' entre ', x, ' y ', a)
                    #print(stack, 'pila')
                    produccion = self.gramatica.get_produccion(self.predict(x, a) - 1) #lista de las producciones a leer
                    x = produccion[0]
                    print('producciones a leer ',produccion)
                    stack.pop() #saca la produccion al tope de la pila
                    #print('-------------------------------hice pop-------------------------------------------')
                    # Ciclo de push
                    produccion.reverse() #invierte lista de producciones
                    for element in produccion: #para cada elemento en produccion
                        stack.append(element) #agregalo al final de la pila
                        #print('---------------------agregue en pila a', element,'--------------------------------')
                        #print(stack, 'nueva pila')
                else:
                    print('Error de sintáxis 1')
                    #print(stack)
                    return
            else:
                if x == vacio:
                    stack.pop()
                elif x == a:
                    stack.pop()
                    a = self.lexico.siguiente()
                    if a == '$':
                        break
                else:
                    print('Error de sintáxis 2')
                    return
        print('Sintáxis correcta')

    def predict(self, x, a): #devuelve simbolo de ocurrencia que pides
        return self.matriz[self.gramatica.no_terminales.index(x)][self.gramatica.terminales.index(a)]

def main():
    asintactico = AnalizadorSintactico()
    asintactico.lldriver()
    

if __name__ == '__main__':
    main()
