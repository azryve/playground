#!/usr/bin/env python3

from tmp_out import tmpout


@tmpout
def myprint(string):
    print(string)

if __name__ == '__main__':
    myprint('TEST MY PRINT')
    print('NORMAL PRINT')
