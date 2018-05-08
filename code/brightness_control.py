import machine

# Definindo as portas que estão sendo utilizadas 
led = machine.PWM(machine.Pin(15))
pot = machine.ADC(0)
#btn = machine.Pin(4, machine.Pin.IN)
btn = 1

while True:
    if btn:
        led.duty(1024)
    else:
        led.duty(0)

    if(btn):
        led.duty(pot.read())
    else:
        pass