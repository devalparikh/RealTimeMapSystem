RealTimeMapSystem

### Microservices
![System Design](https://github.com/devalparikh/RealTimeMapSystem/blob/master/RTBusSystemDesign.png?raw=true)

### Dependencies
- Java 8
- Kafka
- Zookeeper
- Python3
- Flask

### Servers
- `Zookeeper` => `http://localhost:2181/`
    - Starting Zookeeper `./zookeeper-server-start.sh {insert pwd of kafka_{version}/config/zookeeper.properties}`
    - Example of starting Zookeeper `zookeeper-server-start.sh /Users/devalparikh/Documents/Development/Kafka/kafka_2.13-2.6.0/config/zookeeper.properties`
- `Kafka` => `http://localhost:9092/`
    - Starting Kafka `./kafka-server-start.sh {insert pwd of kafka_{version}/config/server.properties}`
    - Example of starting Kafka `kafka-server-start.sh /Users/devalparikh/Documents/Development/Kafka/kafka_2.13-2.6.0/config/server.properties`
    - Create Kafka Topic `kafka-topics.sh --zookeeper 0.0.0.0:2181 --topic test_topic --create --partitions 1 --replication-factor 1`
    - Info about the Kafka Topic `kafka-topics.sh --zookeeper 0.0.0.0:2181 --topic test_topic --describe`
    - Create Kafka Producer `kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic`
    - Create Kafka Consumer `kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic test-topic --partition 0`

- `Flask` => `http://localhost:5000/`
    - `FLASK_APP=app.py flask run`

### Environment Setup

- Initialize Kafka
    1. Java 8 installed
    2. Download Kafka 
    3. Add Kafka bin folder to env PATH
    4. Create a folder inside of Kafka dir called `data`
    5. Create two folders inside of `data`. One `kafka` folder and one `zookeeper` folder.
    6. Copy pwd `zookeeper`
    7. Inside `kafka_{version}/config/zookeeper.properties` paste for the value of dataDir={paste in here}
    8. Copy pwd of the newly created `kafka` dir
    9. Inside `kafka_{version}/config/server.properties` paste for the value of log.dirs={paste in here}
