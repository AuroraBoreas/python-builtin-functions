import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_eval():
    a = '5 + 5'
    r = eval(a)
    logging.debug(r)

if __name__ == "__main__":
    demo_eval()