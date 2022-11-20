# pizza-faker-stream-with-kafka-and-python
This is for learning purpose only. Credit doesn't belong to me

For more detail go to full version code on github [aiven/python-fake-data-producer-for-apache-kafka](https://github.com/aiven/python-fake-data-producer-for-apache-kafka.git) and [Create your own data stream for Apache Kafka® with Python and Faker](https://aiven.io/blog/create-your-own-data-stream-for-kafka-with-python-and-faker)

## Note:
- Turn on "Decode from base64" on **Message** to recive decode message
### Before run:
- Download all three: the **Access Key** as *service.key*, the **Access Certificate** as *service.key*, the **CA Certificate** as *ca.pem* and put those in folder name "kafkaCerts" 
- Use **Service URI** (usually in the form <INSTANCE_NAME>-<PROJECT_NAME>.aivencloud.come:<PORT>) as *my_server*
- More detail on [blog]((https://aiven.io/blog/create-your-own-data-stream-for-kafka-with-python-and-faker)
### Bugs:
- If the error "NoBrokerAvaible" shows up, there would be some potential things you could notice:
1. The string of my_server should have f as a prefix, examaple: f"<INSTANCE_NAME>-<PROJECT_NAME>.aivencloud.come:<PORT>"
