from functools import wraps
from time import time


def timed_args(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Finished {} with args: {} in {}'.format(f, args, end-start))
        return result
    return wrapper




def timed(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Finished {} in {}'.format(f,  end-start))
        return result
    return wrapper
