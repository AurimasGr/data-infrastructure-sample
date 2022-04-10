from helpers.validator import SchemaValidator
import pytest


@pytest.mark.parametrize("pass_validation", [
    {
        "source": "TLCTripRecordData",
        "artifact": "YellowTaxiTripRecords",
        "v_schema": "0-0-1",
        "data": {
            "VendorID": 1,
            "tpep_pickup_datetime": "2021-01-01 00:39:16",
            "tpep_dropoff_datetime": "2021-01-01 01:00:13",
            "passenger_count": 1,
            "trip_distance": 9.1,
            "RatecodeID": 1,
            "store_and_fwd_flag": "N",
            "PULocationID": 97,
            "DOLocationID": 129,
            "payment_type": 4,
            "fare_amount": 27.5,
            "extra": 0.5,
            "mta_tax": 0.5,
            "tip_amount": 0,
            "tolls_amount": 0,
            "improvement_surcharge": 0.3,
            "total_amount": 28.8,
            "congestion_surcharge": 0
        },
        "collector_tstamp": "2022-04-09 10:24:46 +0000",
        "root_id": "a57cd289-a368-4361-84ae-433bd8ca6bcd"
    }
])
def test_validator_pass(pass_validation):

    assert SchemaValidator(pass_validation.get('data'), {'source': pass_validation.get('source'),
                                                         'artifact': pass_validation.get('artifact'),
                                                         'v_schema': pass_validation.get('v_schema')}).validation_output.get('status')


@pytest.mark.parametrize("fail_validation", [
    {
        "source": "TLCTripRecordData",
        "artifact": "YellowTaxiTripRecords",
        "v_schema": "0-0-1",
        "data": {
            "VendorID": 1,
            "tpep_pickup_datetime": "2021-01-01 00:39:16",
            "tpep_dropoff_datetime": "2021-01-01 01:00:13",
            "passenger_count": 1,
            "trip_distance": 9.1,
            "RatecodeID": 1,
            "store_and_fwd_flag": "N",
            "PULocationID": 97,
            "DOLocationID": "some string",
            "payment_type": 4,
            "fare_amount": 27.5,
            "extra": 0.5,
            "mta_tax": 0.5,
            "tip_amount": 0,
            "tolls_amount": 0,
            "improvement_surcharge": 0.3,
            "total_amount": 28.8,
            "congestion_surcharge": 0
        },
        "collector_tstamp": "2022-04-09 10:24:46 +0000",
        "root_id": "a57cd289-a368-4361-84ae-433bd8ca6bcd"
    },
    {
        "source": "TLCTripRecordData",
        "artifact": "YellowTaxiTripRecords",
        "v_schema": "0-0-1",
        "data": {
            "VendorID": int(1),
            "tpep_pickup_datetime": "2021-01-01 00:39:16",
            "tpep_dropoff_datetime": "2021-01-01 01:00:13",
            "passenger_count": 1,
            "trip_distance": 9.1,
            "RatecodeID": 1,
            "store_and_fwd_flag": "N",
            "PULocationID": 97,
            "DOLocationID": 129,
            "payment_type": 4,
            "fare_amount": 27.5,
            "extra": 0.5,
            "mta_tax": 0.5,
            "tip_amount": 0,
            "tolls_amount": 0,
            "improvement_surcharge": 0.3,
            "total_amount": 28.8,
            "congestion_surcharge": 0
        },
        "collector_tstamp": "2022-04-09 10:24:46 +0000",
        "root_id": "a57cd289-a368-4361-84ae-433bd8ca6bcd"
    }
])
def test_validator_fail(fail_validation):

    assert not SchemaValidator(fail_validation.get('data'), {'source': fail_validation.get('source'),
                                                             'artifact': fail_validation.get('artifact'),
                                                             'v_schema': fail_validation.get('v_schema')}).validation_output.get('status')
