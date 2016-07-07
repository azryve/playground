#!/usr/bin/env python3

import sys
import time
import logging
import tempfile
from subprocess import Popen, PIPE

logging.basicConfig(level=logging.DEBUG)


def timing(foo):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        ret = foo(*args, **kwargs)
        finish = time.perf_counter()
        logging.debug("%s run for %s seconds\n" % (foo.__name__, finish - start))
        return ret
    return wrapper


def myiter():
    _max = 10
    counter = 0
    while True:
        if counter > _max:
            break
        c = counter
        counter += 1
        yield c
        time.sleep(0.2)


class myiterclass:
    _max = 10

    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > myiterclass._max:
            raise StopIteration
        c = self.counter
        self.counter += 1
        return c


class BigFile:
    def __init__(self, size):
        self._file = tempfile.NamedTemporaryFile(buffering=0)
        self._file.file.seek(size)


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return out


b1 = BigFile(10000)
print(b1._file.name)
b1._file.file.write(b'1')
sys.stdin.read()
