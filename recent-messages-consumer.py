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
            p = TopicPartition(topic, 0)
            low_offset, high_offset = consumer.get_watermark_offsets(p)

            n_messages = 10

            offset = high_offset - n_messages

            # handle offset out of range
            if offset < low_offset:
                offset = low_offset
                n_messages = high_offset - low_offset

            print(f"low, high ({low_offset}, {high_offset}) offset={offset}, n={n_messages}")

            # consume last messages
            # set start position and consume
            consumer.assign([TopicPartition(topic, 0, offset)])
            messages = consumer.consume(n_messages, timeout=2)

            # decode messages
            all_messages = []
            for m in messages:
                all_messages += [json.loads(m.value().decode('utf-8'))]

            if len(all_messages) > 0:
                df = pd.DataFrame(all_messages)
                print(df)
            else:
                df = pd.DataFrame()

            # polling every n second
            # manually set
            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()