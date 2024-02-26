import RPi.GPIO as GPIO
from time import sleep


def main():
    print('Hi from motor.')
    motor1 = 12
    motor2 = 13
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor1,GPIO.OUT)
    pwm1 = GPIO.PWM(motor1,100)
    pwm1.start(0)
    
    GPIO.setup(motor2,GPIO.OUT)
    pwm2 = GPIO.PWM(motor2,100)
    pwm2.start(0)
    
    while True:
    	duty1 = int(input("Speed of Motor 1: "))
    	pwm1.ChangeDutyCycle(duty1)
    	
    	duty2 = int(input("Speed of Motor 2: "))
    	pwm2.ChangeDutyCycle(duty2)



if __name__ == '__main__':
    main()
