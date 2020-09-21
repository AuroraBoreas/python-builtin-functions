import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_sum():
    some_list = [
        1, 2, 3, 4
    ]
    r = sum(some_list)
    logging.debug(r)

if __name__ == "__main__":
    demo_sum()