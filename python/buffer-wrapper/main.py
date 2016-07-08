#!/usr/bin/env python3


def buffering(size):
    def decorator(foo):
        def wrapper(*args, **kwargs):
            buf = list()
            for elem in foo(*args, **kwargs):
                if len(buf) < size:
                    buf.append(elem)
                    continue
                for elem in buf:
                    yield elem
                buf = list()
            for elem in buf:
                yield elem
        return wrapper
    return decorator


@buffering(10)
def myrange(start, finish):
    return range(start, finish)


if __name__ == '__main__':
    for i in myrange(1, 11):
        print(i)
