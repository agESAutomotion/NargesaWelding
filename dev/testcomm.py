import serial
import time

# Configure serial ports (adjust COM4 and COM5 as needed)
serial_out = serial.Serial(port='COM4', baudrate=9600, timeout=1)  # For sending
serial_in = serial.Serial(port='COM5', baudrate=9600, timeout=1)   # For receiving
time.sleep(2)  # Allow time for the serial connections to initialize

def send_and_receive(data_to_send, num_bytes_to_receive):
    """
    Sends data over COM4 and receives data over COM5.

    :param data_to_send: A list of bytes to send (e.g., [0x01, 0x02, 0x03]).
    :param num_bytes_to_receive: Number of bytes expected to receive.
    :return: A list of received bytes.
    """
    # Send the data
    serial_out.write(bytearray(data_to_send))
    print(f"Sent bytes: {data_to_send}")
    
    # Wait and read the response
    time.sleep(0.1)  # Adjust delay if needed
    received_data = serial_in.read(num_bytes_to_receive)
    
    # Convert received data to a list of byte values
    received_bytes = list(received_data)
    print(f"Received bytes: {received_bytes}")
    return received_bytes

# Example usage
try:
    while True:
        # Input data to send
        data_to_send = input("Enter bytes to send (comma-separated, e.g., 1,2,3): ")
        data_to_send = [int(x.strip()) for x in data_to_send.split(",")]
        
        # Input expected number of bytes to receive
        num_bytes_to_receive = int(input("Enter the number of bytes to receive: "))
        
        # Perform send and receive
        send_and_receive(data_to_send, num_bytes_to_receive)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Close serial ports
    serial_out.close()
    serial_in.close()
