# -*- coding: utf-8 -*-

import influxdb.influxdb08 as influxdb


class InfluxDBClient(object):
    def __init__(self, host, port, username, password, database, ssl):
        self._client = influxdb.InfluxDBClient(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            ssl=ssl,
            verify_ssl=ssl
        )

        self._create_database(database)

    def write_point(self, name, **kwargs):
        self._client.write_points([{
            "name": name,
            "columns": kwargs.keys(),
            "points": [
                kwargs.values()
            ]
        }])

    def write_points(self, name, args):
        if len(args) == 0:
            return

        columns = args[0].keys()
        points = [p.values() for p in args]
        self._client.write_points([{
            "name": name,
            "columns": columns,
            "points": points
        }])

    def query(self, query):
        return self._client.query(query)

    def _create_database(self, name):
        if not self._database_exists(name):
            self._client.create_database(name)

    def drop_database(self, name):
        if self._database_exists(name):
            self._client.delete_database(name)

    def _database_exists(self, name):
        for db in self._client.get_list_database():
            if db['name'] == name:
                return True

        return False
