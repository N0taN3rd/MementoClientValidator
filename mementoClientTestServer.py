import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado
import tornado.web
from tornado.options import define, options
from RequestHandlers import P1d1Handler
import config
import util

define("port", default=8000, help="run on the given port", type=int)


class MementoClientTestServer(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/1.1(.*)", P1d1Handler),
        ]
        settings = {
            "template_path": config.TEMPLATE_PATH,
            "static_path": config.STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    print("Hi")
    print(util.validate_req_datetime("20010320133610",False))
    tornado.options.parse_command_line()
    app = MementoClientTestServer()
    '''
     application.add_handlers(r"www\.myhost\.com", [
            (r"/article/([0-9]+)", ArticleHandler),
        ])
         http://a.example.org
    '''
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

