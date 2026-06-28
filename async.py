import asyncio

async def greet():
    print("Greetings!")

# asyncio.run(greet())

async def download():
    print("Download inprogress...")
    await asyncio.sleep(3)
    print("Download completed!")
    
    
async def task():
    print("Start")
    print("Running...")
    await asyncio.sleep(5)
    print("End!")
    
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 done")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 done")
    
async def main():
    await asyncio.gather(
        task1(),
        task2()
    )
# asyncio.run(main())

async def work():
    await asyncio.sleep(2)
    print("This is work!")

async def main():
    print("Doing something...")
    await work()
    print("This is main")
    
# asyncio.run(main())

async def main_v2():
    task = asyncio.create_task(work())
    print("Doing something...")
    await task
    print("This is main_v2")
    
# asyncio.run(main_v2())

async def download():
    print("Downloading...")
    await asyncio.sleep(5)
    print("Downloaded!")
    
async def report():
    print("Writing a report...")
    await asyncio.sleep(3)
    print("Report finished!")
    
async def main():
    await asyncio.gather(
        download(),
        report()
    )
    
    
async def main_v2():
    download_task = asyncio.create_task(download())
    await report()
    await download_task    

async def main_v3():
    await download()
    await report()
    
async def main_v0():
    await asyncio.gather(
        main_v2(),
        main_v3()
    )
# asyncio.run(main_v0())


async def slow_api():
    await asyncio.sleep(5)
    return "Success"
async def init():
    try:
        task = await asyncio.wait_for(slow_api(), timeout=3)
        print(task)
    except asyncio.TimeoutError:
        print("Took too long!")
asyncio.run(init())