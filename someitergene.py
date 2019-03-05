class Am:
    def __init__(self,begin,step,end):
        self.begin=begin
        self.end=end
        self.step=step

    def __iter__(self):
        result=type(self.begin+self.step)(self.begin)
        index=0
        forever=self.end is None
        while forever or result<self.end:
            yield result
            index+=1
            result=result+self.step*index

import itertools
def gen_am(start,step,end=None):
    result=type(start+step)(start)
    ap_gen=itertools.count(result,step)
    if end is not None:
        ap_gen=itertools.takewhile(lambda n:n<end,ap_gen)
    return ap_gen
