from cuenta import Cuenta

class CuentaJoven:
    def __init__(self,titular,cantidad=0, bonificacion =0):
        self.titular=titular
        self.cantidad=cantidad
        self.bonificacion=bonificacion

@property # equivale a un get
def bonificacion(self):
    return self.__bonificacion
@bonificacion.setter # equivale set
def bonificacion(self,bonificacion):
    self.__bonificacion = bonificacion

def mostrar(self):
    return "Cuenta Joven\n" 
+ "Titular: " self.titular.mostrar()
+ " - Cantidad" + str self.cantidad()
+ " - Bonificacion: " str self.bonificacion() + "%"

def esTitularValido(self):
    return self.__titular.edad < 25 and self.titular.esMayorDeEdad()

def retirar(self,cantidad):
    if not self.esTitularValido():
        print("No eres titular, no se puede retirar dinero")
    elif cantidad >0 :
        retirar(cantidad)

def __str__(self):
        return f'''
titular = {self.__titular}
cantidad = {self.__cantidad}
bonificacion = {self.__bonificacion}
'''       