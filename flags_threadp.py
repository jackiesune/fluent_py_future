import os
import time
import sys
import requests
from concurrent import futures

POP_CC=('CN IN US ID BR PK NG BD RU JP '
        'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL='http://flupy.org/data/flags'
DEST_DIR='downloads'


MAX_WORKERS=3

def save_flags(img,filename):
    path=os.path.join(BEST_DIR,filename)
    with open(path,'wb') as f :
        f.write(img)

def get_flag(cc):
    url='{}/{cc}/{cc}.gif'.format(BASE_URL,cc=cc.lower())
    print("request {}".format(cc))
    resp=requests.get(url)
    print("get {} state{}".format(cc,resp.status_codes))
    return resp.content

def down_one(cc):
    image=get_flag(cc)
    show(cc)
    save_flag(image,cc.lower()+'.gif')
    return cc

def show(text):
    print(text,end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    workers=min(MAX_WORKERS,len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res=executor.map(down_one,sorted(cc_list))

    return len(list(res))

def main(download_many):
    t0=time.time()
    count=download_many(POP_CC)
    ela=time.time()-t0
    msg='\n{} flags downloadedd in {:.2f}s'
    print(msg.format(count,ela))



if __name__=='__main__':
    main(download_many)

