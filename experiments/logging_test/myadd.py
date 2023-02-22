import logging

logger = logging.getLogger(__name__)

def add(a, b):
    logger.warning(f"ADD: a={str(a)}, b={str(b)}")
    return a + b