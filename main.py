from urllib.parse import urlparse
from flask import Flask, request, render_template
import socket
import requests

app = Flask(__name__)


def checkEncryption(url):
    response = requests.get(url)
    if response.status_code == 200:
        if response.url.startswith("https://"):
            return "The access is encrypted"
        else:
            return "The access is unencrypted"
    else:
        return "Couldn't access the website."


def extract_host(url):
    parsed_url = urlparse(url)
    host = parsed_url.hostname
    return host


def check_ports(url):
    # Function to check which ports are open on a given website

    website = extract_host(url)
    open_ports = []

    for port in range(1024):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set a timeout of 1 second
            s.settimeout(1)

            # Try to connect to the website on the current port
            s.connect((url, port))

            # If the connection succeeds, add the port to the list of open ports
            open_ports.append(f"{website}:{port} is open")

        except Exception as e:
            pass

        finally:
            # Close the socket
            s.close()

    if open_ports.__len__() == 0:
        open_ports.append("No open ports found.")

    return open_ports


@app.route('/', methods=['GET', 'POST'])
def submit_form():
    result = []
    if request.method == 'POST':
        url = request.form['inputText']
        if url != '':
            result = check_ports(url)
            result.append(checkEncryption(url))
    else:
        result = []
    return render_template('home.html', result=result)


if __name__ == '__main__':
    app.run()

# https://ambient-stone-383715.lm.r.appspot.com/
