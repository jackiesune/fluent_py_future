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


class LookingGlass:

    def __enter__(self):
        import sys
        self.origin_write=sys.stdout.write
        sys.stdout.write=self.reverse_write
        return "ABCDEFG"

    def reverse_write(self,text):
        return self.origin_write(text[::-1])

    def __exit__(self,exc_type,exc_value,traceback):
        import sys
        sys.stdout.write=self.origin_write
        if exc_type is ZeroDivisionError:
            print("cannot divide zero")
            return True
    

