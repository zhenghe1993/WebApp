import logging
import asyncio, json, os, time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>awesome</h1>')


@asyncio.coroutine
def init(temp):
    app = web.Application(loop=temp)
    app.router.add_route('GET', '/', index)
    srv = yield from temp.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info("server start 127.0.0.1 9000")
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
