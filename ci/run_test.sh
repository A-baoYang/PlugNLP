#! /bin/bash -xe

pytest --cov=./ --cov-report=term --cov-report=html .
rm -rf FiNER