"""
@该demo需要运行在py3环境下
"""

import time
from concurrent import futures


def display(x):
    print("..............:{}".format(x))
    time.sleep(x)
    return x*10


def test1():

    pool = futures.ThreadPoolExecutor(max_workers=3)
    results = pool.map(display, range(4))
    print(type(results), results)      # 此处不会发生阻塞,返回的results结果是一个生成器
    for i in results:    # 此处会发生阻塞,__next__方法会等待当前结果处理完成,所以返回的结果的先后顺序一定是与map的顺序一致
        print("results:{}".format(i))


def test2():
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = list()
        for cc in sorted(range(5), reverse=True):
            future = executor.submit(display, cc)    # sumbit提交的同时线程就开始执行
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))
        results = []
        print("waiting for results")
        for future in futures.as_completed(to_do):     # 首先返还执行状态完成的future(期物), 可以避免第一个结果阻塞造成的等待时间
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
        print("finally results:{}".format(results))

if __name__ == '__main__':
    test1()
    print("================分割线===============")
    test2()
