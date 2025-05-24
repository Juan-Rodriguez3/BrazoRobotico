import sys
import time
import serial
from Adafruit_IO import MQTTClient

run_count = 0

ADAFRUIT_IO_USERNAME = 
ADAFRUIT_IO_KEY =
    
FEED_ID_Send = 'State' 
FEED_ID_receive =  'Estado'
FEED_ID_receive0 =  'Servo1'
FEED_ID_receive1 =  'Servo2'
FEED_ID_receive2 =  'Servo3'
FEED_ID_receive3 =  'Servo4'

FEED_ID_receive4= 'Position1'
FEED_ID_receive5= 'position2'
FEED_ID_receive6= 'position3'
FEED_ID_receive7= 'Position4'


def connected(client):
    print('Subscribing to Feed {0}'.format(FEED_ID_receive))
    client.subscribe(FEED_ID_receive)
    print('Subscribing to Feed {0}'.format(FEED_ID_receive0))
    client.subscribe(FEED_ID_receive0)
    print('Subscribing to Feed {0}'.format(FEED_ID_receive1))
    client.subscribe(FEED_ID_receive1)
    print('Subscribing to Feed {0}'.format(FEED_ID_receive2))
    client.subscribe(FEED_ID_receive2)
    print('Subscribing to Feed {0}'.format(FEED_ID_receive3))
    client.subscribe(FEED_ID_receive3)
    print('Subscribing to Feed {0}'.format(FEED_ID_receive4))
    client.subscribe(FEED_ID_receive4)
    print('Subscribing to Feed {0}'.format(FEED_ID_receive5))
    client.subscribe(FEED_ID_receive5)
    print('Subscribing to Feed {0}'.format(FEED_ID_receive6))
    client.subscribe(FEED_ID_receive6)
    print('Subscribing to Feed {0}'.format(FEED_ID_receive7))
    client.subscribe(FEED_ID_receive7)
    print('Waiting for feed data...')


def disconnected(client):
    sys.exit(1)

def message(client, feed_id, payload):
    
    #print('Feed {0} received new value: {1}'.format(feed_id, payload))
    #Enviar el daro a arduino segun el feed

    if feed_id == FEED_ID_receive:
        print ('Toggle de boton de estado\n')
        mensaje = "M:" + payload + "\n"
        print (mensaje)
        miarduino.write(bytes(mensaje, 'utf-8')) 


    elif feed_id == FEED_ID_receive0:
        print (f'Enviando datos de Servo1: {payload}') 
        mensaje = 'B:' + payload + "\n"
        print (mensaje)
        miarduino.write(bytes(mensaje, 'utf-8')) #le agrego el salto de línea.

    elif feed_id == FEED_ID_receive1:
        print (f'Enviando datos de Servo2: {payload}') 
        mensaje = 'H:' + payload + "\n"
        print (mensaje)
        miarduino.write(bytes(mensaje, 'utf-8')) #le agrego el salto de línea.

    elif feed_id == FEED_ID_receive2:
        print (f'Enviando datos de Servo3: {payload}') 
        mensaje = 'C:' + payload + "\n"
        print (mensaje)
        miarduino.write(bytes(mensaje, 'utf-8')) #le agrego el salto de línea.

    elif feed_id == FEED_ID_receive3:
        print (f'Enviando datos de Servo4: {payload}') 
        mensaje = 'G:' + payload + "\n"
        print (mensaje)
        miarduino.write(bytes(mensaje, 'utf-8')) #le agrego el salto de línea.

    elif feed_id == FEED_ID_receive4:
        print (f'Enviando datos Save en la EEPROM: {payload}') 
        mensaje = 'P1:' + payload + "\n"     #le agrego el salto de línea y un prefijo
        print (mensaje)
        miarduino.write(bytes(mensaje, 'utf-8')) 

    elif feed_id == FEED_ID_receive5:
        print (f'Enviando datos Save en la EEPROM: {payload}') 
        mensaje = 'P2:' + payload + "\n"     #le agrego el salto de línea y un prefijo
        print (mensaje)
        miarduino.write(bytes(mensaje, 'utf-8')) 

    elif feed_id == FEED_ID_receive6:
        print (f'Enviando datos Save en la EEPROM: {payload}') 
        mensaje = 'P3:' + payload + "\n"     #le agrego el salto de línea y un prefijo
        print (mensaje)
        miarduino.write(bytes(mensaje, 'utf-8')) 

    elif feed_id == FEED_ID_receive7:
        print (f'Enviando datos Save en la EEPROM: {payload}') 
        mensaje = 'P4:' + payload + "\n"     #le agrego el salto de línea y un prefijo
        print (mensaje)
        miarduino.write(bytes(mensaje, 'utf-8')) 



    # Publish or "send" message to corresponding feed
    #print('Sendind data back: {0}'.format(payload))
    
    

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
miarduino = serial.Serial(port='COM3', baudrate=9600, timeout=0.1)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

client.connect()
client.loop_background()

#print('Confirmar guardado')

while True:
    if miarduino.in_waiting > 0:
        try:
            dato = miarduino.readline().decode('latin-1').strip()
            if dato:
                print(f'Dato desde Arduino: {dato}')
                modo = dato.strip().split(": ")[1] #Extraer solo el numero
                client.publish(FEED_ID_Send, modo)

        except Exception as e:
            print(f"Error al leer del puerto serial: {e}")

    time.sleep(1)

