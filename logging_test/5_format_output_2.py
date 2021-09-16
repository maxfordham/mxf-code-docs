import logging

# %(asctime)s adds the time of creation of the LogRecord
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')