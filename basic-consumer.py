import numpy as np
import pandas as pd
import datetime as dt
from confluent_kafka import Producer, Consumer, OFFSET_BEGINNING, TopicPartition
import yaml
import json
import time
import os

if __name__ == '__main__':

    config_path = os.path.join(os.getcwd(), 'config.yml')
    with open(config_path) as f:
        config = yaml.load(f, yaml.Loader)

    topic = config['topic']
    group_id = config['consumer']['group_id']

    consumer = Consumer({'bootstrap.servers': config['kafka_addr'], 'group.id': group_id})
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                print('Waiting...')
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                json_data = json.loads(msg.value().decode('utf-8'))
                print(json_data)

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()