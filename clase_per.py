class Persona:
    def __init__(self,nombre,edad,docDNI):
        self._nombre = nombre
        self._edad = edad
        self._docDNI = docDNI
        
@property # equivale a un get
def nombre(self):
    return self.__nombre
@nombre.setter # equivale set
def nombre(self,nombre):
    self.nombre = nombre
    
@property # equivale a un get
def edad(self):
    return self.__edad
@edad.setter # equivale set
def edad(self,edad):
    if edad >= 18:
        print("Es mayor de edad")
    else:    
        print("Es menor de edad")
    self.edad = edad

@property # equivale a un get
def docDNI(self):
    return self.__docDNI
@docDNI.setter # equivale set
def docDNI(self,docDNI):
    self.docDNI = docDNI
    
def __str__(self):
    return f'''nombre = {self.__nombre}
    edad = {self.__edad}
    docDNI = {self.__docDNI}'''