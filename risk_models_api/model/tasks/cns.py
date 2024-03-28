# from ..celery import app, logger
# import time
# import pandas as pd


# @app.task
# def task_1(text):

#     data = {
#         'name': ['Tom', 'Nick', 'John', 'Tom', 'Nick', 'John'],
#         'age': [20, 21, 19, 20, 21, 19]
#     }
#     df = pd.DataFrame(data)
#     logger.info("Task completed successfully")
#     return df.to_dict()




# @app.task
# def task_2(text):
#     data = {
#         'name': ['Tom', 'Nick', 'John', 'Tom', 'Nick', 'John'],
#         'age': [20, 21, 19, 20, 21, 19]
#     }
#     df = pd.DataFrame(data)
    
#     return df.to_dict()
