#!/bin/bash
set -e

case "$1" in
    "integration-tests")
        pip install -r requirements-dev.txt
        exec mamba integration_specs
    ;;
esac
exec "$@"
