
# UNIVERSIDAD POLITÉCNICA DE VICTORIA (UPV)
# TERCERA UNIDAD: METODOLOGÍA DE LA PROGRAMACIÓN
# M.C. CARLOS ANTONIO TOVAR GARCIA
#
# Proyecto: CARRITO (Código MicroPython para ESP32)
# Alumnos:
#  - MAXIMILIANO ANTONIO MARTINEZ ZURITA  2530071
#  - Abraham Maximiliano Hernández Sanchez 2530454
#  - Alejandro De Leon Fonseca 2530020
#  - LUIS JESUS SANTIAGO SEGUNDO 2530120
#  - SANTIAGO JOSHUE CHAVEZ RIVERA 2530323
#
# CARRERA: INGENIERÍA EN MECATRÓNICA
# FECHA: 8/12/2025
#
# Fuente/Documento base: "CARRITO" (documento PDF aportado por el equipo).
# (Este archivo respeta y amplía la información del PDF proporcionado). :contentReference[oaicite:1]{index=1}
#
# --------------------------------------------------------------------------------
# RESUMEN EJECUTIVO
# --------------------------------------------------------------------------------
# Este archivo implementa en MicroPython el servidor web y control de motores para
# un coche robótico basado en ESP32 y driver Puente H L298N. Incluye:
#  - Configuración de pines (IN1-IN4, ENA, ENB).
#  - Control PWM para velocidad.
#  - Funciones de movimiento (adelante, atrás, izquierda, derecha, stop).
#  - Punto de acceso WiFi (AP) llamado "CarritoESP32" para control vía navegador.
#  - Servidor HTTP simple que entrega una página con botones de control.
#
# Se añaden mejoras: comprobación de pines, límites de velocidad, manejo básico de errores,
# y endpoints extra para ajustar velocidad y mostrar estado.
#
# NOTAS: Ajusta los pines a tu placa ESP32 concreta si difieren de los sugeridos en el PDF.
# Está basada en la descripciòn y esquemas presentes en el PDF. :contentReference[oaicite:2]{index=2}
#
# --------------------------------------------------------------------------------
# PRACTICE NOTES / BASICS (INSTRUCCIONES RÁPIDAS)
# --------------------------------------------------------------------------------
# 1) Flashear MicroPython en la ESP32 (descargar firmware desde micropython.org).
# 2) Subir este archivo como main.py o carrito.py (si lo subes como main.py se ejecutará al iniciar).
# 3) Conectar ESP32 y L298N con GND común. Alimentar motores por separado (6-12V) y lógica del L298N con 5V si aplica.
# 4) Abrir red WiFi "CarritoESP32" con contraseña "12345678", navegar a la IP mostrada por la ESP32 (p. ej. 192.168.4.1).
# 5) Controlar desde el navegador los botones que aparecen.
#
# Referencias y más detalles de componentes en la bibliografía del PDF. :contentReference[oaicite:3]{index=3}
#
# --------------------------------------------------------------------------------
# PROBLEMAS / VALIDACIONES (breve)
# --------------------------------------------------------------------------------
# - Validar que los pines usados existen en tu módulo ESP32.
# - No alimentar motores desde el pin 5V de la ESP32 (usar fuente externa).
# - Evitar sobrecorriente: L298N típico hasta 2A por canal; verifica consumo de motores.
#
# --------------------------------------------------------------------------------
# CÓDIGO (MicroPython) - copiar a main.py o carrito.py
# --------------------------------------------------------------------------------

import network
import socket
import time
from machine import Pin, PWM

# -----------------------------
# Configuración de pines (AJUSTAR si es necesario)
# Suggested pins según el PDF: IN1=25, IN2=26, ENA=27, IN3=18, IN4=19, ENB=23
# -----------------------------
PIN_IN1 = 25
PIN_IN2 = 26
PIN_ENA = 27  # PWM
PIN_IN3 = 18
PIN_IN4 = 19
PIN_ENB = 23  # PWM

# PWM configuration
PWM_FREQ = 1000               # frecuencia PWM recomendada
PWM_DUTY_MAX = 1023           # MicroPython duty para ESP32 (0-1023)

# Seguridad / límites
DEFAULT_SPEED = int(PWM_DUTY_MAX * 0.6)  # velocidad por defecto (60%)
MAX_ALLOWED_SPEED = PWM_DUTY_MAX

# Inicialización de pines (output)
def safe_pin_init(pin_num, mode=Pin.OUT):
    try:
        p = Pin(pin_num, mode)
        return p
    except Exception as e:
        print("Error inicializando pin", pin_num, ":", e)
        return None

in1 = safe_pin_init(PIN_IN1)
in2 = safe_pin_init(PIN_IN2)
in3 = safe_pin_init(PIN_IN3)
in4 = safe_pin_init(PIN_IN4)

# PWM pins
def safe_pwm(pin_obj, freq=PWM_FREQ):
    if pin_obj is None:
        return None
    try:
        pwm = PWM(pin_obj)
        pwm.freq(freq)
        pwm.duty(0)
        return pwm
    except Exception as e:
        print("Error inicializando PWM en pin", pin_obj, ":", e)
        return None

# Crear PWM usando las referencias de pin (transformamos el número a Pin objeto para PWM)
ena_pin_obj = safe_pin_init(PIN_ENA)
enb_pin_obj = safe_pin_init(PIN_ENB)

ena = safe_pwm(ena_pin_obj)
enb = safe_pwm(enb_pin_obj)

# Verificación básica
if None in (in1, in2, in3, in4, ena, enb):
    print("AVISO: Algún pin no fue inicializado correctamente. Revisa la configuración de pines.")
else:
    print("Pines inicializados correctamente.")

# Helpers para controlar pines con seguridad
def set_digital(pin, value):
    if pin is None:
        return
    try:
        pin.value(1 if value else 0)
    except Exception as e:
        print("Error seteando pin digital:", e)

def set_speed(pwm, speed):
    # speed entre 0 y MAX_ALLOWED_SPEED
    if pwm is None:
        return
    if speed < 0: speed = 0
    if speed > MAX_ALLOWED_SPEED: speed = MAX_ALLOWED_SPEED
    try:
        pwm.duty(int(speed))
    except Exception as e:
        print("Error asignando velocidad PWM:", e)

# Funciones de movimiento (basadas en el PDF)
def stop():
    set_digital(in1, 0)
    set_digital(in2, 0)
    set_digital(in3, 0)
    set_digital(in4, 0)
    set_speed(ena, 0)
    set_speed(enb, 0)
    print("STOP")

def adelante(speed=DEFAULT_SPEED):
    set_digital(in1, 1)
    set_digital(in2, 0)
    set_digital(in3, 1)
    set_digital(in4, 0)
    set_speed(ena, speed)
    set_speed(enb, speed)
    print("ADELANTE (speed {})".format(speed))

def atras(speed=DEFAULT_SPEED):
    set_digital(in1, 0)
    set_digital(in2, 1)
    set_digital(in3, 0)
    set_digital(in4, 1)
    set_speed(ena, speed)
    set_speed(enb, speed)
    print("ATRÁS (speed {})".format(speed))

def izquierda(speed=DEFAULT_SPEED):
    # motor izquierdo hacia atras, derecho hacia adelante
    set_digital(in1, 0)
    set_digital(in2, 1)
    set_digital(in3, 1)
    set_digital(in4, 0)
    set_speed(ena, speed)
    set_speed(enb, speed)
    print("IZQUIERDA (speed {})".format(speed))

def derecha(speed=DEFAULT_SPEED):
    # motor izquierdo adelante, derecho atrás
    set_digital(in1, 1)
    set_digital(in2, 0)
    set_digital(in3, 0)
    set_digital(in4, 1)
    set_speed(ena, speed)
    set_speed(enb, speed)
    print("DERECHA (speed {})".format(speed))

# Estado actual
current_speed = DEFAULT_SPEED
current_action = "stopped"

# --------------------------------------------------------------------------------
# WiFi AP + servidor web
# --------------------------------------------------------------------------------
AP_SSID = "CarritoESP32"
AP_PASS = "12345678"

def start_access_point():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=AP_SSID, password=AP_PASS)
    # Esperar a que el AP se levante
    for _ in range(20):
        if ap.active():
            break
        time.sleep(0.1)
    ip = ap.ifconfig()[0]
    print("Access Point activo. SSID:", AP_SSID, "IP:", ip)
    return ap, ip

ap, ip_address = start_access_point()

# HTML simple para la interfaz (puedes personalizar)
HTML_PAGE = """\
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Control Carrito ESP32</title>
  <style>
    body {{ font-family: Arial, sans-serif; text-align:center; margin-top:30px; }}
    button {{ width:140px; height:60px; margin:10px; font-size:18px; }}
    #status {{ margin-top:20px; }}
  </style>
</head>
<body>
  <h1>Control Carrito ESP32</h1>
  <div>
    <form action="/adelante"><button type="submit">Adelante</button></form>
    <form action="/atras"><button type="submit">Atrás</button></form><br>
    <form action="/izquierda"><button type="submit">Izquierda</button></form>
    <form action="/derecha"><button type="submit">Derecha</button></form><br>
    <form action="/stop"><button type="submit">Stop</button></form>
  </div>
  <div id="status">
    <p>Velocidad actual: {speed}</p>
    <p>Acción: {action}</p>
  </div>
  <div style="margin-top:20px;">
    <form action="/set_speed">
      <label>Set speed (0-{max}):</label>
      <input type="number" name="v" min="0" max="{max}" value="{speed}">
      <input type="submit" value="Set">
    </form>
  </div>
</body>
</html>
""".format(speed=current_speed, action=current_action, max=MAX_ALLOWED_SPEED)

# Servidor HTTP básico que escucha en puerto 80
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    print('Servidor HTTP escuchando en', addr)
    return s

server_socket = start_server()

# Manejo de peticiones (simple)
def handle_client(client_sock):
    try:
        request = client_sock.recv(1024)  # leer request
        if not request:
            client_sock.close()
            return
        request_str = request.decode('utf-8')
        # Extraer la primera línea
        first_line = request_str.split('\r\n')[0]
        # Ejemplo: "GET /adelante HTTP/1.1"
        parts = first_line.split(' ')
        if len(parts) < 2:
            client_sock.close()
            return
        path = parts[1]
        # Procesar query params (ej: /set_speed?v=500)
        query = ''
        if '?' in path:
            path, query = path.split('?', 1)

        global current_speed, current_action
        # Mapear rutas a funciones
        if path == '/adelante':
            adelante(current_speed)
            current_action = 'adelante'
        elif path == '/atras':
            atras(current_speed)
            current_action = 'atras'
        elif path == '/izquierda':
            izquierda(current_speed)
            current_action = 'izquierda'
        elif path == '/derecha':
            derecha(current_speed)
            current_action = 'derecha'
        elif path == '/stop':
            stop()
            current_action = 'stopped'
        elif path == '/set_speed':
            # parse query like v=123
            try:
                kv = query.split('=')
                if len(kv) == 2 and kv[0] == 'v':
                    v = int(kv[1])
                    if v < 0: v = 0
                    if v > MAX_ALLOWED_SPEED: v = MAX_ALLOWED_SPEED
                    current_speed = v
                    # aplicar a motores si ya están en movimiento
                    # si están detenidos, sólo actualiza el valor
                    if current_action == 'adelante':
                        adelante(current_speed)
                    elif current_action == 'atras':
                        atras(current_speed)
                    elif current_action == 'izquierda':
                        izquierda(current_speed)
                    elif current_action == 'derecha':
                        derecha(current_speed)
                else:
                    print("Query inválida para set_speed:", query)
            except Exception as e:
                print("Error parseando set_speed:", e)
        else:
            # ruta raíz u otra: devuelve página con estado y botones
            pass

        # Responder con HTML actualizado (status)
        response = HTML_PAGE.format(speed=current_speed, action=current_action, max=MAX_ALLOWED_SPEED)
        client_sock.send('HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n')
        client_sock.send(response)
    except Exception as e:
        print("Error manejando cliente:", e)
    finally:
        try:
            client_sock.close()
        except:
            pass

# Loop principal (bloqueante). Puedes adaptar para uso con uasyncio si prefieres.
def server_loop():
    print("Entrando al loop del servidor. Conéctate a la red WiFi '{}' con contraseña '{}' y abre http://{}/".format(AP_SSID, AP_PASS, ip_address))
    try:
        while True:
            client, addr = server_socket.accept()
            # print('cliente conectado desde', addr)
            handle_client(client)
            # pequeña espera para no saturar
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Servidor detenido por KeyboardInterrupt")
    except Exception as e:
        print("Error en server_loop:", e)
    finally:
        try:
            server_socket.close()
        except:
            pass

# Si ejecutamos este archivo directamente, levantamos el servidor
if __name__ == '__main__':
    # Inicialmente detener motores por seguridad
    stop()
    # Breve delay antes de comenzar
    time.sleep(1)
    server_loop()

# --------------------------------------------------------------------------------
# INSTRUCCIONES ADICIONALES / MEJORAS RECOMENDADAS
# --------------------------------------------------------------------------------
# - Usar un controlador de motor más moderno (ej. drivers con protección térmica o controladores MOSFET)
# - Implementar mapeo de velocidad con aceleración suave (ramp-up / ramp-down) para evitar picos.
# - Proteger la fuente de alimentación con diodos/condensadores y fusible para los motores.
# - Añadir endpoints JSON y manejo mediante fetch() para una UI más responsiva.
# - Considerar uasyncio para manejar múltiples conexiones de forma no bloqueante.
#

