import logging;logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s \
%(levelname)s %(message)s', datefmt='%a %d %b %Y %H:%M:%S', filename='../../my.log', filemode="w")
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>wxbtest</h1>',content_type="text/html")

async def init(loop):
    app =  web.Application()
    app.router.add_route('get','/',index)
    apprunner = web.AppRunner(app)
    await apprunner.setup()
    srv = await loop.create_server(apprunner.server,'127.0.0.1',9001)
    logging.info('server started at http://127.0.0.1:9001...')
    return srv

class Model():
    def __init__(self, name):
        self.name = name
    def __getattr__(self, key):
        try:
            print("jinsasasasa")
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
