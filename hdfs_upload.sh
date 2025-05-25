#!/bin/bash
hadoop fs -mkdir -p /user/retail
hadoop fs -put -f data/OnlineRetail.csv /user/retail/
echo "Data uploaded to HDFS /user/retail/"
