class BaseConfig:

    TESTING = False
    DEBUG = False
    GOOD_TOPIC = 'raw_good'
    ENRICHED_GOOD_TOPIC = 'enriched_good'
    ENRICHED_BAD_TOPIC = 'enriched_bad'
    CONSUMER_GROUP_ID = 'enricher_6'
    ENABLE_CONSUMER_AUTOCOMMIT = True
    CONSUMER_AUTO_OFFSET_RESET = 'earliest'


class DevConfig(BaseConfig):

    DEBUG = True
    KAFKA_BROKER_URL = ['kafka:9092']


class ProdConfig(BaseConfig):

    KAFKA_BROKER_URL = ''


class TestConfig(BaseConfig):

    KAFKA_BROKER_URL = ['localhost:29092']
