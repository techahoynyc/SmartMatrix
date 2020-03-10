# Smart RGB Matrix
This matrix utilizes the MQTT protocol to display scrolling messages.
We followed this tutorial for the intial set up of the pi with the matrix: https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/driving-matrices I recommend checking out the python example code to get a feel for how the images or the text is displayed. Our current set up is coded for a 32x128 matrix (two 32x64 matricies). Here are the docs for paho-MQTT: https://pypi.org/project/paho-mqtt/#client Note that there is also a C++ library for paho-MQTT here: https://github.com/eclipse/paho.mqtt.cpp


# Parts: 
RPI Bonnet https://www.adafruit.com/product/3211


# How to make it work
## Step 1
Replace "jane" from line #29 of client_runtext.py with the MQTT broker on your local area network or "mqtt.eclipse.org", which can be used for development 
## Step 2
Run `pip install -r requirements.txt` for additional python packages (paho-MQTT, linkedlist)
## Step 3 
Run `sudo python3 client_runtext.py`
## Step 4
On another raspberry pi or python-enabled wifi device, run `python3 example_publish.py`, which will publish a message to the matrix. The Matrix has a default display "Welcome to Techahoy." 


