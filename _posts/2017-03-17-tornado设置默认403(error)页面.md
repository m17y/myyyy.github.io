# coding=utf-8
# ---
# layout: post
# title: tornado设置默认403(error页面)!
# tags: ["tornado"]
# description: 不断的学习，越努力越幸福。
# ---
import os
import tornado
import tornado.options
import tornado.httpserver
from tornado.web import RequestHandler
from tornado.options import define, options

define("port", default=1994, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self,status_code,**kwargs):
        if status_code == 403 or 405:
            self.write(dict(status = False,
                data = '对不起，你没有权限访问该页面；如需帮助，请联系管理员 '))
        else:
            self.get_error_html(status_code,**kwargs)

    def get_error_html(self, status_code, **kwargs):
        template_name = "{0}.html".format(status_code)
        if not exists(template_path(template_name)):
            template_name = "error.html"

        if not exists(template_path(template_name)):
            return self.write(str(status_code))

        kwargs.update(
            dict(status_code=status_code, message=responses[status_code]))

        self.render(template_name, **kwargs)

class IndexHandler(BaseHandler):
    def get(self):
        self.write('hello')

handlers = [ 
    (r'/index', IndexHandler),
    ]   

settings = { 
        'template_path': os.path.join(os.path.dirname(__file__), "templates"),
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        }

if __name__ == '__main__':
        tornado.options.parse_command_line()
        app = tornado.web.Application(handlers=handlers, **settings)
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        print(options.port)
        tornado.ioloop.IOLoop.instance().start()