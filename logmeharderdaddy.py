# built-in features to add logging to our applications
import logging

# there are 5 different log levels we can log to
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# If we were to run these: only the last 3 will output to console
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# we can change basic settings of logging with basicConfig

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

# we can also create our own modules 
logger = logging.getLogger(__name__)
logger.propagate = False 
# now we can actually log something
logger.info('Hello, this is being logged')

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s  - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('this is an error')


