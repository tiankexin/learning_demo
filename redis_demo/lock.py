# -*- coding: utf-8 -*-
"""
redis 锁
"""
import uuid
import redis
import time
import math
from redis import Redis

cnn = Redis()


def acquire_lock(cnn, lock_name, acquire_timeout=10, lock_timeout=10):
    """
    identifier用于防止该线程释放其他人的锁
    lock_timeout解决上锁的进程已经崩溃,而其他需要锁的方一直等待获取锁
    检查ttl可以防止程序在setnx和expire直接奔溃了,导致锁没有上锁时间
    """

    identifier = uuid.uuid4().get_hex()
    lock_timeout = math.ceil(lock_timeout)
    end_time = time.time() + acquire_timeout
    while time.time() < end_time:
        if cnn.setnx(lock_name, identifier):
            cnn.expire(lock_name, lock_timeout)
            return True
        elif not cnn.ttl(lock_name):
            cnn.expire(lock_name, lock_timeout)
        time.sleep(.001)
    return False


def release_lock(cnn, lock_name, identifier):
    pipe = cnn.pipeline(True)
    while True:
        try:
            pipe.watch(lock_name)
            if pipe.get(lock_name) == identifier:
                pipe.multi()
                pipe.delete(lock_name)
                pipe.execute()
                return True
            pipe.unwatch()
            break
        except redis.exceptions.WatchError:
            pass
    return False


