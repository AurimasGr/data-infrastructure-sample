class BaseConfig:

    TESTING = False
    DEBUG = False
    COLLECTOR_PATH = '/collect'


class DevConfig(BaseConfig):

    DEBUG = True
    COLLECTOR_URL = f'http://localhost:5000'


class ProdConfig(BaseConfig):

    ...


class TestConfig(BaseConfig):

    COLLECTOR_URL = f'http://localhost:5000'
