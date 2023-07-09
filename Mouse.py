import serial
from pynput.mouse import Button, Controller

# Initialize mouse
mouse = Controller()

try:
  
  # Setting Serial port number and baudrate
  ser = serial.Serial('COM5',baudrate = 9600)       

  while 1:                                            
      # Reading Serial Port
      dump = ser.readline()                           
      # Converting the data to string
      dump = str(dump)
      # print(dump)                           
      # Removing output that is not needed.
      dump = dump[2:-5]                         
      # Spiliting the data with the key and the location to move.
      data = dump.split(',')
      print(data)
      
      # Checking the key, and then performing the required action as per the key.
      if data[0] == "DataToMove":                          
        # Moving the mouse cursor the amount of units as received from data. We have to convert the reading to int also.
        mouse.move(int(data[1]), int(data[2]))
        
      # If the key is DATAB, it means either the left or right button has been clicked in our mouse.
      if data[0] == "DATAB":   
            # When left button is pressed  
            if data[1] == 'L' :                    
              # we first press the left button and then release it to simulate a click   
              mouse.press(Button.left)                
              mouse.release(Button.left)
            # When right button is pressed
            if data[1] == 'R' :
              # we first press the left button and then release it to simulate a click 
              mouse.press(Button.right)         
              mouse.release(Button.right)
# Incase of any errors, when the mouse couldn't be found, or it is disconnected, or the serial monitor is running at some other place, we throw the exception.
except:
  print("Mouse not found or is disconnected.")
  k=input("Press any key to exit.")