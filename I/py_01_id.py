import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_id():
    a = [
        i for i in range(10, 15)
    ]
    
    b = 10
    logging.debug(id(a))
    logging.debug(id(b))

if __name__ == "__main__":
    demo_id()