
import RPi.GPIO as GPIO
import time


class ServoPWM():

    def __init__(self, pin):
        #Ajuste estes valores para obter o intervalo completo do movimento do servo
        deg_0_pulse   = 0.5
        deg_180_pulse = 2.0
        f = 25
import RPi.GPIO as GPIO
import time


class ServoPWM():

    def __init__(self, pin):
        #Ajuste estes valores para obter o intervalo completo do movimento do servo
        deg_0_pulse   = 0.5
        deg_180_pulse = 2.0
        f = 25
        
        # Faca alguns calculos dos parametros da largura do pulso
        period = 1000/f
        k      = 100/period
        self.deg_0_duty = deg_0_pulse * k
        pulse_range = deg_180_pulse - deg_0_pulse
        self.duty_range = pulse_range * k
        
        #Iniciar o pino gpio
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)
        self.pwm = GPIO.PWM(pin,f)
        self.pwm.start(0)

    def set_angle(self, angle):
        duty = self.deg_0_duty + (angle/180.0)* self.duty_range
        self.pwm.ChangeDutyCycle(duty)

class Led():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        

    def on(self):
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)


    def off(self):
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        
        # Faca alguns calculos dos parametros da largura do pulso
        period = 1000/f
        k      = 100/period
        self.deg_0_duty = deg_0_pulse * k
        pulse_range = deg_180_pulse - deg_0_pulse
        self.duty_range = pulse_range * k
        
        #Iniciar o pino gpio
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)
        self.pwm = GPIO.PWM(pin,f)
        self.pwm.start(0)

    def set_angle(self, angle):
        duty = self.deg_0_duty + (angle/180.0)* self.duty_range
        self.pwm.ChangeDutyCycle(duty)

class Led():

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        

    def on(self):
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)


    def off(self):
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)