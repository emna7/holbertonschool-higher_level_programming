#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return(fct(*args))
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return(None)
