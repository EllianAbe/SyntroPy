import cProfile
import time


def iter_stopwatch(iterations=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()

            result = [func(*args, **kwargs) for i in range(iterations)]

            mean_time = (time.time() - start) / iterations

            print(f'{func.__name__} took {mean_time:.2f} seconds')

            return result
        return wrapper
    return decorator


# declaration

def stopwatch(func):
    def wrapper(*args, **kwargs):
        # before func is called
        start = time.time()

        # func call
        result = func(*args, **kwargs)

        # after func is called
        elapsed_time = time.time() - start

        print(f'{func.__name__} took {elapsed_time:.2f} seconds')

        return result
    return wrapper

# usage


@stopwatch
def my_function(args):
    pass


def profile(func):

    def wrapper(*args, **kwargs):

        profiler = cProfile.Profile()
        profiler.enable()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.disable()

        print('         Function: ', func.__name__ + str(args)),
        profiler.print_stats()
        print('-' * 100)

        return result
    return wrapper
