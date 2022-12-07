import boto3
import json
import botocore
class SendMail:
    TargetARN = "arn:aws:sns:us-east-1:999698209796:IOT_DHT11"
    def __init__(self):
        self.client = boto3.client('sns')

    def publish(self,msg):
        default_msg = {"嗚嗚":"啊啊"}
        response = self.client.publish( TargetArn = self.TargetARN, Message=json.dumps({ "default":json.dumps(default_msg), "email":msg }), Subject = "IOT-Final", MessageStructure="json")

#SendMail().publish("石頭：你頭皮屑好多")
