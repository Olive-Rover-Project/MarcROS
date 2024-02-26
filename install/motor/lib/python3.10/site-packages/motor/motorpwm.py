import RPi.GPIO as GPIO
from time import sleep


def main():
    print('Hi from motor.')
    motor1 = 12
    motor2 = 13
    
    int1 = 20
    int2 = 21
    
    predir = 0
    
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(int1,GPIO.OUT)
    GPIO.setup(int2,GPIO.OUT)
    #GPIO.setup(int3,GPIO.OUT)
    #GPIO.setup(int4,GPIO.OUT)
    
    GPIO.output(int1, GPIO.LOW)
    GPIO.output(int2, GPIO.LOW)
    
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
    	
    	direction = int(input("Direction of Motor 1: "))
    	
    	
    	if direction == 1 and predir == 0:
    	
    	
    		GPIO.output(int1, GPIO.LOW)
    		GPIO.output(int2, GPIO.LOW)
    		
    		sleep(0.1)
    	
    	
    		GPIO.output(int1, GPIO.HIGH)
    		GPIO.output(int2, GPIO.LOW)
    		
    		predir = 1;
    		
    	if direction == 0 and predir == 1:
    	
    		GPIO.output(int1, GPIO.LOW)
    		GPIO.output(int2, GPIO.LOW)
    		
    		sleep(0.1)
    		
    		
    		GPIO.output(int1, GPIO.LOW)
    		GPIO.output(int2, GPIO.HIGH)
    		
    		predir = 0;
    		
    	
    	



if __name__ == '__main__':
    main()
