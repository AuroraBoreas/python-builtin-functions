import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

def demo_ascii():
    """docs

    As repr(), return a string containing a printable representation of an object, 
    but escape the non-ASCII characters in the string returned by repr() using \\x, \\u or \\U escapes
    """
    some_string = "hello 三季人cnm, je m'en foo complétement, くそ野郎"
    result = ascii(some_string)
    logging.debug(result)
    

if __name__ == "__main__":
    demo_ascii()