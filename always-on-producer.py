import numpy as np
import pandas as pd
import datetime as dt
from confluent_kafka import Producer, Consumer, OFFSET_BEGINNING, TopicPartition
import yaml
import json
import time
import os


def delivery_callback(err, msg):
    if err:
        print('ERROR: Message failed delivery: {}'.format(err))
    else:
        print("Produced event: {value}".format(value=(json.loads(msg.value().decode('utf-8')))))


if __name__ == '__main__':

    config_path = os.path.join(os.getcwd(), 'config.yml')
    with open(config_path) as f:
        config = yaml.load(f, yaml.Loader)

    topic = config['topic']

    producer = Producer({'bootstrap.servers': config['kafka_addr']})

    # produce event every n seconds
    while True:
        timestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
        data = {'timestamp': timestamp}
        producer.produce(topic, json.dumps(data), 'data', callback=delivery_callback)

        # TODO: what is this
        producer.poll(1000)
        producer.flush()

        time.sleep(2)
