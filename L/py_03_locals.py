import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_locals():
    a = 'nmgb'
    b = 'cnm'
    c = 'nmsl'
    logging.debug(locals())
    
if __name__ == "__main__":
    demo_locals()