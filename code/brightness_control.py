import time, math, machine

# Definindo as portas que estão sendo utilizadas 
led = machine.PWM(machine.Pin(2), freq=1000)
pot = machine.ADC(0)
btn = machine.Pin(4, machine.Pin.IN)

# função para controlar os pulsos de intensidade
def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

while True:
    if(btn.value()):
        pulse(led, 1024)
    else:
        pulse(led, 0)

    if(btn.value()):
        pulse(led, pot.read())
    else:
        pass