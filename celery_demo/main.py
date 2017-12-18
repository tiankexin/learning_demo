# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import Celery

app = Celery("celery_demo", include=['celery_demo.tasks'])
app.config_from_object('celery_demo.config')

if __name__ == '__main__':
    app.start()
