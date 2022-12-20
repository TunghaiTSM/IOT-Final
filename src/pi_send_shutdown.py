from mqtt import MQTT

class Shutdown:

    def now (self):
        client = MQTT ("PI")
        client.publish ("TEST")

#Shutdown ().now ()
