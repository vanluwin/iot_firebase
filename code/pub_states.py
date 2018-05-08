import machine, uFirebase

fb = uFirebase.uFirebase('https://micro-py.firebaseio.com/')

# Caminho no banco de dados 
path = 'states/'

# Definindo as portas que estão sendo utilizadas 
# Led
led = machine.PWM(machine.Pin(15))
# Botão
#btn = machine.Pin(4, machine.Pin.IN)
btn = 1
# Potenciômentro
pot = machine.ADC(0)


while True:
    if(btn):
        led.duty(1024)
        fb.put(path, {'led': 'on'})
    else:
        led.duty(0)
        fb.put(path, {'led': 'off'})

    if(btn):
        led.duty(pot.read())
        fb.put(path, {'pot': pot.read()})
    else:
        pass