import time
import Adafruit_DHT
import datetime

#C:\Users\NGRoboticsAdmin\AppData\Local\Programs\Python\Python37\python.exe C:\Users\NGRoboticsAdmin\Desktop\archivolocal.py
##===========================Maquina de estados nivel 1===================##
def inicio():
    print("Estamos en estado de inicio")
    time.sleep(2)
    print("despues del sleep")
    #return([1,3,4])
    print("esto esta abajo del return")
    inicio_sesion()

def inicio_sesion():
    usuario=input("Favor de ingresar el usuario: ")
    contrasena=input("Favor de ingresar la contrasena: ")
    print(usuario)
    print(contrasena)
    if(usuario=="admin" and contrasena=="1234"):
        sesion_iniciada()
    else:
        print("usuario o contrasena incorrecta")
        inicio()

def tiempo_real():
    hum, tem = Adafruit_DHT.read_retry(11, 17)
    print("la humedad es: {}".format(hum))
    print("la temperatura es: {}".format(tem))
    print("informacion en tiempo real")
    ts=time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    with open('registro.txt',mode='w+') as f:
        f.write("En el tiempo {}, la humedad es: {}, la temperatura es: {}".format(st,hum,tem))

def informacion_recopilada():
    print("informacion registrada previamente")

def sesion_iniciada():
    print("usuario inicio sesion")
    opcion_seleccionada=input("seleccione la opcion buscada: \n1. informacion tiempo real \n2. Informacion registrada previamente")
    if(opcion_seleccionada=="1"):
        tiempo_real()
    elif(opcion_seleccionado=="2"):
        informacion_recopilada()
    else:
        print("la opcion seleccionada no esta disponible")
        sesion_iniciada()

x=inicio()
print(x)

