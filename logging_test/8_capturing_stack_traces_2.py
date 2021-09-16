import logging

a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")

# Similar to exapmle is "capturing_stack_traces_1", but using logging.exception() instead of logging.error(exc_info=True).
# Note: logging.exception() should only be called from an exception handler.

# Using logging.exception() would show a log at the level of ERROR. 
# If you don’t want that, you can call any of the other logging methods from debug() to critical() and pass the exc_info parameter as True.