import config.config as config
from kafka import KafkaProducer
import json
import os

conf = getattr(config, f'{os.environ["APP_ENV"].title()}Config')


class Producer:

    def __init__(self):

        self.producer = KafkaProducer(bootstrap_servers=conf.KAFKA_BROKER_URL,
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def produce(self, topic: str, value: str) -> None:

        self.producer.send(topic, value=value)



