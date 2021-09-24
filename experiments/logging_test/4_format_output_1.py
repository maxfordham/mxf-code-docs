import logging

# Logging process ID, the severity level, and the message.
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')