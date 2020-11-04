# Kafka Producer for topic testBusData

from pykafka import KafkaClient
import asyncio

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

route_input_file = open('./data/GMU-BUS-ROUTE1.json')
route_json_array = json.load(route_input_file)

route1_coordinates = route_json_array['features'][0]['geometry']['coordinates']
route2_coordinates = route_json_array['features'][1]['geometry']['coordinates']
route3_coordinates = route_json_array['features'][2]['geometry']['coordinates']



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

async def generate_checkpoint(coordinates, bus_num=1):
    """
    Generate Checkpoint Message to be used to sent to kafka stream
    :param coordinates: the list of coordinates on route
    :return: message for kafka
    """
    i = 0
    while i < len(coordinates):

        data['busline'] = bus_num
        data['key'] = str(data['busline']) + '_' + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude'] = coordinates[i][1]
        data['longitude'] = coordinates[i][0]

        # Create message for Kafka
        message = json.dumps(data)

        # Send Message to Kafka
        producer.produce(message.encode('ascii'))

        await asyncio.sleep(2)

        # TODO: Change to be based off of real length
        if i == len(coordinates) - 1:
            i = 0
        else:
            i += 1


async def main():

    await asyncio.wait([
                        generate_checkpoint(route1_coordinates, 1),
                        generate_checkpoint(route2_coordinates, 2),
                        generate_checkpoint(route3_coordinates, 3)
                       ])


###########################
#    Calling Generator    #
###########################


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(main())
event_loop.close()
