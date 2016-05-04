import fnmatch
import os

from tornado.options import options

from config import TIMEMAP_PATH, TIMEMAP_TEMPLATE_PATH


def generate_configured_timemaps():
    where = "localhost:%d" % options.port

    for path, dirs, files in os.walk(os.path.abspath(TIMEMAP_TEMPLATE_PATH)):
        for filename in fnmatch.filter(files, "*.timemap"):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace("{$replace}", where)

            with open(os.path.join(TIMEMAP_PATH, filename), "w+") as out:
                out.write(s)
