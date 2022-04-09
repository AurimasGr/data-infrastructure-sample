# collector
Collector is a simple Flask application that acts as a backend API and accepts arbitrary json payloads on /collect endpoint.

Received payloads are validated against a predefined required schema:

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
In case of schema validation pass, the payload is enriched by adding 2 new top level fields:
- ```collector_tstamp``` - timestamp generated after validation has passed.
- ```root_id``` - uuid.

Payload is then sent to ```raw_good``` Kafka topic.

In case of schema validation fail, the payload is sent to ```raw_bad``` Kafka topic, event is reformated to contain detailed validation error:
```
{
"error": <error string>,
"payload": <json payload>
}
``` 

###Development mode

Run ```./dev_mode.sh``` to start Flask server in development mode, note that Kafka has to be started beforehand for the application to start successfully. Refer to [a link](https://github.com/AurimasGr/data-infrastructure-sample) on how to do that. After the server is started you can test it by sending json payloads to http://localhost:5050/collect you can investigate forvarded events by accessing Kafka web ui at http://localhost:8081

###Testing

Run ```ci.sh``` to execute tests. You can refer to sample producer at [...]

###TODO

- ```Add poetry dependency management```
- ```Add GitHub actions for CI tests```
- ```Separate paths for different api versions```

