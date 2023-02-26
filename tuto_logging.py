import logging

"""
logging levels in order of increasing severity 
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL

by default, the logging level is set to WARNING
it means that only messages with a level of WARNING or higher will be displayed
"""

# CREATE BASIC LOGGER
logging.basicConfig(filename="log.log",
                    level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")
                    
# write log to file
logging.info("logging info")

"""
# if you want to overwrite the log file, use the "w" filemode
logging.basicConfig(filename="log.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s"

# if you want to log the stack trace, use the exc_info parameter
try:
    raise Exception("error")
except:
    logging.error("error", exc_info=True)
"""

# CREATE CUSTOM LOGGER
logger = logging.getLogger("logger_name")
handler = logging.FileHandler("custom_log.log")
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# write log to file
logger.info("logging info")

