# from celery.schedules import crontab


# beat_schedule = {
#     'task_every_minutes':{
#     'task':'one.show',
#     'schedule':crontab(minute='*/1'),
#     'args':('mahsa',)
#     }
# }


from kombu import Exchange,Queue


default_exchange = Exchange('default',type='direct')
media_exchange = Exchange('media',type='direct')


task_queues = (
    Queue('default',default_exchange,routing_key='default'),
    Queue('video',media_exchange,routing_key='video'),
    Queue('image',media_exchange,routing_key='image'),
)


task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'


# task_routes = {
#     'one.add':{'queue':'video'},
#     'one.sub':{'queue':'image'},
# }