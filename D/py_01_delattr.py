import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class Foo:
    name = 'foo'
    age  = 35
    sex  = 'unknown'


def demo_delattr():
    """docs
    
    This is a relative of setattr().

    The arguments are an object and a string. 
    The string must be the name of one of the object’s attributes. 
    The function deletes the named attribute, provided the object allows it. 
    
    For example, delattr(x, 'foobar') is equivalent to del x.foobar.
    
    Table: del vs delattr
    +-----------+-------------------+
    | del       | more efficient    |
    +-----------+-------------------+
    | delattr   | more dynamic      |
    +-----------+-------------------+
    
    """
    f = Foo()
    logging.debug(f.name)
    # delattr(f, 'name') # not instance of attr, but a class's..
    delattr(Foo, 'name')
    logging.debug(f.name) # exception

if __name__ == "__main__":
    demo_delattr()