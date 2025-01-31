import serial
import threading
from serial.rs485 import RS485Settings

def forward_data4(source, destination):
    """Reads data from source and forwards it to destination."""
    while True:
        try:
            data = source.read(source.in_waiting or 1)  # Read available data or block for 1 byte
            if data:
                destination.write(data)
                print(f"COM4: {data.hex()}")  # Optional: Log forwarded data
        except Exception as e:
            print(f"Error in forwarding data: {e}")
            break

def forward_data5(source, destination):
    """Reads data from source and forwards it to destination."""
    while True:
        try:
            data = source.read(source.in_waiting or 1)  # Read available data or block for 1 byte
            if data:
                destination.write(data)
                print(f"COM5: {data.hex()}")  # Optional: Log forwarded data
        except Exception as e:
            print(f"Error in forwarding data: {e}")
            break

def main():
    try:
        # Configure the first serial port
        port1 = serial.Serial(
            port='COM4',  # Update to your first RS485 port
            baudrate=115200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=0.1
        )
        # port1.rs485_mode = RS485Settings(
        #     rts_level_for_tx=True,  # Set RTS high during transmission
        #     rts_level_for_rx=False,  # Set RTS low during reception
        #     delay_before_tx=None,
        #     delay_before_rx=None
        # )
        # Configure the second serial port
        port2 = serial.Serial(
            port='COM5',  # Update to your second RS485 port
            baudrate=115200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=0.1
        )
        # port2.rs485_mode = RS485Settings(
        #     rts_level_for_tx=True,  # Set RTS high during transmission
        #     rts_level_for_rx=False,  # Set RTS low during reception
        #     delay_before_tx=None,
        #     delay_before_rx=None
        # )
        print("Ports opened successfully.")
        print("Forwarding data between ports.")

        # Create threads for bi-directional communication
        thread1 = threading.Thread(target=forward_data4, args=(port1, port2), daemon=True)
        thread2 = threading.Thread(target=forward_data5, args=(port2, port1), daemon=True)

        thread1.start()
        thread2.start()

        # Keep the main thread alive
        while True:
            pass

    except serial.SerialException as e:
        print(f"Serial port error: {e}")
    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()
