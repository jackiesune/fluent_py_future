import queue
from collections import namedtuple
import random
import time



Event=namedtuple("Event","time num action")

SEARCHTIME=5
TRIPTIME=20
ENDTIME=180
DEFAULTTAXI=3
STARTINTERVAL=5



def taxi_process(num,trips,start_time=0):
    time=yield Event(start_time,num,"leave home")
    for i in range(trips):
        time=yield Event(time,num,"get passenger")
        time=yield Event(time,num,"put down passenger")
    yield Event(time,num,"go home")


class  simu:

    def __init__(self,process):
        self.events=queue.PriorityQueue()
        self.processes=dict(process)

    def run(self,end_time):
        '''循环主程序'''
        #预激协程
        for _,process in sorted(self.processes.items()):
            tevent=next(process)
            self.events.put(tevent)

        now_time=0
        #开始活动
        while now_time<end_time:
            if self.events.empty():
                print('has no taxi')
                break
            
            revent=self.events.get()
            now_time,num,action=revent
            print("at {} the num taxi:{}\'s action is {}".format(now_time,num,action))
            active_taxi=self.processes[num]
            next_time=now_time + time_spending(action)
            try:
                next_event=active_taxi.send(next_time)
            except StopIteration:
                del self.processes[num]
            else:
                self.events.put(next_event)
        else:
            msg='##end of simulation time:{} events pending##'
            print(msg.format(self.events.qsize))


def time_spending(pre_action):
    if pre_action in ["leave home","put down passenger"]:
        interval=SEARCHTIME
    elif pre_action == "get passenger":
        interval=TRIPTIME
    elif pre_action == "go home":
        interval=1
    else:
        raise ValueError("Unknow action{} not in actions".format(pre_action))
    return int(random.expovariate(1/interval)) + 1


         



def main(end_time=ENDTIME,num_taxi=DEFAULTTAXI,seed=None):
    taxis={i:taxi_process(i,(i+1)*2,STARTINTERVAL*i) for i in range(num_taxi)
         }
    sim=simu(taxis)
    sim.run(end_time)

if __name__=="__main__":
    main()
