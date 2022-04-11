# tlc_trip_record_data_producer
tlc_trip_record_data_producer is a Python cli application that downloads data from
[NYC TLC website](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page), transforms it into suitable
format for [Collector](https://github.com/AurimasGr/data-infrastructure-sample/blob/main/stream/integration/collector)
and sends it to a dedicated endpoint.


Development mode
-
Run ```./dev_mode.sh``` to start the application in development mode, note that 
[Collector](https://github.com/AurimasGr/data-infrastructure-sample/blob/main/stream/integration/collector) has 
to be started beforehand for the application to be able to send events successfully. 
Refer to [Project README](https://github.com/AurimasGr/data-infrastructure-sample) 
on how to do that. After the server is started you can test it by sending json payloads to http://localhost:5050/collect 
you can investigate forvarded events by accessing Kafka web ui at http://localhost:8081

Testing
-
Run ```ci.sh``` to execute tests.

TODO
-
- ```Add poetry dependency management```
- ```Add GitHub actions for CI tests```
- ```Implement other NYC TLC dataset integrations```
- ```Implement tests```
- ```Add metrics```
- ```Add centralised logs```

