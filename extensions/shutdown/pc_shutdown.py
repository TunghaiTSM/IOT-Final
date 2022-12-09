from os import system
from time import sleep
from plyer import notification
from time import sleep
from mqtt import MQTT



def shutdown(client, userdata, result):
    print("Request received! \n")
    notification.notify(
            title="怪叔叔",
            message="系統即將關閉",
            )
    sleep(1)
    for i in range(5,0,-1):
        notification.notify(
                title="system shutdown in "+str(i),
                message=""
                )
        sleep(1)

    #system("shutdown -P now")
    pass

# Driver code
client = MQTT("PC", shutdown)
client.subscribe()
