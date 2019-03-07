import asyncio
import sys

from charfinder import UnicodeNameIndex

CONT=b'\r\n'
PR=b'???>'

index=UnicodeNameIndex()

@asyncio.cooroutine
def handle_query(reader,writer):
    while True:
        yield from writer.write(PR)
        
        yield from writer.drain()
        data=yield from reader.readline()
        try:
            query=data.decode().strip()
        except UnicodeDecodeError:
            query='\x00'
        client=writer.get_extra_info('peername')
        print('Received data from {} : {!r}'.format(client,query))
        if query:
            if ord(query[:1])<32:
                break
            lines=list(index.find_descriprtion_strs(query))
        if lines:
            writer.write(index.status(query,len(lines).encode()+CONT))

        yield from write.drain()
        print('Sented to client  {} results'.format(len(lines)))

    print('Close this client{} socket'.format(client))
    writer.close()


def main1(address='127.0.0.1',port=12345):
    port=int(port)
    loop=asyncio.get_event_loop()
    service_co=asyncio.start_server(handle_query,address,port,loop=loop)
    servic=loop.run_until_complete(service_co)
    host=service.socket[0].getsockname()
    print("Service at address {}.Press CTRL-C to stop".format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    print("Server shutting down.")
    loop.run_until_complete(server.wait_closed())
    loop.close()

#if __name__=='__main__':
#    main1(*sys.argv[1:])



#下面是使用aiohttp 实现的web服务器
import aiohttp
from aiohttp import web
import sys



CONTENT_TYPE = 'text/html; charset=UTF-8'
ROW_TPL = '<tr><td>{code_str}</td><th>{char}</th><td>{name}</td></tr>'


def home(request):
    query=rquest.GET.get('query',' ').strip()
    print("Query :{!r} from client".format(query))
    if query:
        descriptions=list(index.find_descriptions(query))
        res='\n'.join(ROW_TPL.format(**vars(desc)) for desc in descriptions)
        msg = index.status(query,len(description))
    else:
        res = ''
        descriptions=[]
        msg='Enter words to  descrip the characters'
    html=template.format(query=query,result=res,message=msg)

    print("send {} results.".format(len(descriptions)))
    return web.Response(content_type=CONTENT_TYPE,text=html)


@asyncio.coroutine
def init(loop,address,port):
    app=web.Aplication(loop=loop)
    app.router.add_route('GET','/',home)
    handler=app.make_handler()
    #以handler为处理程序 创建服务器
    server=yield from loop.start_server(handler,address,port)
    
    return server.sockets[].getsockname()

def main(address='127.0.0.1',port=12345):
    loop=asyncio.get_event_loop()
    port=int(port)
    host=loop.run_until_complete(init(loop,address,port))
    print("service at address:{},Press CTRL-C to quit".format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    print("Service Stopped")
    loop.close()


#if __name__=='__main__':
#    main(*sys.argv[1:])

