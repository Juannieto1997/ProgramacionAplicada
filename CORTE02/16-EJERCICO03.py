## 16-EJERCICO 03 RECURSIÓN por Kenneth Jouseph Gomez GUerrero
'''
Los ejercicios son de caracter obligatorio, sin embargo no se les asignará una calificación, el objetivo de estos
es que ustedes practiquen y mejoren sus habilidades.
estos los deben subir de manera individual en su cuenta de Git
'''
'''
se les darán multiples funciones, así como la documentación correspondiente
 deben completar las tareas marcadas como TODO
'''
## DEMOSTRACIONES MATEMATICAS
# ejercicios tomados de: https://elvex.ugr.es/decsai/java/pdf/7D-Ejercicios.pdf

#TODO: Demuestre por inducción que, para todo n mayor o igual que 4, n!>2^n
#TODO: Un granjero ha comprado una pareja de conejos para criarlos y luego venderlos.

#   Si la pareja de conejos produce una nueva pareja cada mes y la nueva pareja
#   tarda un mes más en ser también productiva, ¿cuántos pares de conejos podrá
#   poner a la venta el granjero al cabo de un año?

def Conejos(c_num): 
    if c_num < 2: #Establecemos la condicion la cual sera la cantidad de conejos que se reproducen el cual sea menor a 2
        return(c_num) #retornamos el numero 
    return Conejos(c_num-1)+Conejos(c_num-2) #Indica que el número devuelto antes entra en la "fórmula de la secuencia de Fibonacci" y vuelve
    if c_num: #s_num se pone en un bucle para pasar la cantidad de veces que queremos construir
        return (c_num) #el numero puestro retornara la funcion 
print(f" la cantidad  de crias hechas durante un año son  {Conejos(12)}") #IMprimimos el codigo y vemos la cantidad de crias teniendo en cuenta la cantidad de meses que habra.


## Solución a la torre de Hanoi
def Hanoi (fichas,col1=1,col2=2,col3=3):
    if fichas==1: #Estblecemos la sumatoria de una ficha a otra como es 1,2,3....
        print ("la ficha se mueve de ",col1,"a",col3) #Aca Imprimiremos la ubicacion de la ficha 

    else: 
        Hanoi(fichas-1,col1,col3,col2)  #Dentro de esta funcion lo que intentaremos hacer sera la ficha puesta le contaremos como le restaremos la ubicacion de cada una de estas
        print("la ficha se mueve de ",col1,"a",col3) #Aca Imprimiremos el dialogo de como se movera de ubicacion la ficha 
        Hanoi (fichas-1,col2,col1,col3) #Dentro de esta funcion lo que intentaremos hacer sera la ficha puesta le contaremos como le restaremos la ubicaci pero teniendo en cuenta como esta estara alrevez
    return #mientras colocamos una ficha a un espacio vacio colocamos otra ficha un espacio con fichas mayores a esta

Hanoi(3)#Dentro de este ubicaremos el numero de fichas con la que vamos a jugar 

## Ejercicio objetos.

# TODO: 1. Cree un archivo, Taller donde llevará acabo el codigo principal
#       crear una lista de vehiculos que se encuentran en el taller en ese momento que tienen asociados: fecha de entrega, costo, modelo, año y dueño
#       crear una caja donde se almacena el dinero y se lleva registro de los movimientos
#       crear una lista de empleados que tienen asociado un nombre, cargo, salario, vehiculo y documento
#       Crear una lista de clientes que tienen asociado un nombre, vehiculo y documento

# TODO: 2 Ejecute sobre so codigo principal:
#       ingresar un vehiculo nuevo al taller (validar cupo)
#       Sacar un vehiculo del taller (se debe generar un pago por parte del cliente)
#       PAgar a los empleados (se debe hacer una reducción en el dinero de la caja)
#       Contrarar a una persona nueva
#       Despedir a una persona
#       Encontrar un vehiculo a partir de su dueño y determinar si está en el taller

caja=500000000     #Se declara la variable al inicio para tener el dinero de la caja como base (5.000.000 como base)
vehiculos = 0

class vehicle:
    def _init_(self, d_delivery, cost, model, year, owner):
        self.d_delivery = d_delivery
        self.cost = cost
        self.model = model
        self.year = year
        self.owner = owner

list_car = []
list_car.append(vehicle('13/09/2022', '10000', 'hyundai n vision 74', '2022','Samuel'))  # Para ingresar un nuevo vehiculo realizamos en nombre de la lista. append y como parametro el nombre de la clase y sus caracteristicas
list_car.append(vehicle('15/09/2022', '20000', 'porsche 911 turbo s gtr', '2022', ' Jouseph'))
list_car.append(vehicle('06/01/2022', '3000', 'lamborghini aventador', '2013', 'Juan Jose'))


def sacarvehiculo(sacar_v,pago):  # sacar_v = el indice del vehiculo que se desea sacar     pago = El pago que realiza el cliente
    list_car1 = list_car.pop(sacar_v)
    global caja, vehiculos
    caja+=pago
    vehiculos-=1
    return list_car1,caja,vehiculos

vehiculos += len(list_car)  # Llevar al cuenta de vehiculos que hay en el taller
print("Hay", vehiculos, "vehiculos")

# TODO: 3 Todas las funciones que implemente deben estar en un script distinto al principal y donde se definen sus clases
#       NOTA - (la UNICA exepción son las funciones que definen dentro de sus clases.)

