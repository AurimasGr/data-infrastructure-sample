from helpers.processor import Processor
from helpers.validator import SchemaValidator
from helpers.producer import Producer
import requests
import pandas as pd
import time
import config.logger as logger
import argparse


SOURCE_URL = "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv"
DATA_DIR = "data"
DESTINATION = f"{DATA_DIR}/yellow.csv"

logger = logger.setup_logger()
producer = Producer()


def download_file(source: str, target: str) -> None:

    data = requests.get(source)
    with open(target, 'wb')as file:
        file.write(data.content)


def load_pandas(source: str) -> pd.DataFrame:

    df = pd.read_csv(source)

    return df


def main(sleep_time: float, max_record_count: int, download: int) -> None:

    if download == 1:
        download_file(SOURCE_URL, DESTINATION)

    logger.debug('data downloaded.')
    yellow_df = load_pandas(DESTINATION)

    if max_record_count == 0:
        max_record_count = len(yellow_df)

    record_counter = 0

    top_level_fields = {'source': 'TLCTripRecordData',
                        'artifact': 'YellowTaxiTripRecords',
                        'v_schema': '0-0-1'}

    for index, row in yellow_df.iterrows():

        try:
            validation_output = SchemaValidator(row.to_dict(), top_level_fields).validation_output
            if validation_output.get('status'):
                processed_event = Processor(event=validation_output.get('data').dict(),
                                            top_level_fields=top_level_fields).processed_event
                producer.produce(processed_event)
                logger.debug('event sent.')
            else:
                logger.error(validation_output.get('error').json())
        except:
            logger.error(f'Failed to process payload')

        record_counter += 1
        time.sleep(sleep_time)

        if record_counter >= max_record_count:
            break


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Runs producer which writes TLCTripRecordData to collector endpoint")
    parser.add_argument('-s', '--sleep_time', required=False, default='1')
    parser.add_argument('-m', '--max_record_count', required=False, default='1000')
    parser.add_argument('-d', '--download', required=False, default='1')
    args = parser.parse_args()

    logger.info(f'Starting sample producer (TLCTripRecordData) with {args.sleep_time} s between sending records')

    main(float(args.sleep_time), int(args.max_record_count), int(args.download))
