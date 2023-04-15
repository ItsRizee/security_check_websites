import socket


def check_ports(website):

    website=website[8:]
    website=website[:-1]
    open_ports = []

    for port in range(1024):
        try:
        # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout of 1 second
            s.settimeout(1)

        # Try to connect to the website on the current port
            s.connect((website, port))

        # If the connection succeeds, print a message
            open_ports.append(port)

        finally:
        # Close the socket
            s.close()

    return open_ports
