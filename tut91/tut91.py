'''
    TODO: AsyncIO in Python | Python Tutorial - Day #96 
    ? async - sync wait
    ! it is not multithreading & not multiprocessing
    ! async executing more than one program at same time
'''

import asyncio


async def fun1():
    await asyncio.sleep(2)
    print("fun1")
    
    return "--fun1--"


async def fun2():
    await asyncio.sleep(2)
    print("fun2")

    return "--fun2--"

async def fun3():
    await asyncio.sleep(2)
    print("fun3")

    return "--fun3--"

async def main():
    res = await asyncio.gather(
        fun1(),
        fun2(),
        fun3(),
    )
    print(res)

asyncio.run(main())