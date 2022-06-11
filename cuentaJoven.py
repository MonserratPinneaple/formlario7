from clase_cuenta import Cuenta
class CuentaJoven:
    def __init__(self,titular,cantidad):
        self.__titular=titular
        self.__cantidad=cantidad
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
    @cantidad.setter # equivale set
    def ingresar(self,c):
        self.cantidad = self.cantidad +c
    def retirar(self,c):
        if(self.cantidad-c > 0):
            self.cantidad = cantidad
    
def mostrarCuenta(self):
    print("\nCuenta: "+self.getCuenta()+"\n Propietario: "+ self.getPersona()+
            "\nCantidad: "+str(self.getCantidad()))
    
    
def __str__(self):
        return f'''
titular = {self.__titular}
cantidad = {self.__cantidad}
'''        
        
