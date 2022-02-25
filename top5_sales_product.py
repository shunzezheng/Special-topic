from __init__ import *


class NewAsyncHTMLSession(AsyncHTMLSession):
    def run(self, *coros, urls=None):
        """ Pass in all the coroutines you want to run, it will wrap each one
            in a task, run it and wait for the result. Return a list with all
            results, this is returned in the same order coros are passed in. """
        if urls:
            if isinstance(urls, list):
                tasks = [
                    asyncio.ensure_future(coro(url)) for coro in coros for url in urls
                ]
                done, _ = self.loop.run_until_complete(asyncio.wait(tasks))
                return [t.result() for t in done]
            else:
                tasks = [
                    asyncio.ensure_future(coro(urls)) for coro in coros
                ]
                done, _ = self.loop.run_until_complete(asyncio.wait(tasks))
                return [t.result() for t in done]
        else:
            tasks = [
                asyncio.ensure_future(coro()) for coro in coros
            ]
            done, _ = self.loop.run_until_complete(asyncio.wait(tasks))
            return [t.result() for t in done]


asession = NewAsyncHTMLSession()


async def pop_goods(url):
    r = await asession.get(url)
    try:
        await r.html.arender()
    except:
        await r.html.arender(timeout=20)
    e3 = r.html.find("#cq_recomm_slot-89984c043f9f6c5dfe5899d4eb > div > div > div > div:nth-child(9) > div.photo > a")
    e2 = r.html.find("#cq_recomm_slot-89984c043f9f6c5dfe5899d4eb > div > div > div > div:nth-child(6) > div.photo > a")
    e1 = r.html.find("#cq_recomm_slot-89984c043f9f6c5dfe5899d4eb > div > div > div > div:nth-child(3) > div.photo > a")
    for r1, r2, r3 in zip(e1, e2, e3):
        i = '第 ' + r1.attrs['data-position'] + ' 名 ' + r1.attrs['data-name'] + ' ' + r1.attrs['data-price'] + ' 元 '
        await asyncio.sleep(1)
        j = '第 ' + r2.attrs['data-position'] + ' 名 ' + r2.attrs['data-name'] + ' ' + r2.attrs['data-price'] + ' 元 '
        await asyncio.sleep(1)
        k = '第 ' + r3.attrs['data-position'] + ' 名 ' + r3.attrs['data-name'] + ' ' + r3.attrs['data-price'] + ' 元 '
    return i, j, k


if __name__=="__main__":
    url = input('')
    pop_result = asession.run(pop_goods, urls=url)
    print(pop_result)
