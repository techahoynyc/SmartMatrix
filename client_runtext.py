#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
from datetime import datetime as dt
import paho.mqtt.client as mqtt
import os
from pyllist import sllist, sllistnode

commands = sllist([])

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("TA/test")
    client.subscribe("TA/topic")
 
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    #print(message)
    commands.appendright(message)

 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("jane", 1883, 60)

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../Matrix_Support_Files/fonts/10x20.bdf")
        #textColor = graphics.Color(32, 178, 178)
        textColor = graphics.Color(46,139,87)
        default_string = "Welcome to TechAhoy"
        pos = offscreen_canvas.width 
        
        while True:
            if len(commands) > 0:
                #print(commands)
                cmd = commands.popleft()
                endtime = time.time() + 1 * 10
                while time.time() < endtime:
                    #print(commands)
                    offscreen_canvas.Clear()
                    length = graphics.DrawText(offscreen_canvas, font, pos, 22, textColor, cmd)
                    pos -= 1
                    if (pos + length < 0):
                        pos = offscreen_canvas.width
                    time.sleep(0.05)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            else:                
                endtime = time.time() + 1 * 1
                while time.time() < endtime:
                    #print(commands)
                    offscreen_canvas.Clear()
                    length = graphics.DrawText(offscreen_canvas, font, pos, 22, textColor, default_string)
                    pos -= 1
                    if (pos + length < 0):
                        pos = offscreen_canvas.width
                    time.sleep(0.05)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            

# Main function
if __name__ == "__main__":
    client.loop_start()
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
    
