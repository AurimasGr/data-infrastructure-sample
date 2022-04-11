from helpers.producer import Producer
from helpers.consumer import Consumer
import config.logger as logger
import config.config as config
import os

conf = getattr(config, f'{os.environ["APP_ENV"].title()}Config')

logger = logger.setup_logger()
consumer = Consumer(conf.ENRICHED_GOOD_TOPIC).consumer
producer = Producer(consumer)


def main(producer, consumer):

    for message in consumer:
        producer.put_event(message.value)


if __name__ == "__main__":

    main(producer, consumer)
