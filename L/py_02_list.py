import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_list():
    some_list = list('cnm world')
    # or
    other_list = [
        'c',
        'm'
    ]
    logging.debug(some_list)
    logging.debug(other_list)

if __name__ == "__main__":
    demo_list()