#!/usr/bin/env python3

import logging
import time
import urllib.request
import urllib.error
import http.client
from concurrent import futures

logging.basicConfig(level=logging.DEBUG)


def get_code(url):
    try:
        with urllib.request.urlopen(url, timeout=0.5) as gethandle:
                return gethandle.getcode()
    except urllib.error.URLError as e:
        logging.warning(str(e))


def host_ok(host):
    if get_code(host) == http.client.OK:
        return True
    else:
        return False


def test_host(host):
    if host_ok(host):
        return "%s OK" % host
    else:
        return "%s FAILED" % host


if __name__ == '__main__':
    hosts = ['https://ya.ru', 'https://google.ru']
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        try:
            while True:
                fut = dict(
                    ((executor.submit(test_host, h), h) for h in hosts)
                )
                for f in futures.as_completed(fut):
                    logging.debug(f.result())
                time.sleep(1)
        except KeyboardInterrupt:
            pass
