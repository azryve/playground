#!/usr/bin/env bash

CURDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SCRIPT=`echo $* | sed s#$CURDIR/## | sed s#^#/playground/#`
docker run --rm -v $CURDIR:/playground playground $SCRIPT
