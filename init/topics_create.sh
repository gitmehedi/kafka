#!/bin/bash

/kafka/kafka/bin/kafka-topics.sh --zookeeper localhost:2182 --create --topic cassandra --partitions 10 --replication-factor 3
