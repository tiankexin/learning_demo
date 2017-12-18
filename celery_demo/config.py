from kombu import Queue
from datetime import timedelta

BROKER_URL = 'amqp://tian:tian@localhost:5672/tian'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

CELERY_QUEUES = (
    Queue('default', routing_key='task.#'),
    Queue('web_tasks', routing_key='web.#')
)
CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'
CELERY_ROUTES = {
    'celery_demo.tasks.add': {
        'queue': 'web_tasks',
        'routing_key': 'web.add'
    },
    'celery_demo.tasks.div': {
        'queue': 'default',
        'routing_key': 'task.default'
    }
}
CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'celery_demo.tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    }
}
