# import logging
# from os import environ
# import sys


# from celery import Celery
# from celery.signals import after_setup_logger

# #from . import log_file, app_configs

# logger = logging.getLogger(__name__)

# app = Celery(
#     'model',
#     broker='redis://redis:6379/0',
#     backend='redis://redis:6379/0',
#     include=['risk_models_api.model.tasks.cns'],
#     broker_connection_retry_on_startup=True,
# )


# app.conf.update(
#     result_expires=3600,
#     task_routes = {  
#         'risk_models_api.model.tasks.cns.task_1': {
#             'queue': 'queue1',  
#         },
#         'risk_models_api.model.tasks.cns.task_2': { 
#             'queue': 'queue2'   
#         }
#     }
# )


# if __name__ == '__main__':
#     app.start()