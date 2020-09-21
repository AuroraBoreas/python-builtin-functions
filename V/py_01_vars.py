import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class MyClass:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def __dir__(self):
        return [self.args, self.kwargs]


def demo_vars():
    """docs

    Return the __dict__ attribute for a module, class, instance, 
    or any other object with a __dict__ attribute.

    Without an argument, vars() acts like locals(). 
    
    Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored.
    """
    mc = MyClass(1, 2, 3, hello='world', cnm='haoma')
    r = vars(mc)
    logging.debug(r)

if __name__ == "__main__":
    demo_vars()