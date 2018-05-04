import time, math, machine, uFirebase

db = uFirebase.uFirebase('https://micro-py.firebaseio.com')

# Caminho no banco de dados 
path = '/states'

# Definindo as portas que estão sendo utilizadas 
# Led
led = machine.PWM(machine.Pin(2), freq=1000)
# Botão
btn = machine.Pin(4, machine.Pin.IN)
# Potenciômentro
pot = machine.ADC(0)

# função para controlar os pulsos de intensidade
def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

while True:
    if(btn.value()):
        pulse(led, 1024)
        db.put(path, {'led': 'on'})
    else:
        pulse(led, 0)
        db.put(path, {'led': 'off'})

    if(btn.value()):
        pulse(led, pot.read())
        db.put(path, {'pot': pot.read()})
    else:
        pass