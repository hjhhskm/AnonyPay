import asyncio
import time

async def do_some_things(x):
    time.sleep(x)
    print("hello world")
    return 1

async def input_some_things():
    data = input("please input your name")
    print(data," love PJ")
async def printSecond(x):
    for i in range(0,x):
        print(i)
        time.sleep(1)

def callbackF(future):
    print("Callback",future.result())

coroutine1 = do_some_things(2)
coroutine3 = printSecond(15)
coroutine2 = input_some_things()

loop = asyncio.get_event_loop()
pool = asyncio.get_event_loop()
task = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2)
]
task.append(asyncio.ensure_future(coroutine3))

print(task)
print(asyncio.isfuture(task))

loop.run_until_complete(asyncio.wait(task))

# cor = do_some_things()
# loop = asyncio.get_event_loop()
# task = loop.create_future(cor)
# print(isinstance(task,asyncio.Future))
# loop.run_until_complete(task)