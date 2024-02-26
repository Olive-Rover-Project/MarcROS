import serial
from serial import Serial


def main():

    X_Acc = 0
    Y_Acc = 0
    Z_Acc = 0
    X_G = 0
    Y_G = 0
    Z_G = 0
    
    print('Hi from sensors.')
    
    ser = serial.Serial('/dev/ttyS0',9600)
    while True:
    	x = ser.readline(1000)
    	
    	if x[0] == 88:
    		if x[1] == 65:
    			X_Acc = (x[2:len(x)-1])
    			
    	if x[0] == 88:
    		if x[1] == 71:
    			X_G = (x[2:len(x)-1])	
    			
    	
    	
    	
    	
    	if x[0] == 89:
    		if x[1] == 65:
    			Y_Acc = (x[2:len(x)-1])
    	if x[0] == 89:
    		if x[1] == 71:
    			Y_G = (x[2:len(x)-1])
    			
    			
    			
    			
    			
    	if x[0] == 90:
    		if x[1] == 65:
    			Z_Acc = (x[2:len(x)-1])
    			
    	if x[0] == 90:
    		if x[1] == 71:
    			Z_G = (x[2:len(x)-1])	
    			
    			
    	print("XA = ") 
    	print(X_Acc) 
    	print("\t") 
    	
    	print("YA = ") 
    	print(Y_Acc) 
    	print("\t") 
    	
    	print("ZA = ") 
    	print(Z_Acc) 
    	print("\t") 
    	
    	print("XG = ") 
    	print(X_G) 
    	print("\t") 
    	
    	print("YG = ") 
    	print(Y_G) 
    	print("\t") 
    	
    	print("ZG = ") 
    	print(Z_G) 
    	print("\n") 
    	
    	
    	
    	
    	
    
if __name__ == '__main__':
    main()
