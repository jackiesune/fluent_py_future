import os
import time
import sys
import asyncio
import aiohttp


POP_CC=('CN IN US ID BR PK NG BD RU JP '
        'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL='http://flupy.org/data/flags'
DEST_DIR='downloads'


MAX_WORKERS=3

def save_flags(img,filename):
    path=os.path.join(BASE_URL,filename)
    with open(path,'wb') as f :
        f.write(img)
@asyncio.coroutine
def get_flag(cc):
    url='{}/{cc}/{cc}.gif'.format(BASE_URL,cc=cc.lower())
    print("request {}".format(cc))
    resp=yield from aiohttp.request('GET',url)
    image=yield from resp.read()
    print("get {} state{}".format(cc,resp.status_codes))
    return image

@asyncio.coroutine
def down_one(cc):
    image=yield from image=get_flag(cc)
    show(cc)
    save_flags(image,cc.lower()+'.gif')
 #   if verbose:
 #       print(cc,msg)
    return cc

def show(text):
    print(text)
    sys.stdout.flush()

def download_many(cc_list):
    loop=asyncio.get_event_loop()
    co_list=[down_one(cc) for cc in cc_list]
    wait=async.wait(co_list)
    results,_ in loop.run_until_completed(wait)
    loop.close()

    return len(results)

def main(download_many):
    t0=time.time()
    count=download_many(POP_CC)
    ela=time.time()-t0
    msg='\n{} flags downloadedd in {:.2f}s'
    print(msg.format(count,ela))

