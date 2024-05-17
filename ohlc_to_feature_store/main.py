import os
def print_env_variables():
    for key, value in os.environ.items():
        print(f"{key}: {value}")
        
# import logging

# from src.main import run
# from src.utils import initialize_logger

# initialize_logger()

# logger = logging.getLogger()
# logger.info('Starting ohlc_to_feature_store service...')
# run()
