#!/usr/bin/env python
__author__ = 'brad'
"""
Example using the logging package in Python
"""

import sys
import logging
import logging.config
import uuid
import os
import random

current_dir = os.path.dirname(os.path.realpath(__file__))
log_id = str(uuid.uuid4())[-12:]
extra = {'log_id': log_id}
logging.config.fileConfig('logger_cfg_example.cfg')
random_msgs = ['OHHHH…. I give up Core dumped', 'Keyboard not present, press any key', \
               'Man the Lifeboats! Women and children first!', 'That makes 100 errors; please try again.', \
               'Maybe you should try asking a human?', 'very funny', 'Now deleting all files. Goodbye', \
               'Out of order', 'minor alarm', 'Invalid Error', 'The impossible has happened!', 'Mysterious Error -nnn']


def do_something():
    logging.debug('this is a degug statement', extra=extra)
    logging.info('Did something', extra=extra)
    for i in range(0, 50):
        logging.info(random_msgs[random.randint(0, len(random_msgs)-1)], extra=extra)


def main(argv):
    logging.info('Starting a new instance of the logger_example.py script', extra=extra)
    do_something()
    logging.info('The logger_example.py script is now complete', extra=extra)


if __name__ == '__main__':
    main(sys.argv[1:])
