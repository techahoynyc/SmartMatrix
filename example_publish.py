import paho.mqtt.publish as publish

publish.single("TA/test", "display", hostname = "jane")
print("DONE")
