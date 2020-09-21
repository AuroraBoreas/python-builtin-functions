import random
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def run_many_times(n):
    def dec(f):
        def inner(*args, **kwargs):
            logging.debug(f'run {n} times, results are:')
            for _ in range(n):
                f(*args, **kwargs)
        return inner
    return dec

@run_many_times(random.randint(5, 10))
def demo_filter():
    some_list = [
        random.randint(10, 100)
        for _ in range(5)
    ]
    r = filter(lambda x: x > 50, some_list)
    logging.debug(list(r))

if __name__ == "__main__":
    demo_filter()