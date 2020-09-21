import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_hex():
    some_list = [
        8,
        16,
        32,
        512
    ]
    for i in some_list:
        r = hex(i)
        logging.debug(f'hex({i}) = {r}')

if __name__ == "__main__":
    demo_hex()