import paho.mqtt.client as mqtt

pub_client=mqtt.Client()
pub_client.connect('broker.hivemq.com',1883)
print('Server Connected')

pub_client.publish('b18','Hello batch members')


