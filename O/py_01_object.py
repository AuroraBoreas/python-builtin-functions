import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_object():
    """docs

    Return a new featureless object. object is a base for all classes. 
    It has the methods that are common to all instances of Python classes. 
    This function does not accept any arguments.

    Note object does not have a __dict__, so you can’t assign arbitrary attributes to an instance of the object class.
    """
    o = object()
    logging.debug(o)
    logging.debug(dir(o))

if __name__ == "__main__":
    demo_object()