# enricher
Enricher is a Python application that acts as both Kafka consumer on one side and producer on another. Enricher consumes 
raw_good Kafka topic which already contains only events that were validated against following json schema (validation 
performed by collector: 4):

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "source": {
      "type": "string"
    },
    "artifact": {
      "type": "string"
    },
    "v_schema": {
      "type": "string"
    },
    "data": {
      "type": "object",
    }
  },
  "required": [
    "source",
    "artifact",
    "v_schema",
    "data"
  ]
}
```
Enricher application performs several functions. First,it validates the inner ```data``` object 
against it's expected schema, schema name is constructed by combining 
fields ```source```, ```artifact``` and ```v_version``` separated by ```-```. You can find schemas 
here: [Schema](https://github.com/AurimasGr/data-infrastructure-sample/blob/main/stream/integration/enricher/src/helpers/schema). 
After validation events that pass it are forwarded to ```enriched_good``` Kafka topic and the ones that failed 
validation to ```enriched_bad``` Kafka topic.

You can as well implement any data enrichment in this application.

Development mode
-
Run ```./dev_mode.sh``` to start the application in development mode, note that Kafka has to be started beforehand for 
the application to start successfully. Refer to [Project README](https://github.com/AurimasGr/data-infrastructure-sample)
on how to do that. You can investigate forvarded events by accessing Kafka web ui at http://localhost:8081

Testing
-
Run ```ci.sh``` to execute tests.

TODO
-
- ```Add poetry dependency management```
- ```Add GitHub actions for CI tests```
- ```Separate schemas of different artifacts into separate folders```
- ```investigate failing integer/float validations (see failing test)```

