import re
import reprlib

REWORD=re.compile('\w+')
class Sentence:
    def __init__(self,text):
        self.text=text
        self.word=REWORD.findall(text)

    def __len__(self):
        return len(self.word)

    def __getitem__(self,index):
        return self.word[index]

    def __repr__(self):
        return "Sentence :{}".format(reprlib.repr(self.text))
    
    def __iter__(self):
        '''or 
        for match in REWORD.finditer(self.text):
            yield match.group()减少了一个列表
            
            or
        return (match.group() for match in REWORD.findall(self.text0)) 直接返回生成器'''
        for i in self.word:
            yield i

