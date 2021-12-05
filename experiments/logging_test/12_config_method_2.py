# Calls file.conf as the config file.

import logging
import logging.config

logging.config.fileConfig(fname='logging_test/file.conf', disable_existing_loggers=False)

# Get the logger, sampleStreamLogger, specified in the file which will print to the console.
logger = logging.getLogger('sampleStreamLogger')

logger.debug('This is a debug message')
