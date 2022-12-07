import boto3
import json
class SendMail:
    def __init__(self):
        self.client = boto3.client('sns')

    def pubish(self,msg):
        response = self.client.publish(
            default_msg = { '嘿嘿' : "哇嗚" },
            TargetArn = "arn:aws:sns:us-east-1:999698209796:IOT_DHT11",
            Message=json.dump({'default':json.dump(default_msg),
                                        'email':msg}),
            Subject = 'IOT-Final',
            MessageStructure='json'
        )