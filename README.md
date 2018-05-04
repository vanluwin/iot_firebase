# Oficina de IOT com Firebase :fire:

## MicroPython

MicroPython é uma implementação enxuta e eficiente da linguagem de programção Python 3 que inclui um pequeno subconjunto da biblioteca padrão do Python e é otimizada para rodar em microcontroladores e ambientes restritos.

### Instalação 

O jeito mais facil é utilizando o [esptool.py](https://github.com/espressif/esptool) para lidar com as tarefas de manipulação de firmware

1. Primeiro apague o flash

    ```bash
        sudo python esptool.py --port /dev/ttyUSB0 erase_flash
    ```
2. Carregue o firmware (RENOMEIE PARA SUA VERSÃO)

    ```bash 
        sudo python esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-2016-07-10-v1.8.2.bin
    ```

3. Testando tudo 

    Use o [screen](https://www.cyberciti.biz/faq/unix-linux-apple-osx-bsd-screen-set-baud-rate/) no linux e o [puTTy](https://www.putty.org/) no windows

    Instalando o screen:

    ```bash
        sudo apt-get install screen
    ```

    Utilizando o screen:

    ```bash
        screen /dev/ttyUSB0 115200
    ```

## Ampy

Ampy é uma ferramenta da Adafruit para carregar e rodar códigos em uma placa com MicroPython, sendo uma utilitario de linha de comando multiplataforma fornece muitas funcionalidades de acesso ao sistema de arquivos do MicroPython sem ser muito complexa.

## Instalação 

```bash
    pip install adafruit-ampy
```

Verificando a instalação:

```bash
    ampy --help
```


## Firebase
O Firebase hoje, após a aquisição do Google, virou uma plataforma muito completa para se desenvolver aplicações. Podendo ser integrado em vários pontos partes da sua aplicação.

Uma característica interessante dessa plataforma para o desenvolvimento de aplicações IOT é o **Firebase Realtime Database** que armazena dados na forma de árvores ou documentos JSON é os distribui em tempo real para todos os dispositivos conectados.

Para prosseguir com o tutorial crie uma conta no [firebase](https://firebase.google.com/) e um inicie um projeto no console do firebase com o nome que desejar.

**Uma vez no console do projeto:**

Precisaremos de algumas informações do console para a configuração do dispositivo IOT e da aplicação Web:

1. Clique em 'Adicionar o Firebase ao seu aplicativo da Web', será mostrado as informações de seu projeto precisaremos do'databaseURL' futuramente.
2. Vá para a seção Database.
3. Clique em primeiros passos com o Realtime Database.
4. Inicie no modo de teste ( não será necessário estar autenticado para ler e escrever no bando de dados).


## Utilizando os exemplos 

1. Hello World

    [Código](https://github.com/vanluwin/iot_firebase/blob/master/code/hello_world.py)

    Executando o código no ESP:

    ```bash
        ampy --port /serial/port run hello_wolrd.py
    ```


2. Blink

    [Código](https://github.com/vanluwin/iot_firebase/blob/master/code/led_blink.py)

    Executando o código no ESP:

    ```bash
        ampy --port /serial/port run led_blink.py
    ```

3. Publicando dados no :fire: **Firebase** :fire:

    Utilizaremos a biblioteca [uFirebase](https://github.com/TiagoGIM/ufirebaseESP8266) desenvolvida pelo [Tiago Hérique](https://github.com/TiagoGIM)

    [Código](https://github.com/vanluwin/iot_firebase/blob/master/code/fb_data.py)

    Executando o código no ESP:

    ```bash
        ampy --port /serial/port run fb_data.py
    ```

4. Controle de brilho 

    [Código](https://github.com/vanluwin/iot_firebase/blob/master/code/brightness_control.py)

    Executando o código no ESP:

    ```bash
        ampy --port /serial/port run brightness_control.py
    ```

5. Publicando estados no Firebase:

    [Código](https://github.com/vanluwin/iot_firebase/blob/master/code/pub_states.py)

    Executando o código no ESP:

    ```bash
        ampy --port /serial/port run pub_states.py
    ```
    

