FROM python:2.7.9-onbuild
MAINTAINER Jaime Gil de Sagredo <jgil@alea-soluciones.com>

RUN python setup.py develop

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
