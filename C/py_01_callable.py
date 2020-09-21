import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class MyClass:
    def __call__(self):
        return

class OtherClass:
    pass

def demo_callable():
    """docs

    Return True if the object argument appears callable, False if not. 

    If this returns True, it is still possible that a call fails, 
    but if it is False, calling object will never succeed. 

    Note that classes are callable (calling a class returns a new instance); 
    instances are callable if their class has a __call__() method.
    """
    mc = MyClass()
    oc = OtherClass()
    r1 = callable(mc)
    r2 = callable(oc)
    logging.debug(r1)
    logging.debug(r2)


if __name__ == "__main__":
    demo_callable()