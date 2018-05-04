import machine 

port = machine.Pin(4, machine.Pin.IN)


while True: 
    print('oi')
    print(port.value())