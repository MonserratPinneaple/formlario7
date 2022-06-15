
class Persona():
    def __init__(self,nombre,edad,docDNI):
        self._nombre = nombre
        self._edad = edad
        self._docDNI = docDNI #CURP?
        
@property # equivale a un get
def nombre(self):
    return self.__nombre
@nombre.setter # equivale set
def nombre(self,nombre):
    self.__nombre = nombre
    
@property # equivale a un get
def edad(self):
    return self.__edad
@edad.setter # equivale set
def edad(self,edad):
    if edad >= 18:
        print("Es mayor de edad")
    else:    
        print("Edad incorrecta")
    self.edad = edad

@property # equivale a un get
def docDNI(self):
    return self.__docDNI
    
def validar_docDNI(self):
    letras = "PITK960429MDFXJT04"
    if len(self.__docDNI) !=18:
        print("Incorretcto")
    else:
        print ("Correcto")

@docDNI.setter # equivale set
def docDNI(self,docDNI):
    self.docDNI = docDNI
    self.validar_docDNI()
    
def __str__(self):
    return f'''nombre = {self.__nombre}
    edad = {self.__edad}
    docDNI = {self.__docDNI}'''

def mostrar(self):
    return "Nombre: " + self.__nombre + "Edad: " +self.__edad + "CURP: " + self.__docDNI

def esMayorDeEdad (self):
    return self.__edad >= 18 