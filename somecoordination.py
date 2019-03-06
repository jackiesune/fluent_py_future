from description import co_des

@co_des
def co_average():
    total=0
    count=0
    term=0
    average=None
    while True:
        term=yield average
        total+=term
        count+=1
        average=total/count



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
