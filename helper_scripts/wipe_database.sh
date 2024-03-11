#!/bin/bash

cd ".." || exit
rm -r pgdata
docker-compose down
docker-compose up -d
sleep 35
pipenv run python manage.py migrate
