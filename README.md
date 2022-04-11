# data-infrastructure-sample
This repository holds a sample data project implemented with Python. It follows architecture depicted in the diagram:

![alt text](https://github.com/AurimasGr/data-infrastructure-sample/blob/main/pictures/architecture.png?raw=true)

Currently only 2 elements have been implemented, you can find them here:

   1. Collector: [a link](https://github.com/AurimasGr/data-infrastructure-sample/blob/main/stream/integration/collector)
   2. Enricher: [a link](https://github.com/AurimasGr/data-infrastructure-sample/blob/main/stream/integration/enricher)
   3. ElasticSearchLoader: [Link pending]
   4. BatchLoader: [Link pending]
   5. DataProcessor: [Link pending]
   
In order to successfully run the two applications you will have to spin up a Kafka cluster and create
topics needed by the applications. if you haven't setup ```docker``` and ```docker-compose``` - do that. After you
have installed ```docker``` and ```docker-compose``` execute: ```docker-compose up .```. After few seconds you will 
have local Kafka cluster up and running, I also included a convenient Kafka UI through which you can easily manage your
clusters, you can access it on http://localhost:8081. You can create required topics through the following interface:

![alt text](https://github.com/AurimasGr/data-infrastructure-sample/blob/main/pictures/kafka-ui.png?raw=true)

Create 4 topics: ```raw_good```, ```raw_bad```, ```enriched_good```, ```enriched_bad```. Now feel free to test 
```collector``` and ```enricher```.

You can find a sample third party data integration application 
[here](https://github.com/AurimasGr/data-infrastructure-sample/blob/main/stream/integration/collector/sample_integration_applications/tlc_trip_record_data).

Project Description
-
The infrastructure is meant to serve as a system that allows users to collect arbitrary events from numerous sources, 
validate the events against predefined schema, perform custom defined real time enrichments (possibly ML use cases as 
well) and output the data into two destinations - ElasticSearch for real time querying and alerting and s3, minIO, GCS
or any other blob storage for further data analysis.