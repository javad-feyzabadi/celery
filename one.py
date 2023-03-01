from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('first',brocker = 'amqp://guest:guest@localhost:5672')
logger = get_task_logger(__name__)

@app.task(name = 'one.disuing',bind = True,default_retry_delay = 600)
def disu(self,a,b):
    try:
        return a /b
    except ZeroDivisionError:
        logger.info('sorry')
        self.retry(countdown = 5)

