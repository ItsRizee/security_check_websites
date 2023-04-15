
import socket

website = "https://www.google.com/"
ports = [80, 443]

for port in ports:
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout of 1 second
        s.settimeout(1)

        # Try to connect to the website on the current port
        s.connect((website, port))

        # If the connection succeeds, print a message
        print(f"{website}:{port} is open")

    except Exception as e:
        # If an error occurs, print the error message
        print(f"{website}:{port} is closed: {e}")

    finally:
        # Close the socket
        s.close()