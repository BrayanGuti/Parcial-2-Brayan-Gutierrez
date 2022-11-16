## Parking lot

## Funcionalidad

Este programa permite al administrador del parqueadero llevar un registro de la cantidad de espacios que tiene para cada tipo de carro y calcular las ganancias va teniendo a lo largo de la jornada y a la hora de entrar un auto le permite validar si tiene espacios disponibles, ademas le permite a los carros (usuarios) tener una reserva. 
## UML
Parking es una clase que contiene como atributos los espacios de parqueo de cada tipo de auto y tambien tiene como atributo las ganancias de todo el parking, como metodos tenemos que muestre las ganancias actuales, que aparque un auto, que cheque que todos los inputs son correctos y que muestre los espacios disponibles actuales y del dia de mañana.

Carro es una Clase que hereda de la clase abstracta Vehiculo que le hererada los metodos check y percios, esta clase carro pose como atributos todas las caracteristicas del carro como son su tipo, horas, dias, min, si es una reseva, hora de entrada y el precio a pagar por el servicio como metodos solo tiene check que chuquea que todos los inputs sean correctos


## Python Code

Uso if y objetos de tipo carro para que el programa sepa  tipo de auto, si tiene un espacio para ese tipo de auto para que luego calcule las ganancias atravez de los atributos del objeto carro y almacene el carro en su espacio, si tiene espacio,  si no que diga porque no puede parquear el auto. Ademas uso el decorador property  para ahorrame ciertas lineas de codigo y uso exceptions para asegurarme que todos los inputs son validos.