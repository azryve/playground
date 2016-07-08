#!/usr/bin/env python3

import tracemalloc

tracemalloc.start()

def foo():
	return None


def gen():
	yield None


if __name__ == '__main__':
	foobuf = list()
	genbuf = list()
	snap1 = tracemalloc.take_snapshot()
	for i in range(1, 100000):
		genbuf.append(gen())
		genbuf.append(foo())
	snap2 = tracemalloc.take_snapshot()
	for stat in snap2.compare_to(snap1, 'lineno'):
		print(stat)
