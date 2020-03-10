# Smart RGB Matrix
Followed this tutorial for the intial set up: https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/driving-matrices


# Parts: 
RPI Bonnet https://www.adafruit.com/product/3211


# How to make it work
`pip install -r requirements.txt` for additional python packages (paho-MQTT, linkedlist)_
Run `sudo python3 client_runtext.py`_
On another raspberry pi or python-enabled wifi device, run `python3 example_publish.py`, which will publish a message to the matrix. The Matrix has a default display "Welcome to Techahoy." 


