from flask import Flask, request
from helpers.processor import Processor
from helpers.validator import SchemaValidator
from helpers.producer import Producer
import config.logger as logger
import config.config as config
import os

logger = logger.setup_logger()
producer = Producer()
conf = getattr(config, f'{os.environ["APP_ENV"].title()}Config')


def process_collected_event(event: dict) -> None:

    try:
        raw_data = event
        validation_output = SchemaValidator(raw_data).validation_output
        if validation_output.get('status'):
            data = Processor(request.get_json()).processed_event
            producer.produce(topic=conf.GOOD_TOPIC, value=data)
        else:
            producer.produce(topic=conf.BAD_TOPIC, value={'error': validation_output.get('error'),
                                                          'payload': raw_data})
    finally:
        logger.error(f'Failed to process payload')


def create_app():

    logger.info(f'Starting app in {os.environ["APP_ENV"]} environment')
    app = Flask(__name__)
    app.config.from_object('config')

    @app.route(conf.COLLECTOR_PATH, methods=['POST'])
    def write_data() -> str:

        process_collected_event(request.get_json())

        return ""

    return app


app = create_app()


if __name__ == "__main__":

    app.run(host='0.0.0.0', debug=True)
