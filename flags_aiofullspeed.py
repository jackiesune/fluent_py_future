import os
import time
import sys
import asyncio
import aiohttp
from aiohttp import web
import collections

from flags_common import HTTPStatus,Result
POP_CC=('CN IN US ID BR PK NG BD RU JP '
        'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL='http://flupy.org/data/flags'
DEST_DIR='downloads'
DEFAULT_CONCUR_REQ = 5



def save_flags(img,filename):
    path=os.path.join(BASE_URL,filename)
    with open(path,'wb') as f :
        f.write(img)

@asyncio.coroutine
def get_flag(cc):
    url='{}/{cc}/{cc}.gif'.format(BASE_URL,cc=cc.lower())
    print("request {}".format(cc))
    resp=yield from aiohttp.request('GET',url)
    if resp.status == 200:
        image=yield from resp.read()
        return image
    elif resp.status == 404:
        raise
    else:
        raise aiohttp.HttpProcessingError(code=resp.status,message=resp.reason,
                                          headers=resp.headers)


@asyncio.coroutine
def down_one(cc,semaphore,base_url,verbose=None):
    try:
        with (yield from semaphore):
            image=yield from image=get_flag(cc)
    except web.HTTPNotFound:
        status=HTTPStatus.not_found
        msg='not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        loop=async.get_event_loop()
        loop.run_in_executor(None,save_flags,cc.lower() + '.gif')
        status=HTTPStatus.ok
        msg='ok'
 #   if verbose:
 #       print(cc,msg)
    return Result(status,cc)

#def show(text):
#    print(text)
#    sys.stdout.flush()
class FetchError(Exception):
    def __init__(self,country_code):
        self.country_code=country_code

@asyncio.coroutine
def download_co(cc_list,base_url,concur_req,verbose=None):
    counter=collections.Counter()
    semaphore=asyncio.Semaphore(concur_req)
    to_do = [down_one(cc,semaphore,base_url,verbose) for cc in cc_list]
    iterfortqdm=asyncio.as_completed(to_do)
#    if not verbose:
#        iterfortqdm=tqdm.tqdm(iterfortqdm,total=len(cc_list))
    for future in iterfortqdm:
        try:
            res=yield from future
        except FetchError as exc:
            country_code=exc.country_code
            try:
                error_msg=exc.__cause__.args[0]
            except IndexError:
                error_msg=exc.__cause__.__classs__.__name__
            if verbose and error_msg:
                msg='detail:Error for {} :{}'
                print(msg.format(country_code,error_msg))
                status=HTTPStatus.error
        else:
            status=res.status
        counter[status] += 1
    return counter

def download_many(cc_list,base_url,concur_req,verbose=None):
    loop=asyncio.get_event_loop()
    co=download_co(cc_list,base_url,concur_req)
    countss=loop.run_until_completed(co)
    loop.close()
    return countss

def main(download_many, concur_req):
    concur_req=min(cc_list,concur_req)
    base_url =BASE_URL
    t0 = time.time()
    counter = download_many(cc_list, base_url,concur_req)
    print(counter)


if __name__ = "__main__":
    main(download_many, DEFAULT_CONCUR_REQ)


