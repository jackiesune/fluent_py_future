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

if __name__=='__main__':
    main1(*sys.argv[1:])



