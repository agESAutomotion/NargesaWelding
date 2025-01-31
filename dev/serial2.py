import serial
import threading
import time

# Configure the serial ports (adjust 'COM4' and 'COM5' as needed)
port1 = serial.Serial(port='COM6', baudrate=115200, timeout=1)  # Port 1
port2 = serial.Serial(port='COM7', baudrate=115200, timeout=1)  # Port 2
time.sleep(2)  # Allow time for serial connections to initialize

def forward_data(source, destination, source_name, destination_name):
    """
    Listens to the source port and forwards data to the destination port.

    :param source: Source serial port object.
    :param destination: Destination serial port object.
    :param source_name: Name of the source port (for display purposes).
    :param destination_name: Name of the destination port (for display purposes).
    """
    while True:
        if source.in_waiting > 0:  # Check if data is available on the source port
            data = source.read(source.in_waiting)  # Read all available data
            print(f"Received from {source_name}: {data}")
            destination.write(data)  # Forward data to the destination port
            print(f"Forwarded to {destination_name}: {data}")

# Create threads for forwarding in both directions
thread1 = threading.Thread(target=forward_data, args=(port1, port2, "COM4", "COM5"))
thread2 = threading.Thread(target=forward_data, args=(port2, port1, "COM5", "COM4"))

# Start the threads
thread1.start()
thread2.start()

print("START")
try:
    while True:
        time.sleep(1)  # Keep the main thread alive
except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Close serial ports on exit
    port1.close()
    port2.close()
