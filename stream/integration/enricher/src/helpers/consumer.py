import config.config as config
from kafka import KafkaConsumer
import json
import os

conf = getattr(config, f'{os.environ["APP_ENV"].title()}Config')


class Consumer:

    def __init__(self, topic):

        self.topic = topic
        self.consumer = KafkaConsumer(self.topic,
                                      bootstrap_servers=conf.KAFKA_BROKER_URL,
                                      group_id=conf.CONSUMER_GROUP_ID,
                                      enable_auto_commit=conf.ENABLE_CONSUMER_AUTOCOMMIT,
                                      auto_offset_reset=conf.CONSUMER_AUTO_OFFSET_RESET,
                                      value_deserializer=lambda x: json.loads(x.decode('utf-8')))
