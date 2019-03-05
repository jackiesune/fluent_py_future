class Am:
    def __init__(self,begin,step,end):
        self.begin=begin
        self.end=end
        self.step=step

    def __iter__():
        result=type(self.begin+self.end)(self.begin)
        index=0
        forever=self.end is None
        while forever or result<self.end:
            yield result
            index+=1
            result=result+self.step*index

