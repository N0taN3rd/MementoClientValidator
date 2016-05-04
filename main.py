import tornado.web
from tornado.options import define, options

import util
from generate import generate_configured_timemaps

define("port", default=8000, help="run on the given port", type=int)

if __name__ == '__main__':
    options.parse_config_file("server.conf")
    print("Hi")
    print(util.validate_req_datetime("20010320133610", False))
    generate_configured_timemaps()
    from mementoClientTestServer import MementoClientTestServer

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

