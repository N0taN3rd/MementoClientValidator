import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado
import tornado.web
import tornado.log
from requestHandlers import P1d1Handler
import config


class MementoClientTestServer(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/1.1(.*)", P1d1Handler),
        ]
        settings = {
            "template_path": config.TEMPLATE_PATH,
            "static_path": config.STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

