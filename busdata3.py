# Kafka Producer for topic testBusData

from pykafka import KafkaClient
import json
from datetime import datetime
import uuid
import time

# Kafka Producer
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['geodata_final']
producer = topic.get_sync_producer()


#######################################
#    Read Coordinates from GEOJSON    #
#######################################

route1_input_file = open('./data/GMU-BUS-ROUTE1.json')
route1_json_array = json.load(route1_input_file)
route1_coordinates = route1_json_array['features'][2]['geometry']['coordinates']



def generate_uuid():
    """
    Generate Unique ID for message
    :return: uuid
    """
    return uuid.uuid4()


#######################
#    Build Message    #
#######################

data = {}
data['busline'] = '00003'

def generate_checkpoint(coordinates):
    """
    Generate Checkpoint Message to be used to sent to kafka stream
    :param coordinates: the list of coordinates on route
    :return: message for kafka
    """
    i = 0
    while i < len(coordinates):

        data['key'] = data['busline'] + '_' + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude'] = coordinates[i][1]
        data['longitude'] = coordinates[i][0]

        # Create message for Kafka
        message = json.dumps(data)
        # Semd Message to Kafka
        producer.produce(message.encode('ascii'))
        # print(message)
        time.sleep(2)

        if i == len(coordinates) - 1:
            i = 0
        else:
            i += 1

    # for i in range(len(coordinates)):
    #
    #     data['key'] = data['busline'] + '_' + str(generate_uuid())
    #     data['timestamp'] = str(datetime.utcnow())
    #     data['latitude'] = coordinates[i][1]
    #     data['longitude'] = coordinates[i][0]
    #
    #     # Create message for Kafka
    #     message = json.dumps(data)
    #     # Semd Message to Kafka
    #     producer.produce(message.encode('ascii'))
    #     print(message)
    #
    # print(data)


###########################
#    Calling Generator    #
###########################

generate_checkpoint(route1_coordinates)

