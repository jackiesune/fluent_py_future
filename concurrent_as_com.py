from concurrent import futures
import time
import tqdm
import random

l1=list('abcdefghjklmn')



def change(strs):
    
    time.sleep(random.choice(range(1,10,2)))
    print(time.strftime('[%H:%M:%S]'),"+",'char is ','strs')
    return strs.upper()

def main():
    print("start:",time.strftime('[%H:%M:%S]'))
    futurel=[]
    executor=futures.ThreadPoolExecutor(max_workers=3)
    for i in l1:
        future=executor.submit(change,i)
        futurel.append(future)
    tqdmiter=tqdm.tqdm(futures.as_completed(futurel),total=13)
    for fu in tqdmiter:
        print("start completed")
        print('fu:',fu,'result:',fu.result())

if __name__=='__main__':
    main()
