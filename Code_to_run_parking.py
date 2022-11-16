from Package.Parking_clases import Parking
from Package.Carro import Carro

#Se crean los autos que ingresan
Carro1 = Carro(tipo= "van", horas=1 , dias= 0, min= 0, hora_entrada=10.00, reserva= False)
Carro2 = Carro(tipo= "SUV", horas=1 , dias= 1, min= 0, hora_entrada=10.00, reserva= True)
Carro3 = Carro(tipo= "compact", horas=1 , dias= 1, min= 0, hora_entrada=10.00, reserva= True) 

"""Las horas de entrada son en hora militar"""

#Se crea el parqueadero
Parqueadero = Parking(espacios_van= 20, espacios_SUV= 20, espacios_compact= 20) 

#Se aparcan cada carro y se muestra como van variando los espacios disponibles y las ganacias actuales
Parqueadero.aparcar(objeto= Carro1)
Parqueadero.ganancias_actuales()
Parqueadero.espacios_disponibles_hoy()
Parqueadero.aparcar(objeto=Carro2)
Parqueadero.ganancias_actuales()
Parqueadero.espacios_disponibles_mañana()
Parqueadero.aparcar(objeto=Carro3)
Parqueadero.ganancias_actuales()
Parqueadero.espacios_disponibles_mañana()
