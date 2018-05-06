import machine 

port = machine.Pin(4, machine.Pin.IN)


while True: 
    print(port.value())