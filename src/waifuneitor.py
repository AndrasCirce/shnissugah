class Separador:

    def __init__(self):
        self.p =[]
        self.terminales = []
        self.no_terminales = []
        self.lado_derecho = []
        self.Derecha()
        self.No_Ter()
        self.Ter()
        print ('Lado derecha ', '\n', self.lado_derecho, '\n')
        #print('No Terminales ', '\n', self.no_terminales, '\n')
        print('Terminales ','\n',self.terminales,'\n')

    def Derecha(self):
        with open("Gramatica2.txt") as prueba:
            for line in prueba:
                f = line.find('>')
                s = line.find('\n')
                j = line[f+2: s]
                self.p += j.split()
                self.lado_derecho = self.p
        #print ('Lado derecha ', '\n', self.lado_derecho, '\n')
        return self.lado_derecho
        

    def No_Ter(self):
        with open("Gramatica2.txt") as prueba:
            for line in prueba:
                f = line.find('>')
                if line[:f-1] not in self.no_terminales:
                    self.no_terminales.append(line[:f-1])
        #print('No Terminales ', '\n', self.no_terminales, '\n')
        return self.no_terminales
        

    def Ter(self):
        for sim in self.lado_derecho: #por cada simbolo en lado derecho
            if sim not in self.no_terminales: #si el simbolo no esta en no terminales
                if sim not in self.terminales and sim != 'E': #y si sim no esta en terminales
                    self.terminales.append(sim) #introduce sim a terminales
        #print('Terminales ','\n',self.terminales,'\n')
        return self.terminales
        