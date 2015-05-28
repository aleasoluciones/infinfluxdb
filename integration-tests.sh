#!/bin/bash -x

docker-compose -f docker-compose-test.yml pull
docker-compose -f docker-compose-test.yml build
docker-compose -f docker-compose-test.yml run --rm -T tests
RC=$?
docker-compose -f docker-compose-test.yml stop
docker-compose -f docker-compose-test.yml rm -f
exit $RC
