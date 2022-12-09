import paho.mqtt.client as paho
import time

# Callback function
#def on_connect(client,userdata,flags, rc):
#    print ("Connected!, result code:", str(rc))
#    client.subscribe ()

class MQTT:
    message = "------------------------------\nTesting MQTT Server in Python.\n------------------------------"
    broker="184.72.120.107"
    port=1883
    topic = "test/mqtt"

    def __init__ (self, client_name, on_message_callback=0):
        self.client= paho.Client(client_name)             #create client object
        #print ("Init object", self.client)
        self.client.on_message = on_message_callback
        self.client.connect(self.broker,self.port)                    #establish connection




    def subscribe (self):
        self.client.loop_start ()
        self.client.subscribe(self.topic)           #publish message
        print ("Subscribed and connected! Waiting for request...")
        time.sleep (100)
        self.client.loop_stop ()

    def publish (self, msg):
        print ("Prepare to publish request...\n")
        ret= self.client.publish(self.topic, msg)           #publish message
def on_publish(client,userdata,result):
    print("Request published successfully! \n")
    pass

