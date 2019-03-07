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
    path=os.path.join(BASE_URL,filename)
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
    save_flags(image,cc.lower()+'.gif')
    return cc

def show(text):
    print(text)
    sys.stdout.flush()

def download_many(cc_list):
#    workers=min(MAX_WORKERS,len(cc_list))
#    with futures.ThreadPoolExecutor(workers) as executor:
#        res=executor.map(down_one,sorted(cc_list))
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        lfutures=[]
        for cc in cc_list:
            future=executor.submit(down_one,cc)
            lfutures.append(future)
            msg='scheduled for {} :{}'
            print(msg.format(cc,future))

        results=[]
        for resfuture in futures.as_completed(lfutures):
            res=resfuture.result()
            results.append(res)
            msg='{} result :{!r}'
            print(msg.format(resfuture,res))


    return len(results)

def main(download_many):
    t0=time.time()
    count=download_many(POP_CC)
    ela=time.time()-t0
    msg='\n{} flags downloadedd in {:.2f}s'
    print(msg.format(count,ela))



if __name__=='__main__':
    main(download_many)

