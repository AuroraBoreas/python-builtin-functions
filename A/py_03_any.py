import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')


def demo_any():
    some_list = list('hello world!')
    some_cond = [ord(i) > 100 for i in some_list]
    result = any(some_cond)
    logging.debug(result)

if __name__ == "__main__":
    demo_any()