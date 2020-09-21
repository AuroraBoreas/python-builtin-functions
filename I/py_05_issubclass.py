import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class Cnm:
    pass

class Reflect(Cnm):
    pass

class Omit(Reflect):
    pass

class Fight(Omit):
    pass

def demo_issubclass():
    r = issubclass(Fight, Cnm)
    logging.debug(r)

if __name__ == "__main__":
    demo_issubclass()