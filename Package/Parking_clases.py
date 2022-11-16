from Package.Carro import Carro
class Parking:
    #Constructor
    def __init__(self, espacios_van : int, espacios_SUV : int,  espacios_compact : int) -> None:
        self.espacios_van = espacios_van
        self.espacios_van_dia_siguiente = espacios_van
        self.espacios_SUV = espacios_SUV
        self.espacios_SUV_dia_siguiente = espacios_SUV
        self.espacios_compact = espacios_compact
        self.espacios_compact_dia_siguiente = espacios_compact
        self.ganancias = 0
        #Se chequean los inputs
        self.check()

    
    def check(self):
        #Se chequean los tipos que sean correctos
        if not isinstance(self.espacios_compact, int) or not isinstance(self.espacios_SUV, int)or not isinstance(self.espacios_van, int):
            raise TypeError("Algun parametro no es del tipo pernitente")
        #Se chequean que la cantidad de los espacios para estacionar no sean negativos
        elif(self.espacios_van < 0 or self.espacios_SUV < 0 or self.espacios_van < 0):
            raise ValueError("Uno de sus datos ingresados es negativo")
    
    #Se imprimen la informacion actual de los espacios del parking
    def espacios_disponibles_hoy(self):
        print(f"Los espacios disponibles para van son {self.espacios_van}")
        print(f"Los espacios disponibles para SUV son {self.espacios_SUV}")
        print(f"Los espacios disponibles para compact son {self.espacios_compact}")
    
    #Se imprimen la informacion actual de los espacios del parking de mañana
    def espacios_disponibles_mañana(self):
        print(f"Los espacios disponibles para el dia de mañana para van son {self.espacios_van_dia_siguiente}")
        print(f"Los espacios disponibles para el dia de mañana para SUV son {self.espacios_SUV_dia_siguiente}")
        print(f"Los espacios disponibles para el dia de mañana para compact son {self.espacios_compact_dia_siguiente}")

    #Se imprimen las ganancias actuales
    def ganancias_actuales(self):
        print(f"Las ganacias actuales son {self.ganancias}")
    
    

     #Se aparca el vehiculo
    def  aparcar(self, objeto : Carro):
        if(objeto.reserva == False):                                # Se comprueba si es una reserva
            if(objeto.hora_entrada > 6.0 and objeto.hora_entrada < 18.0):       #Se compruba de que este en un horario donde el parking este abierto
                #Se mira el tipo de auto
                if(objeto.tipo == "van"):
                    if(self.espacios_van >= 1):                 #Se comprueba de que halla un espacio para la van       
                        self.ganancias += objeto.precios        #Se suman las ganancias que genera el aparcamiento de una van
                        self.espacios_van -=1                   #Se resta un espacio a los correspondientes a las vans
                    else:
                        print("No contamos con estacionamientos en este momento, losentimos")
                if(objeto.tipo == "SUV"):
                    if(self.espacios_SUV >= 1):                 #Se comprueba de que halla un espacio para el SUV  
                        self.ganancias += objeto.precios        #Se suman las ganancias que genera el aparcamiento de un SUV
                        self.espacios_SUV -=1                   #Se resta un espacio a los correspondientes a los SUV
                    else:
                        print("No contamos con estacionamientos en este momento, losentimos")
                if(objeto.tipo == "compact"):
                    if(self.espacios_compact >= 1):             #Se comprueba de que halla un espacio para el compact
                        self.ganancias += objeto.precios        #Se suman las ganancias que genera el aparcamiento de un compact
                        self.espacios_compact -=1               #Se resta un espacio a los correspondientes a los compact
                    else:
                        print("No contamos con estacionamientos en este momento, losentimos")
            else:
                print("Cerramos, losentimos")
        else:
            if(objeto.hora_entrada > 6.0 and objeto.hora_entrada < 18.0):       #Se compruba de que este en un horario donde el parking este abierto
                #Se mira el tipo de auto
                if(objeto.tipo == "van"):
                    if(self.espacios_van_dia_siguiente >= 1):                 #Se comprueba de que halla un espacio para la van       
                        self.ganancias += objeto.precios                      #Se suman las ganancias que genera el aparcamiento de una van
                        self.espacios_van_dia_siguiente -=1                   #Se resta un espacio a los correspondientes a las vans
                    else:
                        print("No contamos con estacionamientos en este momento, losentimos")
                if(objeto.tipo == "SUV"):
                    if(self.espacios_SUV_dia_siguiente >= 1):                 #Se comprueba de que halla un espacio para el SUV  
                        self.ganancias += objeto.precios        #Se suman las ganancias que genera el aparcamiento de un SUV
                        self.espacios_SUV_dia_siguiente -=1                   #Se resta un espacio a los correspondientes a los SUV
                    else:
                        print("No contamos con estacionamientos en este momento, losentimos")
                if(objeto.tipo == "compact"):
                    if(self.espacios_compact_dia_siguiente >= 1):             #Se comprueba de que halla un espacio para el compact
                        self.ganancias += objeto.precios            #Se suman las ganancias que genera el aparcamiento de un compact
                        self.espacios_compact_dia_siguiente -=1               #Se resta un espacio a los correspondientes a los compact
                    else:
                        print("No contamos con estacionamientos en este momento, losentimos")
            else:
                print("La hora indicada no se encuentra dentro de nuestros horarios, losentimos")