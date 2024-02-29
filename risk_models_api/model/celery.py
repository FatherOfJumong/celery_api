import logging
from os import environ
import sys


from celery import Celery
from celery.signals import after_setup_logger

#from . import log_file, app_configs

logger = logging.getLogger(__name__)

app = Celery(
    'model',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
    include=['risk_models_api.model.tasks.cns'],
    broker_connection_retry_on_startup=True,
)

app.conf.update(
    result_expires=3600,
)

# @after_setup_logger.connect
# def setup_loggers(logger, *args, **kwargs):
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#     # FileHandler
#     fh = logging.FileHandler(log_file)
#     fh.setFormatter(formatter)
#     logger.addHandler(fh)
#

if __name__ == '__main__':
    app.start()