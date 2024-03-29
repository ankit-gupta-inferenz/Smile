from kafka import KafkaProducer
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def callProducer(data):
    producer = KafkaProducer(
        #    security_protocol="SSL", 
        bootstrap_servers=["b-1.smilemsk.sbp07d.c2.kafka.me-south-1.amazonaws.com:9092"], value_serializer=json_serializer
    )   
    # log_data = generate_logs()

    producer.send("SmileTestTopic", data)
