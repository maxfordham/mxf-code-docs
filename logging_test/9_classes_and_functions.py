# Logger: This is the class whose objects will be used in the application code directly to call the functions.

# LogRecord: Loggers automatically create LogRecord objects that have all the information related to the event being logged, like the name of the logger, the function, the line number, the message, and more.

# Handler: Handlers send the LogRecord to the required output destination, like the console or a file. Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.

# Formatter: This is where you specify the format of the output by specifying a string format that lists out the attributes that the output should contain.

import logging

logger = logging.getLogger('example_logger')
logger.warning('This is a warning')