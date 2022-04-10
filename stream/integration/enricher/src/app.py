from helpers.validator import SchemaValidator
from helpers.producer import Producer
from helpers.consumer import Consumer
import config.logger as logger
import config.config as config
import os

conf = getattr(config, f'{os.environ["APP_ENV"].title()}Config')

logger = logger.setup_logger()
producer = Producer()
consumer = Consumer(conf.GOOD_TOPIC).consumer


def process_consumed_event(event: dict) -> None:

    try:
        data = event
        schema_combination = {'source': data.get('source'),
                              'artifact': data.get('artifact'),
                              'v_schema': data.get('v_schema')}
        validation_output = SchemaValidator(data.get('data'), schema_combination).validation_output

        if validation_output.get('status'):
            producer.produce(topic=conf.ENRICHED_GOOD_TOPIC, value=data)
            print(f"data sent to good")
        else:
            producer.produce(topic=conf.ENRICHED_BAD_TOPIC, value={'error': validation_output.get('error'),
                                                                   'payload': data})
            print(f"data sent to bad")

    except:
        logger.error(f'Failed to process payload')


def main(consumer):

    for message in consumer:
        process_consumed_event(message.value)


if __name__ == "__main__":

    main(consumer)
