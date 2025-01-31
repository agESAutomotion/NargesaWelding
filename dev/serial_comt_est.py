import serial
import time

# Set up the serial connection (adjust 'COM3' to match your Arduino's port)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for the connection to initialize

def send_and_receive(byte_value):
    if 0 <= byte_value <= 255:  # Ensure the value is a valid byte
        # Send the byte to the Arduino
        arduino.write(bytearray([byte_value]))
        print(f"Sent byte: {byte_value}")
        
        # Wait for a response
        time.sleep(0.1)  # Allow Arduino some time to process and respond
        response = arduino.read()  # Read one byte from the Arduino
        
        if response:
            print(f"Received byte: {response[0]}")
        else:
            print("No response received.")
    else:
        print("Invalid byte value. Must be between 0 and 255.")

try:
    while True:
        # Ask the user for a byte value to send
        byte_value = int(input("Enter a byte value (0-255): "))
        send_and_receive(byte_value)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    arduino.close()
