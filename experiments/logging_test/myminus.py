import logging
import yaml

with open('file.yml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

def minus(a, b):
    logger.warning(f"MINUS: a={str(a)}, b={str(b)}")
    return a + b