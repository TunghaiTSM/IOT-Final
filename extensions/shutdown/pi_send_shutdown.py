from mqtt import MQTT

class Shutdown:

    def now ():
        client = MQTT ("PI")
        client.publish ("TEST")
