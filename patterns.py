from tornado.options import options

with open('timemaps/1.1.timemap', 'r') as content_file:
    tm1d1 = "".join(line for line in content_file)

with open('timemaps/1.2.timemap', 'r') as content_file:
    tm1d2 = "".join(line for line in content_file)

with open('timemaps/1.3.timemap', 'r') as content_file:
    tm1d3 = "".join(line for line in content_file)

where = "localhost:%d" % options.port
'''
HEAD / HTTP/1.1
   Host: a.example.org
   Accept-Datetime: Tue, 20 Mar 2001 20:35:00 GMT
   Connection: close
'''

get_link_1d1 = "<%s/1.1/>; rel=\"original timegate\",<%s/1.1/?version=all&style=timemap>; rel=\"timemap\"; " \
               "type=\"application/link-format\"; from=\"Tue, 15 Sep 2000 11:28:26 GMT\"; until=\"Tue, 20 Mar 2001 13:36:10 GMT" \
               "09:34:33 GMT\"" % (
                   where, where)

link_1d2 = "<%s/1.2/>; rel=\"original timegate\", <%s/1.2/?version=20010320133610>; rel=\"memento last first\"; " \
           "datetime=\"Tue, 20 Mar 2001 13:36:10 GMT\", <%s/1.2/?version=all&style=timemap>; rel=\"timemap\"; " \
           "type=\"application/link-format\"" % (
               where, where, where)

link_1d3 = "<%s/1.3/>; rel=\"original timegate\", <%s/1.3/?version=all&style=timemap>; rel=\"timemap\"; " \
           "type=\"application/link-format\"" % (
               where, where)

head_link_2d1 = "<%s/2.1-archive/timegate/%s/2.1/>; rel=\"timegate\"" % (where, where)

head_link_2d1_timegate = "<%s/2.1/>; rel=\"original\", <%s/2.1-archive/timemap/2.1/>; rel=\"timemap\"; " \
                         "type=\"application/link-format\"; from=\"Tue, 15 Sep 2000 11:28:26 GMT\"; until=\"Wed, " \
                         "20 Jan 2010 09:34:33 GMT\"" % (
                             where, where)

link_2d1m = "<%s/2.1/>; rel=\"original\",<%s/2.1-archive/timemap/%s/2.1/>; rel=\"timemap\"; " \
            "type=\"application/link-format\", <%s/2.1-archive/timegate/%s/2.1/>; rel=\"timegate\"" % (
                where, where, where, where, where)

link_2d2_timegate = "<%s/2.2/>; rel=\"original\", <%s/2.2-archive/timemap/%s/2.2/>; rel=\"timemap\"; " \
                    "type=\"application/link-format\", <%s/2.2-archive/timegate/%s/2.2/>; rel=\"timegate\"" % (
                        where, where, where, where, where)

link_2d2 = "<%s/2.2-archive/timegate/%s/2.2/>; rel=\"timegate\"" % (where, where)

link_2d3 = "<%s/2.3-archive/timegate/%s/2.3/>; rel=\"timegate\"" % (where, where)

link_2d3_timegate = "<%s/2.3/>; rel=\"original\", <%s/2.3/timemap/%s/2.3/>; rel=\"timemap\"; " \
                    "type=\"application/link-format\", <%s/2.3-archive/timegate/%s/2.3/>; rel=\"timegate\"" % (
                        where, where, where, where, where)

link_3 = "<%s/3/>; rel=\"original\"" % where

link_4 = "<%s/4/>; rel=\"original\", <%s/4-archive/20010321203610/%s/4/>; rel=\"first last memento\"; datetime=\"Wed, " \
         "" \
         "21 Mar 2001 20:36:10 GMT\""

link_5d2 = "<%s/5.2-archive/timegate/%s/5.2/>; rel=\"timegate\""

link_5d4b = "<%s/5.4/>; rel=\"original\", <%s/5.4/timemap/%s/5.4>; rel=\"timemap\"; type=\"application/link-format\", " \
            "" \
            "<%s/5.4/timegate/%s/5.4>; rel=\"timegate\"" % (
                where, where, where, where, where)

head_link_5d5 = "<%s/5.5>; rel=\"original\", <%s/5.5/timemap/%s/5.5>; rel=\"timemap\"; " \
                "type=\"application/link-format\", <%s/5.5/timegate/%s/5.5>; rel=\"timegate\"" % (
                    where, where, where, where, where)

ph = {
    "1.1": {
        "HEAD": {
            "response_code": 302,
            "response": "FOUND",
            "headers": [
                ("Vary", "accept-datetime"),
                ("Link", "<%s/1.1/>; rel=\"original timegate\"" % where),
                ("Location", "%s/1.1/?version=20010320133610" % where),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ]
        },
        "GET": {
            "response_code": 200,
            "response": "OK",
            "uri-r_required": "20010320133610",
            "headers": [
                ("Memento-Datetime", "Tue, 20 Mar 2001 13:36:10 GMT"),
                ("Link", get_link_1d1),
                ("Content-Type","text/html;charset=utf-8"),
                ("Connection", "close")
            ]

        },
        "default": {
            "response_code": 200,
            "response": "OK",
            "headers": [
                ("Link", get_link_1d1),
                ("Content-Type", "text/html;charset=utf-8"),
                ("Connection", "close")
            ]
        }
    },
    "1.2": {
        "HEAD": {
            "response_code": 200,
            "response": "OK",
            "headers": [
                ("Vary", "accept-datetime"),
                ("Content-Location", "%s/1.2/?version=20010320133610" % where),
                ("Memento-Datetime", "Tue, 20 Mar 2001 13:36:10 GMT"),
                ("Link", link_1d2),
                ("Content-Type", "text/html;charset=utf-8"),
                ("Connection", "close")
            ]
        },
        "GET": {
            "response_code": 200,
            "response": "OK",
            "headers": [
                ("Vary", "accept-datetime"),
                ("Content-Location", "%s/1.2/?version=20010320133610" % where),
                ("Memento-Datetime", "Tue, 20 Mar 2001 13:36:10 GMT"),
                ("Link", link_1d2),
                ("Content-Type", "text/html;charset=utf-8"),
                ("Connection", "close")
            ]
        },
        "uri-t": "%s/1.2/?version=all&style=timemap"%where
    },
    "1.3": {
        "HEAD": {
            "response_code": 200,
            "response": "OK",
            "headers": [
                ("Vary", "accept-datetime"),
                ("Memento-Datetime", "Tue, 20 Mar 2001 13:36:10 GMT"),
                ("Link", link_1d3),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ]
        },
        "GET": {
            "response_code": 200,
            "response": "OK",
            "headers": [
                ("Vary", "accept-datetime"),
                ("Memento-Datetime", "Tue, 20 Mar 2001 13:36:10 GMT"),
                ("Link", link_1d3),
                ("Content-Type", "text/html;charset=utf-8"),
                ("Connection", "close")
            ]
        }
    },
    "2.1": {
        "HEAD": {
            "headers": [
                ("Link", head_link_2d1),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
        "GET": {
            "headers": [
                ("Link", head_link_2d1),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        }
    },
    "2.1-timegate": {
        "HEAD": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Location", "%s/2.1-archive/web/20010321203610/%s/2.1/" % (where, where)),
                ("Link", head_link_2d1_timegate),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 302,
            "response": "Found",
        },
        "GET": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Location", "%s/2.1-archive/web/20010321203610/%s/2.1/" % (where, where)),
                ("Link", head_link_2d1_timegate),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 302,
            "response": "Found",
        }
    },
    "2.1-m": {
        "HEAD": {
            "headers": [
                ("Memento-Datetime", "Wed, 21 Mar 2001 20:36:10 GMT"),
                ("Link", link_2d1m),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
        "GET": {
            "headers": [
                ("Memento-Datetime", "Wed, 21 Mar 2001 20:36:10 GMT"),
                ("Link", link_2d1m),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        }
    },
    "2.2-timegate": {
        "HEAD": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Content-Location", "%s/2.2-archive/web/20010321203610/%s/2.2/" % (where, where)),
                ("Memento-Datetime", "Wed, 21 Mar 2001 20:36:10 GMT"),
                ("Link", link_2d2_timegate),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
        "GET": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Content-Location", "%s/2.2-archive/web/20010321203610/%s/2.2/" % (where, where)),
                ("Memento-Datetime", "Wed, 21 Mar 2001 20:36:10 GMT"),
                ("Link", link_2d2_timegate),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        }
    },
    "2.2": {
        "HEAD": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Link", link_2d2),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
        "GET": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Link", link_2d2),
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
    },
    "2.3": {
        "HEAD": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Link", link_2d3),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
        "GET": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Link", link_2d3),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
    },
    "2.3-timegate": {
        "HEAD": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Memento-Datetime", "Wed, 21 Mar 2001 20:36:10 GMT"),
                ("Link", link_2d3_timegate),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
        "GET": {
            "headers": [
                ("Vary", "accept-datetime"),
                ("Memento-Datetime", "Wed, 21 Mar 2001 20:36:10 GMT"),
                ("Link", link_2d3_timegate),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        }
    },
    "3": {
        "HEAD": {
            "headers": [
                ("Memento-Datetime", "Fri, 20 Mar 2009 11:00:00 GMT"),
                ("Link", link_3),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
        "GET": {
            "headers": [
                ("Memento-Datetime", "Fri, 20 Mar 2009 11:00:00 GMT"),
                ("Link", link_3),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
    },
    "4": {
        "HEAD": {
            "headers": [
                ("Memento-Datetime", "Wed, 21 Mar 2001 20:36:10 GMT"),
                ("Link", link_4),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
        "GET": {
            "headers": [
                ("Memento-Datetime", "Wed, 21 Mar 2001 20:36:10 GMT"),
                ("Link", link_4),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 200,
            "response": "OK",
        },
    },
    "5.2": {
        "HEAD": {
            "headers": [
                ("Link", link_5d2),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 404,
            "response": "Not Found",
        },
        "GET": {
            "headers": [
                ("Link", link_5d2),
                
                ("Content-Type", "text/plain; charset=UTF-8"),
                ("Connection", "close")
            ],
            "response_code": 404,
            "response": "Not Found",
        },
    },
    "5.4": {
        "initial-redirect": {
            "HEAD": {
                "headers": [
                    ("Location", "%s/5.4b/"),
                    
                    ("Content-Type", "text/plain; charset=UTF-8"),
                    ("Connection", "close")
                ],
                "response_code": 301,
                "response": "Moved Permanently",
            },
            "GET": {
                "headers": [
                    ("Location", "%s/5.4b/"),
                    
                    ("Content-Type", "text/plain; charset=UTF-8"),
                    ("Connection", "close")
                ],
                "response_code": 301,
                "response": "Moved Permanently",
            },
        },
        "5.4b-original": {
            "HEAD": {
                "headers": [
                    ("Memento-Datetime", "Fri, 11 Apr 2008 00:06:50 GMT"),
                    ("Location", "%s/5.4b/"),
                    ("Link", link_5d4b),
                    
                    ("Content-Type", "text/plain; charset=UTF-8"),
                    ("Connection", "close")
                ],
                "response_code": 301,
                "response": "Moved Permanently",
            },
            "GET": {
                "headers": [
                    ("Memento-Datetime", "Fri, 11 Apr 2008 00:06:50 GMT"),
                    ("Location", "%s/5.4b/"),
                    ("Link", link_5d4b),
                    
                    ("Content-Type", "text/plain; charset=UTF-8"),
                    ("Connection", "close")
                ],
                "response_code": 301,
                "response": "Moved Permanently",
            },
        },
        "5.4b-memento": {
            "HEAD": {
                "headers": [
                    ("Memento-Datetime", "Fri, 11 Apr 2008 00:06:50 GMT"),
                    ("Location", "%s/5.4-archive/20080411000655/%s/5.4"),
                    ("Link", link_5d4b),
                    
                    ("Content-Type", "text/plain; charset=UTF-8"),
                    ("Connection", "close")
                ],
                "response_code": 301,
                "response": "Moved Permanently",
            },
            "GET": {
                "headers": [
                    ("Memento-Datetime", "Fri, 11 Apr 2008 00:06:50 GMT"),
                    ("Location", "%s/5.4-archive/20080411000655/%s/5.4"),
                    ("Link", link_5d4b),
                    
                    ("Content-Type", "text/plain; charset=UTF-8"),
                    ("Connection", "close")
                ],
                "response_code": 301,
                "response": "Moved Permanently",
            },
        },
    },
    "5.5": {
        "HEAD": {
            "headers": [
                ("Memento-Datetime", "Fri, 11 Apr 2008 00:06:50 GMT"),
                ("Link", head_link_5d5),
                ("Connection", "close")
            ],
            "response_code": 404,
            "response": "Not Found",
        },
        "GET": {
            "headers": [
                ("Connection", "close")
            ],
            "response_code": 404,
            "response": "Not Found",
        }
    },
}


class P1D1:
    """
       This class holds the headers for pattern 4.1.1
       and the methods to get them
    """
    headers = ph['1.1']
    pnum = "1.1"
    timemap = tm1d1

    @classmethod
    def default(cls, set_header, set_status):
        d = cls.headers['default']
        for hk, hv in d["headers"]:
            set_header(hk, hv)
        set_status(d['response_code'], d['response'])

    @classmethod
    def get_headers(cls, set_header, set_status):
        g = cls.headers['GET']
        for hk, hv in g["headers"]:
            set_header(hk, hv)
        set_status(g['response_code'], g['response'])

    @classmethod
    def is_memento_uri(cls, urir):
        r_urir = cls.headers['GET']["uri-r_required"]
        return r_urir == urir

    @classmethod
    def head_headers(cls, set_header, set_status):
        h = cls.headers['HEAD']
        for hk, hv in h["headers"]:
            set_header(hk, hv)
        set_status(h['response_code'], h['response'])

    @classmethod
    def head_timegate_response(cls, http_handler):
        h = cls.headers["timegate"]
        for hk, hv in h["headers"]:
            http_handler.set_header(hk, hv)
        http_handler.set_status(h['response_code'], h['response'])


class P1D2:
    headers = ph['1.2']
    pnum = "1.2"
    timemap = tm1d2

    @classmethod
    def default(cls, set_header, set_status):
        d = cls.headers['default']
        for hk, hv in d["headers"]:
            set_header(hk, hv)
        set_status(d['response_code'], d['response'])

    @classmethod
    def get_headers(cls, set_header, set_status):
        g = cls.headers['GET']
        for hk, hv in g["headers"]:
            set_header(hk, hv)
        set_status(g['response_code'], g['response'])

    @classmethod
    def is_memento_uri(cls, urir):
        r_urir = cls.headers['GET']["uri-r_required"]
        return r_urir == urir

    @classmethod
    def is_timemap_uri(cls, urir):
        r_urir = cls.headers["uri-t"]
        return r_urir == urir

    @classmethod
    def head_headers(cls, set_header, set_status):
        h = cls.headers['HEAD']
        for hk, hv in h["headers"]:
            set_header(hk, hv)
        set_status(h['response_code'], h['response'])

    @classmethod
    def head_timegate_response(cls, http_handler):
        h = cls.headers["timegate"]
        for hk, hv in h["headers"]:
            http_handler.set_header(hk, hv)
        http_handler.set_status(h['response_code'], h['response'])


class P1D3:
    headers = ph['1.3']
    pnum = "1.3"
    timemap = tm1d3

    @classmethod
    def get_headers(cls, set_header, set_status):
        g = cls.headers['GET']
        for hk, hv in g["headers"]:
            set_header(hk, hv)
        set_status(g['response_code'], g['response'])

    @classmethod
    def is_memento_uri(cls, urir):
        r_urir = cls.headers['GET']["uri-r_required"]
        return r_urir == urir

    @classmethod
    def is_timemap_uri(cls, urir):
        r_urir = cls.headers["uri-t"]
        return r_urir == urir

    @classmethod
    def head_headers(cls, set_header, set_status):
        h = cls.headers['HEAD']
        for hk, hv in h["headers"]:
            set_header(hk, hv)
        set_status(h['response_code'], h['response'])


class P2D1GATE:
    headers = ph['2.1-timegate']
    pnum = "2.1-timegate"

    @classmethod
    def head_headers(cls, http_handler):
        h = cls.headers['HEAD']
        for hk, hv in h["headers"]:
            http_handler.set_header(hk, hv)
        http_handler.set_status(h['response_code'], h['response'])
