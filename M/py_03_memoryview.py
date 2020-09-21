import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_memoryview():
    # some_dict = dict(zip('hello', range(5)))
    # mv = memoryview(some_dict)
    # for k, v in mv.items():
    #     logging.debug(f'{k}, {v}')
    some_bytes = b'hello world'
    mv = memoryview(some_bytes)
    for i in mv:
        logging.debug(i)
    mv[0] = 101 # exception

if __name__ == "__main__":
    demo_memoryview()