# Calls file.conf as the config file.

import logging
import logging.config

logging.config.fileConfig(fname='logging_test/file.conf', disable_existing_loggers=False)

# In the config file we define the keys for the logger, handler, and formatter.
# So under [loggers] we have the key "sampleLogger". 
# In the same file we then define the configuration for the logger under [logger_sampleLogger].
# This is the same for handlers. Under [handlers] we have the key "consoleHandler".
# Then under [handler_consoleHandler] we define the configuration.

# Get the logger, sampleFileLogger, specified in the file.
# This logger we have configured will save to the file test.log.
logger = logging.getLogger('sampleFileLogger')

logger.debug('This is a debug message')

# Note: A root logger must be defined in the config file, file.conf.
# See source here: https://github.com/python/cpython/blob/main/Lib/logging/config.py#L185