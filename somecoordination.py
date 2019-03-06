from collections import namedtuple



from description import co_des


Result=namedtuple('Result','count average')

def co_average():
    total=0
    count=0
    term=0
    average=None
    while True:
        term=yield average
        if term is None:
            break
        total+=term
        count+=1
        average=total/count
    return Result(count,average)


#让协程抛出指定异常，并处理。
class DemoException(Exception):
    '''自定义异常'''

def demo_finally():
    try:
        while True:
            try:
                x=yield
            except DemoException:
                print("**DemoException has been handled**")
            else:
                print("coroutine receiverd x:",x)
    finally:
        print("coroutine end")


#调用co_average的委派函数
def grouper(results,key):
    while True:
        results[key]=yield from co_average()


#输出报告result
def report(results):
    for key,result in sorted(results.items()):
        group,unit=key.split(';')
        print('{:2} {:5} average {:.2f}{}'.format(result.count,group,result.average,unit))




