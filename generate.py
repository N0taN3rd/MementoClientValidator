import fnmatch
import os

from tornado.options import options

def generate_configured_timemaps():
    where = "localhost:%d" % options.port
    dirname = os.path.dirname(__file__)
    timemap_path = os.path.join(dirname, 'timemaps')
    if not os.path.exists(timemap_path):
        os.mkdir(timemap_path)
    timemap_template_path = os.path.join(dirname, 'timemap_templates')
    for path, dirs, files in os.walk(os.path.abspath(timemap_template_path)):
        for filename in fnmatch.filter(files, "*.timemap"):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace("{$replace}", where)

            with open(os.path.join(timemap_path, filename), "w+") as out:
                out.write(s)
