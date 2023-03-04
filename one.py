from celery import Celery,group,signals,schedules
import time
# from celery.utils.log import get_task_logger

app = Celery('one',brocker = 'amqp://guest:guest@localhost:5672',backend='rpc://')
app.config_from_object('celery_conf')

# app.conf.update(
#     tasK_time_limit = 60 ,
#     task_soft_time_limit = 50 ,
#     worker_concurrency = 70 ,
#     worker_prefetch_multiplier=0 ,
#     task_ignore_result = True,
#     task_acks_late = False,
# )


# logger = get_task_logger(__name__)

@app.task
def add(a,b):
    time.sleep(2)
    return a + b

@app.task
def sub(a,b):
    return a-b


# @app.task
# def show(name):
#     print(f'this is signal schedule {name}')

