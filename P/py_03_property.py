import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class Cnm:
    def __init__(self):
        self._voltage = 100_000
    @property
    def voltage(self):
        return self._voltage

def demo_property():
    """docs
    
    @property as dec
    """

    c = Cnm()
    v = c.voltage
    logging.debug(v)

if __name__ == "__main__":
    demo_property()