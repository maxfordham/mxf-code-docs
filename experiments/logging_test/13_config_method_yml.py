# Calls file.yml as the config file.

import logging
import logging.config
import yaml

with open('file.yml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Get the logger, console_logger, which will print to the console.
logger = logging.getLogger('console_logger')

logger.info('This is a debug message')