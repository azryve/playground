#!/bin/sh

docker rmi -f playground
docker build -t playground .
