import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def owner(name, email, group):
    """Print the owner/author of this class. """
    def decorator_owner(cls):
        @functools.wraps(cls)
        def wrapper_owner(*args, **kwargs):
            value = cls(*args, **kwargs)
            # log the info or do something with it
            print(f'Owner of {cls.__name__}: {name}, {email}, {group}')
            return value
        return wrapper_owner
    return decorator_owner


@owner(name='carlos', email='carlos@qap.dev', group='QAP')
class TestSuite:

    @timer
    def check_one(self):
        time.sleep(5)


if __name__ == '__main__':
    TestSuite().check_one()
