import tornado.web
from tornado.web import RequestHandler


from Patterns import P1D1,P1D2,P1D3


class P1d1Handler(RequestHandler, P1D1):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    def head(self, path):
        v = self.get_argument("version", None)
        self.head_headers(self)
        if path == '/' or path == '':
            self.render("default.html", title="Default Head Pattern 4.1.1",
                        items=['You Asked For Head'])
        else:
            if v is not None and self.is_get_required_uri(v):
                self.render("pattern4-1.html", title="Pattern 4.1.1")
            else:
                self.render("bad.html", title="Bad URI-R",
                            items=['required URI-R %s' % '1.1/?version=20010320133610',
                                   'received URI-R %s %s' % (path, v if v is not None else "Nothing")])

    @tornado.web.asynchronous
    def get(self, path):
        v = self.get_argument("version", None)
        t = self.get_argument("style", "not")
        vv = v if v is not None else "Nothing"
        if v is not None:
            if self.is_get_required_uri(v):
                self.get_headers(self)
                self.render("pattern4-1.html", title="Pattern 4.1.1")
            else:
                if v == 'all' and t == 'timemap':
                    with open('timemaps/1.1.timemap', 'r') as content_file:
                        content = "".join(line for line in content_file)
                    print(content)
                    self.write(content)
                    self.finish()
                else:
                    self.render("bad.html", title="Bad URI-R",
                                items=['required URI-R %s' % '1.1/?version=20010320133610',
                                       'received URI-R %s %s' % (path, vv)])
        else:
            self.render("default.html", title="Default Get Pattern 4.1.1",
                        items=['You Asked For Get'])


class P1d2Handler(RequestHandler, P1D2):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    def head(self, path):
        v = self.get_argument("version", None)
        self.head_headers(self)
        if path == '/' or path == '':
            self.render("default.html", title="Default Head Pattern 4.1.2",
                        items=['You Asked For Head'])
        else:
            if v is not None and self.is_get_required_uri(v):
                self.render("pattern4-2.html", title="Pattern 4.1.2")
            else:
                self.render("bad.html", title="Bad URI-R",
                            items=['required URI-R %s' % '1.2/?version=20010320133610',
                                   'received URI-R %s %s' % (path, v if v is not None else "Nothing")])

    @tornado.web.asynchronous
    def get(self, path):
        v = self.get_argument("version", None)
        vv = v if v is not None else "Nothing"
        if v is not None:
            if self.is_get_required_uri(v):
                self.get_headers(self)
                self.render("pattern4-1.html", title="Pattern 4.1.1")
            else:
                self.render("bad.html", title="Bad URI-R",
                            items=['required URI-R %s' % '1.1/?version=20010320133610',
                                   'received URI-R %s %s' % (path, vv)])
        else:
            self.render("default.html", title="Default Get Pattern 4.1.1",
                        items=['You Asked For Get'])


class P1d3Handler(RequestHandler, P1D3):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    def head(self):
        self.head_headers(self)
        self.finish()

    @tornado.web.asynchronous
    def get(self):
        self.get_headers(self)
        self.finish()
