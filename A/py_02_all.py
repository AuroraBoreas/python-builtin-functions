import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_all():
    some_list = range(1, 10)
    some_cond = [i < 5 for i in some_list]
    result = all(some_cond)
    logging.debug(result)

if __name__ == "__main__":
    demo_all()