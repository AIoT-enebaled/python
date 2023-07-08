#!/usr/bin/env python3

import RPi.GPIO as GPIO  # Import the GPIO library
import os  # Import the os library
from http.server import BaseHTTPRequestHandler, HTTPServer  # Import the HTTP server classes

host_name = '10.0.0.184'  # IP Address of Raspberry Pi
host_port = 8000


def setupGPIO():
    GPIO.setmode(GPIO.BCM)  # Set the GPIO mode to BCM
    GPIO.setwarnings(False)  # Disable GPIO warnings

    GPIO.setup(18, GPIO.OUT)  # Set GPIO pin 18 as output


def getTemperature():
    temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()  # Execute a command to get the GPU temperature
    return temp


class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)  # Send a success response
        self.send_header('Content-type', 'text/html')  # Set the content type header
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)  # Send a redirect response
        self.send_header('Content-type', 'text/html')  # Set the content type header
        self.send_header('Location', path)  # Set the location header to redirect
        self.end_headers()

    def do_GET(self):
        html = '''
           <html>
           <body 
            style="width:960px; margin: 20px auto;">
           <h1>Welcome to my Raspberry Pi</h1>
           <p>Current GPU temperature is {}</p>
           <form action="/" method="POST">
               Turn LED :
               <input type="submit" name="submit" value="On">
               <input type="submit" name="submit" value="Off">
           </form>
           </body>
           </html>
        '''
        temp = getTemperature()  # Get the GPU temperature
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))  # Write the HTML response with the temperature

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])  # Get the length of the POST data
        post_data = self.rfile.read(content_length).decode("utf-8")  # Read the POST data
        post_data = post_data.split("=")[1]  # Extract the value from the POST data

        setupGPIO()

        if post_data == 'On':
            GPIO.output(18, GPIO.HIGH)  # Turn on the LED
        else:
            GPIO.output(18, GPIO.LOW)  # Turn off the LED

        print("LED is {}".format(post_data))
        self._redirect('/')  # Redirect back to the root URL


# # # # # Main # # # # #

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)  # Create an HTTP server object
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()  # Start the HTTP server and keep it running
    except KeyboardInterrupt:
        http_server.server_close()  # Close the HTTP server if interrupted by keyboard
