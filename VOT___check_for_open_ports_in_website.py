import socket

def check_ports(website):
    # Function to check which ports are open on a given website
    website = website[8:]
    website = website[:-1]
    open_ports = []

    for port in range(1024):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set a timeout of 1 second
            s.settimeout(1)

            # Try to connect to the website on the current port
            s.connect((website, port))

            # If the connection succeeds, add the port to the list of open ports
            open_ports.append(port)

        except Exception as e:
           pass

        finally:
            # Close the socket
            s.close()

    return open_ports

def main():
    # Main function to run the check_ports() function
    website = "https://www.google.com/"
    open_ports = check_ports(website)
    if len(open_ports) > 0:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
