# -*- coding: utf-8 -*-

import os
import random

from expects import *
from expects.aliases import above_or_equal

from infinfluxdb import factory

DATABASE = os.environ['INFLUXDB_DATABASE']

with describe('Influxdb Client'):
    with before.each:
        self.client = factory.influxdb_client()

    with after.each:
        self.client.drop_database(DATABASE)

    with describe('write point'):
        with it('writes point in database'):
            a_value = random.getrandbits(10)
            another_value = random.getrandbits(10)

            self.client.write_point('test', a=a_value, b=another_value)

            point = self.client.query('select * from test limit 1')[0]['points'][0]

            expect(point).to(contain(a_value, another_value))

    with describe('write points'):
        with it('writes points in database'):
            a_value = random.getrandbits(10)
            another_value = random.getrandbits(10)

            self.client.write_points('test', [{'value': a_value}, {'value': another_value}])

            points = self.client.query('select * from test limit 2')[0]['points']

            expect(points).to(contain(end_with(another_value), end_with(a_value)))

        with it('does not write anything if empty points list'):
            self.client.write_points('test', [])

    with describe('drop database'):
        with context('when database does not exist'):
            with it('does nothing'):
                self.client.drop_database(DATABASE)
                self.client.drop_database(DATABASE)

        with context('when database already exists'):
            with it('deletes database'):
                self.client.drop_database(DATABASE)

                expect(lambda: self.client.write_point('test', a=1, b=2)).to(raise_error)
