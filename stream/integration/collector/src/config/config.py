class BaseConfig:

    COLLECTOR_PATH = '/collect'
    TESTING = False
    DEBUG = False
    GOOD_TOPIC = 'raw_good'
    BAD_TOPIC = 'raw_bad'


class DevConfig(BaseConfig):

    FLASK_ENV = 'development'
    DEBUG = True
    KAFKA_BROKER_URL = ['kafka:9092']


class ProdConfig(BaseConfig):

    FLASK_ENV = 'production'
    KAFKA_BROKER_URL = ''


class TestConfig(BaseConfig):

    FLASK_ENV = 'development'
    KAFKA_BROKER_URL = ['localhost:29092']
