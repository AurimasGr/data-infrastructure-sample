class BaseConfig:

    TESTING = False
    DEBUG = False
    ENRICHED_GOOD_TOPIC = 'enriched_good'
    CONSUMER_GROUP_ID = 'batch_loader'
    ENABLE_CONSUMER_AUTOCOMMIT = False
    CONSUMER_AUTO_OFFSET_RESET = 'earliest'
    MINIO_OUTPUT_BUCKET = 'sample-infrastructure-project'
    MINIO_LANDING_PATH = 'data/landing'
    BUFFER_RECORD_COUNT = 5
    BUFFER_MILLISECONDS = 60000


class DevConfig(BaseConfig):

    DEBUG = True
    KAFKA_BROKER_URL = ['kafka:9092']


class ProdConfig(BaseConfig):

    KAFKA_BROKER_URL = ''


class TestConfig(BaseConfig):

    KAFKA_BROKER_URL = ['localhost:29092']
    MINIO_URL = 'localhost:9000'
    MINIO_ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE'
    MINIO_SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
