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
