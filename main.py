import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from websocket_server import WebsocketServer
import threading  # For running the WebSocket server in a separate thread

# DHT11 sensor's DATA pin
DHT_PIN = 27  # DHT11 sensor's DATA pin

# GPIO configuration
GPIO.setmode(GPIO.BCM)

# WebSocket server setup
server = WebsocketServer(port=8000, host='0.0.0.0')

# Functions for when a client connects or disconnects
def client_connected(client, server):
    print(f"Client connected: {client['id']}")

def client_disconnected(client, server):
    print(f"Client disconnected: {client['id']}")

# Function to send messages to all WebSocket clients
def send_message_to_all(message):
    server.send_message_to_all(message)

# Setting up the WebSocket server functions
server.set_fn_new_client(client_connected)
server.set_fn_client_left(client_disconnected)

# Function to run the WebSocket server in a separate thread
def run_server():
    server.run_forever()

# Start the WebSocket server in a new thread
threading.Thread(target=run_server, daemon=True).start()

print("DHT11 sensor monitoring...")

try:
    while True:
        # Reading data from DHT11
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)

        if humidity is not None and temperature is not None:
            # Send temperature and humidity as separate messages
            temperature_message = f'Temperature: {temperature:.1f} °C'
            humidity_message = f'Humidity: {humidity:.1f} %'
            send_message_to_all(temperature_message)  # Send temperature data
            send_message_to_all(humidity_message)     # Send humidity data
        else:
            error_message = 'Error reading from DHT11 sensor.'
            send_message_to_all(error_message)

        time.sleep(10)  # Wait for 10 seconds before reading again

except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    GPIO.cleanup()  # Clean up GPIO configuration
