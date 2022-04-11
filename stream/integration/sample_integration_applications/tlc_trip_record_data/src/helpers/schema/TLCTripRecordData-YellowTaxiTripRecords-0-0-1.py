from pydantic import BaseModel


class Schema(BaseModel):

    VendorID: int
    tpep_pickup_datetime: str
    tpep_dropoff_datetime: str
    passenger_count: int
    trip_distance: float
    RatecodeID: int
    store_and_fwd_flag: str
    PULocationID: int
    DOLocationID: int
    payment_type: int
    fare_amount: float
    extra: float
    mta_tax: float
    tip_amount: float
    tolls_amount: float
    improvement_surcharge: float
    total_amount: float
    congestion_surcharge: float