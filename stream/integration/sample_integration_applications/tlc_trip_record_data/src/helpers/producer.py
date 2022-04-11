import config.config as config
import requests
import json
import os

conf = getattr(config, f'{os.environ["APP_ENV"].title()}Config')


class Producer:

    def __init__(self):

        ...

    def produce(self, value: dict) -> requests.Response:

        json_header = {'Content-Type': 'application/json'}
        url = f'{conf.COLLECTOR_URL}{conf.COLLECTOR_PATH}'

        response = requests.post(url, data=json.dumps(value), headers=json_header)

        return response



