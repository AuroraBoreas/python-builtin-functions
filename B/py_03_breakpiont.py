import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_breakpoint():
    for i in range(0, 100, 2):
        if i == 40:
            breakpoint()
        else:
            logging.debug(f'{i:<3}')

if __name__ == "__main__":
    demo_breakpoint()