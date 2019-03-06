def co_des(func):
    def prim(*args,**kwargs):
        gen=func()
        next(gen)
        return gen
    return prim

