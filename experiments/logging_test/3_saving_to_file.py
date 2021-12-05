import logging

logging.basicConfig(filename='logging_test/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# filemode 'w' means to write to app.log. By default this is set to 'a' which appends to the contents of the file.
logging.warning('This will get logged to a file')

# Note: basicConfig can only be called once. We can not configure the root logger more than once.