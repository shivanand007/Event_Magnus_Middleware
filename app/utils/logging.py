import logging
import os
import datetime
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
import colorlog
import sys


def setup_logger(name):
    """Function to setup a logging configuration with a rotating file handler"""
    load_dotenv()
    # Get logging details from environment variables
    log_dir = os.environ.get('LOG_DIR')
    log_level = os.environ.get('LOG_LEVEL')
    log_max_size = int(os.environ.get('LOG_MAX_SIZE'))

    # create a formatter without log colors
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    # Create log file directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Use rotating file handler to create new log file every day and limit file size
    file_handler = logging.handlers.RotatingFileHandler(
        filename=os.path.join(log_dir, datetime.datetime.now().strftime('%Y-%m-%d') + '.log'),
        maxBytes=log_max_size,
        backupCount=10
    )
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger("Api-Logger")