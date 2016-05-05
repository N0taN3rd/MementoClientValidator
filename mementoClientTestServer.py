import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado
import tornado.web
from tornado.web import  url
import tornado.log
from requestHandlers import P1d1Handler,P1d2Handler,P1d3Handler
import config


class MementoClientTestServer(tornado.web.Application):
    def __init__(self):
        handlers = [url(r"/1.1(.*)", P1d1Handler),
                    url(r"/1.2(.*)", P1d2Handler),
                    url(r"/1.3(.*)", P1d3Handler),
        ]
        settings = {
            "template_path": config.TEMPLATE_PATH,
            "static_path": config.STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

