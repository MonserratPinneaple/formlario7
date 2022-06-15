from clase_persona import Persona

class Cuenta:
    def __init__(self,titular,cantidad=0):
        self.titular = titular
        self.cantidad=cantidad
        bon=bon
        
@property # equivale a un get
def titular(self):
    return self.titular
@titular.setter # equivale set
def titular(self,titular):
    self.titular

@property # equivale a un get
def cantidad(self):
    return self.cantidad
    self.cantidad = cantidad
    
def mostrarCuenta(self):
    print("\nCuenta: "+self.getCuenta()+"\n Propietario: "+ self.getPersona()+
            "\nCantidad: "+str(self.getCantidad()))
    
def ingresar(self,cantidad):
    if cantidad > 0:
        self.__cantidad = self.__cantidad + cantidad

def retirar (self,cantidad):
    if cantidad > 0:
        self.__cantidad = self.__cantidad + cantidad


def __str__(self):
        return f'''
titular = {self.__titular}
cantidad = {self.__cantidad}
'''