# batch_loader
batch_loader is a Python application that acts as a Kafka consumer. It consumes events from Kafka topic 
```enriched_good```, buffers them and writes them to local minIO instance as gziped json files.


Development mode
-
Run ```./dev_mode.sh``` to start the application in development mode, note that Kafka has to be started beforehand for 
the application to start successfully. Refer to [Project README](https://github.com/AurimasGr/data-infrastructure-sample)
on how to do that. You can investigate written files in minIO web UI: http://localhost:9090

Testing
-
Run ```ci.sh``` to execute tests.

TODO
-
- ```Add poetry dependency management```
- ```Add GitHub actions for CI tests```
- ```Add buffering per buffer size```
- ```Add tests```
- ```Add metrics```
- ```Add centralised logs```
