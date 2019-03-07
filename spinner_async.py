import asyncio
import sys
#import tqdm
import itertools


@asyncio.coroutine
def spinner(msg):
    writer=sys.stdout.write
    flush=sys.stdout.flush
    for char in itertools.cycle('-\\|/'):
        status=char + ' ' + msg
        writer(status)
        flush()
        writer('\x08'*len(status))
        try:
            yield from asyncio.sleep(.2)
        except asyncio.CancelledError:
            break
    writer(' ' * len(status) + '\x08'*len(status))

@asyncio.coroutine
def sleept():
    '''运行时间控制'''
    yield from asyncio.sleep(4)
    return "4秒"

@asyncio.coroutine
def supervisor():
    spinnert=asyncio.async(spinner('Thinking'))
    print('spinner object',spinnert)
    result=yield from sleept()
    spinnert.cancel()
    return result

def main():
    loop=asyncio.get_event_loop()
    result=loop.run_until_complete(supervisor())
    loop.close()
    print('Asnwer:',result)


if __name__ == "__main__":
    main()
