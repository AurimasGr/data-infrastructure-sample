SCHEMA = {
    'VendorID': {'type': 'float', 'required': True},
    'tpep_pickup_datetime': {'type': 'string', 'required': True},
    'tpep_dropoff_datetime': {'type': 'string', 'required': True},
    'passenger_count': {'type': 'float', 'required': True},
    'trip_distance': {'type': 'float', 'required': True},
    'RatecodeID': {'type': 'float', 'required': True},
    'store_and_fwd_flag': {'type': 'string', 'required': True},
    'PULocationID': {'type': 'integer', 'required': True},
    'DOLocationID': {'type': 'integer', 'required': True},
    'payment_type': {'type': 'float', 'required': True},
    'fare_amount': {'type': 'float', 'required': True},
    'extra': {'type': 'float', 'required': True},
    'mta_tax': {'type': 'float', 'required': True},
    'tip_amount': {'type': 'float', 'required': True},
    'tolls_amount': {'type': 'float', 'required': True},
    'improvement_surcharge': {'type': 'float', 'required': True},
    'total_amount': {'type': 'float', 'required': True},
    'congestion_surcharge': {'type': 'float', 'required': True}
}