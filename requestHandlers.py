import tornado.web
from tornado.web import RequestHandler



from patterns import P1D1, P1D2, P1D3


class P1d1Handler(RequestHandler, P1D1):
    """
    RequestHandler for pattern 4.1.1

    Subclass P1D1 as well as tornado.web.RequestHandlers
    are spawned per request and do not persist state
    so by making the actions surrounding the headers
    tied to classmethods and class variables.
    The logic in the patterns and how the request is served
    can be separate
    """
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    def head(self, path):
        v = self.get_argument("version", None)
        t = self.get_argument("style", None)
        if v == 'all' and t == 'timemap':
            self.set_header("Content-Type", "text/plain; charset=UTF-8")
            self.write(self.timemap)
            self.finish()
        else:
            self.head_headers(self.set_header, self.set_status)
            if path == '/' or path == '':
                self.render("default.html", title="Default Head Pattern 4.1.1",
                            items=['You Asked For Head'])

            else:
                if v is not None and self.is_memento_uri(v):
                    self.render("pattern4-1.html", title="Pattern 4.1.1")
                else:
                    self.render("bad.html", title="Bad URI-R",
                                items=['required URI-R %s' % '1.1/?version=20010320133610',
                                       'received URI-R %s %s' % (path, v if v is not None else "Nothing")])

    @tornado.web.asynchronous
    def get(self,path):
        print(path)
        v = self.get_argument("version", None)
        t = self.get_argument("style", None)
        print(self.request.full_url())
        vv = v if v is not None else "Nothing"
        if v is not None:
            if self.is_memento_uri(v):
                self.get_headers(self.set_header, self.set_status)
                self.render("pattern4-1.html", title="Pattern 4.1.1")
            else:
                if v == 'all' and t == 'timemap':
                    self.write(self.timemap)
                    self.set_header("Content-Type", "text/plain; charset=UTF-8")
                    self.finish()
                else:
                    self.default(self.set_header, self.set_status)
                    self.render("bad.html", title="Bad URI-R",
                                items=['required URI-R %s' % '1.1/?version=20010320133610',
                                       'received URI-R %s %s' % (" ", vv)])
        else:
            self.default(self.set_header, self.set_status)
            self.render("default.html", title="Default Get Pattern 4.1.1",
                        items=['You Asked For Get'])


class P1d2Handler(RequestHandler, P1D2):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    def head(self, path):
        v = self.get_argument("version", None)
        self.head_headers(self.set_header, self.set_status)
        if path == '/' or path == '':
            self.render("default.html", title="Default Head Pattern 4.1.2",
                        items=['You Asked For Head'])
        else:
            if v is not None and self.is_memento_uri(v):
                self.render("pattern4-2.html", title="Pattern 4.1.2")
            else:
                self.render("bad.html", title="Bad URI-R",
                            items=['required URI-R %s' % '1.2/?version=20010320133610',
                                   'received URI-R %s %s' % (path, v if v is not None else "Nothing")])

    @tornado.web.asynchronous
    def get(self, path):
        v = self.get_argument("version", None)
        t = self.get_argument("style", "not")
        vv = v if v is not None else "Nothing"
        if v == 'all' and t == 'timemap':
            self.write(self.timemap)
            self.set_header("Content-Type", "text/plain; charset=UTF-8")
            self.finish()
        else:
            self.get_headers(self.set_header, self.set_status)
            self.render("pattern4-2.html", title="Pattern 4.1.2")


class P1d3Handler(RequestHandler, P1D3):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    def head(self,path):
        v = self.get_argument("version", None)
        t = self.get_argument("style", "not")
        if v == 'all' and t == 'timemap':
            self.write(self.timemap)
            self.set_header("Content-Type", "text/plain; charset=UTF-8")
            self.finish()
        else:
            self.head_headers(self.set_header, self.set_status)
            self.render("pattern4-3.html", title="Pattern 4.1.3")

    @tornado.web.asynchronous
    def get(self,path):
        v = self.get_argument("version", )
        t = self.get_argument("style", "not")
        if v == 'all' and t == 'timemap':
            self.write(self.timemap)
            self.set_header("Content-Type", "text/plain; charset=UTF-8")
            self.finish()
        else:
            self.get_headers(self.set_header, self.set_status)
            self.render("pattern4-3.html", title="Pattern 4.1.3")