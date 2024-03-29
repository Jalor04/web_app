import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
routes = web.RouteTableDef()


async def index(request):
    return web.Response(body='<h1>Hello world.</h1>',content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.add_routes([web.get('/', index)])
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
