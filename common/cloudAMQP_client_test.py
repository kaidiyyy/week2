from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = 'amqp://ocaqmidw:rR6cCqSfiClEoTP7qCXlV7zuQ0nT1u5i@wombat.rmq.cloudamqp.com/ocaqmidw'

QUEUE_NAME = 'test_queue'



client = CloudAMQPClient(CLOUDAMQP_URL, QUEUE_NAME)

"""# Send a message
client.sendDataFetcherTask({'name' : 'test message'})"""

#Receive a message
client.getDataFetcherTask()