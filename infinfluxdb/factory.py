# -*- coding: utf-8 -*-

import os

from infinfluxdb import client


def influxdb_client():
    return client.InfluxDBClient(
        os.environ['INFLUXDB_HOST'],
        os.environ['INFLUXDB_PORT'],
        os.environ['INFLUXDB_USERNAME'],
        os.environ['INFLUXDB_PASSWORD'],
        os.environ['INFLUXDB_DATABASE'],
        os.environ.get('INFLUXDB_SSL') != 'false'
    )
