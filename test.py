import threading
import asyncio

@asyncio.coroutine
def hello(name):
    print(name)
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())
    print("end",name)

loop = asyncio.get_event_loop()
tasks = [hello("1"), hello("2")]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()