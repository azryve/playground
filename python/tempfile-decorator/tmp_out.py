import sys
from tempfile import NamedTemporaryFile


def tmpout(foo):
    def wrapper(*args, **kwargs):
        out = NamedTemporaryFile(mode='w+', prefix="stdout.", delete=False)
        err = NamedTemporaryFile(mode='w+', prefix="stderr.", delete=False)
        realout = sys.stdout
        realerr = sys.stderr
        sys.stdout = out.file
        sys.stderr = err.file
        ret = foo(*args, **kwargs)
        sys.stdout = realout
        sys.stderr = realerr
        out.close()
        err.close()
        return ret
    return wrapper
