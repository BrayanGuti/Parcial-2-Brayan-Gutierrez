import abc
#Clase abstractra que hereda a Carro
class Vehiculo(abc.ABC):
    #Metodos abstractos que se heredan en carro
    @abc.abstractmethod         
    def check():
        ...
    @abc.abstractmethod
    def precios():
        ...
class Carro(Vehiculo):
    #Constructor se almacen todos los inputs de cada Carro
    def __init__(self, tipo : str, horas : int, dias : int, min : int, hora_entrada : float, reserva : bool) -> None:
        self.tipo = tipo
        self.horas = horas
        self.dias = dias
        self.min = min
        self.hora_entrada = hora_entrada
        self.reserva = reserva
        #Se chequean los inputs
        self.check()
    
    #Metodos regular:
    def check(self):
        #Se chequean los tipos que sean correctos
        if not isinstance(self.tipo, str) or not isinstance(self.horas, int)or not isinstance(self.dias, int)or not isinstance(self.min, int)or not isinstance(self.hora_entrada, float) or not isinstance(self.reserva, bool):
            raise TypeError("Algun parametro no es del tipo pernitente")
        #Se chequean que el tipo de auto sea el correcto
        elif(self.tipo != "van" and self.tipo != "SUV" and self.tipo != "compact"):
            raise ValueError("El tipo de auto ingresado no esta en nuestra base de datos")
        #Se chequean que los inputos no sean negativos            
        elif(self.horas < 0 or self.dias < 0 or self.dias < 0 or self.min < 0):
            raise ValueError("Uno de sus datos ingresados es negativo")
    


    
    #Metodo que devuelve un atributo nuevo  de la clase Carro: 
    
    #Devuelve el precio del auto que entra al parking
    @property
    def precios(self):
        """El precio para compact por hora es de 5000 por min sera 5000/60 y por dia sera 5000*24"""
        """Para SUV sera el mismo valor total de compact multiplicado por 1.2"""
        """Para van sera el mismo valor total de compact multiplicado por 1.5"""
        self.precio = ((self.horas)*5000) + ((self.dias)*5000*24) + (self.min) *(5000/60)
        if self.tipo == "van": 
            self.precio *= 1.5
        elif self.tipo == "SUV":
            self.precio *= 1.2     
        return self.precio 