import logging

from src.main import run
from src.utils import initialize_logger

import os
def print_env_variables():
    for key, value in os.environ.items():
        print(f"{key}: {value}")

# initialize_logger()

# logger = logging.getLogger()
# logger.info('Starting ohlc_to_feature_store service...')
# run()
