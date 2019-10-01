class SeparadorGramatica:

    def __init__(self):
        self.lado_derecho = []
        self.no_terminales = []
        self.terminales = []
        self.gramatica = []
        self.separar()
        print(self.terminales)
        print(self.no_terminales)

    def get_produccion(self, pos):#devuelve produccion leida del lado derecho
        produccion = self.lado_derecho[pos].split()
        return produccion
    def separar(self):
        separador = '>'
        vacio = 'E'

        with open('Gramatica2.txt') as grammar_file:
            for line in grammar_file:
                self.gramatica.append(line.strip()) #remueve espacios
                symbols = line.split() #junta en lista symbols los simbolos leidos en line
                no_terminal = symbols.pop(0) #asigna no_terminal al primer elemento sacado de symbols

                if no_terminal not in self.no_terminales: #si no_terminal no esta en no terminales la agrega 
                    self.no_terminales.append(no_terminal)

                right_side = '' #rigth_side es una cadena vacia 
                for symbol in symbols: #por cada elemento en symbols
                    if symbol == separador: #si symbol es una flecha no lo agrega
                        continue
                    right_side += symbol + ' ' #agrega a rigth_side los elementos de symbol mas un espacio
                self.lado_derecho.append(right_side.strip()) #agrega a lado_derecho rigth_side sin espacios

            for text in self.lado_derecho: #por cada elemento en lado_derecho
                symbols = text.split() #junta en lista symbols los simbolos leidos en lado_derecho

                for symbol in symbols: #por cada elemento de la lista symbols
                    if symbol in self.no_terminales: #si symbol ya esta en no_terminales no lo agrega
                        continue
                    if symbol not in self.terminales and symbol != vacio: #si no esta en terminales y symbol no es vacio lo agrega terminales
                        self.terminales.append(symbol)