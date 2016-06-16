import os
import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello world')


class WebSocketChatHandler():
    pass


class Application(tornado.web.Application):
    
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/chat", WebSocketChatHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        super(Application, self).__init__(handlers, **settings)


def main():
    app = Application()
    port = int(os.environ.get("PORT", 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()