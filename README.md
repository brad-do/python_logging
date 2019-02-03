# Overview
This project explores some of the Python logging features compliments of the [logging API](https://docs.python.org/3.6/library/logging.html).

## logger_example.py
This script shows how I normally use the API: I normally code my configuration right into the script.  I prefer not to do that, however.  Ideally, I'd like to be able to move my logging configuration to a properties file and role my logs, among other improvements.

## logger_cfg_example.py
This script shows how I can achieve some of those improvements.  It uses the logger_cfg_example.cfg file for the logging configuration and it turns out Python does in fact offer a [rotating file handler](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler).

# Future Considerations
Despite the nice offerings of the [logging API](https://docs.python.org/3.6/library/logging.html), people have still authored other packages like [logzero](https://logzero.readthedocs.io/en/latest/) and [loguru](https://github.com/Delgan/loguru).  Some day, I'd like to spend time looking at those packages to see what they can offer above and beyond the standard logging package.
