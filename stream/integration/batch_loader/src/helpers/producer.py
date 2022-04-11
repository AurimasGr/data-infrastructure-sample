import config.config as config
from datetime import datetime
from minio import Minio
from minio.error import S3Error
import os
import gzip
import json
import pytz

conf = getattr(config, f'{os.environ["APP_ENV"].title()}Config')


class Producer:

    def __init__(self, consumer, logger):

        self.records = list()
        self.producer = Minio(
            endpoint=conf.MINIO_URL,
            access_key=conf.MINIO_ACCESS_KEY,
            secret_key=conf.MINIO_SECRET_KEY,
            secure=False
        )
        self.init_time = datetime.now()
        self.consumer = consumer
        self.logger = logger

    def produce(self) -> None:

        try:
            json_bytes = f'{json.dumps(self.records)}\n'.encode('utf-8')
            with gzip.open("tmp_file.gzip", "w") as f:
                f.write(json_bytes)
            self.producer.fput_object(conf.MINIO_OUTPUT_BUCKET,
                                      f"{conf.MINIO_LANDING_PATH}/enriched_good_{datetime.now(tz=pytz.UTC).strftime('%Y_%m_%d_%H_%M_%S_%f')}.gz",
                                      "tmp_file.gzip")
            os.remove("tmp_file.gzip")
        except S3Error as e:
            print(e)

    def put_event(self, event: dict) -> None:

        self.records.append(event)

        if (len(self.records) >= conf.BUFFER_RECORD_COUNT) | ((datetime.now() - self.init_time).total_seconds() * 1000 >= conf.BUFFER_MILLISECONDS):
            self.produce()
            self.logger.info(f'{len(self.records)} events written.')
            self.records = list()
            self.init_time = datetime.now()
            self.consumer.commit()

