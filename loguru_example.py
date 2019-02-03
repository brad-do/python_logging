#!/usr/bin/env python
__author__ = 'brad'
"""
Example using the loguru package in Python
"""

def do_something():
    pass
    

def main(argv):
    logging.info('Starting a new instance of the logger_example.py script', extra={'log_id': log_id})
    do_something()
    logging.info('The logger_example.py script is now complete', extra={'log_id': log_id})


if __name__ == '__main__':
    main(sys.argv[1:])
