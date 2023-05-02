# Research Kafka

## Quick How To

Create `.env` file in the save level of docker-compose.yml with this configuration.

Set this to the server IP when deploy this to DigitalOcean.

```bash
SERVER_IP=localhost
```

```bash
docker compose up -d
```

## Tutorial

This code base on Confluent's Tutorial

Kafka docker: [Apache Kafka and Python - Getting Started Tutorial](https://developer.confluent.io/get-started/python/#introduction)

- How to add config in docker-compose.yml
  - [Docker Configuration Parameters for Confluent Platform | Confluent Documentation](https://docs.confluent.io/platform/current/installation/docker/config-reference.html)
  - `KAFKA_LOG_RETENTION_MINUTES: 2`

## Resources to learn Kafka

- Confluent
  - https://www.confluent.io/blog/kafka-listeners-explained/
  - https://developer.confluent.io/
  - https://developer.confluent.io/get-started/python/
  - Kafka book - https://www.confluent.io/resources/kafka-the-definitive-guide-v2/
  - https://www.confluent.io/learn/extract-transform-load/
  - https://docs.confluent.io/platform/current/clients/index.html
- Apache Kafka: https://kafka.apache.org/
- Conduktor
  - https://www.conduktor.io/kafka/what-is-apache-kafka/
