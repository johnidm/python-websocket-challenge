import os

import tornado.ioloop
import tornado.web
import tornado.websocket

import datetime


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')


class ChatHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('chatroom.html')


class WebSocketChatRoomHandler(tornado.websocket.WebSocketHandler):

    clients = set()

    def open(self):
        WebSocketChatRoomHandler.clients.add(self)

    def on_close(self):
        WebSocketChatRoomHandler.clients.remove(self)

    def on_message(self, message):
        body = tornado.escape.json_decode(message)

        chat = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "message": body["message"],
            "avatar": body["avatar"],
        }

        response = tornado.escape.json_encode(chat)
        for client in WebSocketChatRoomHandler.clients:
            if client != self: # ignore self-message
                client.write_message(response)


class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        handlers = [
            (r'/', IndexHandler),
            (r'/chat', ChatHandler),
            (r'/chatroom', WebSocketChatRoomHandler),
            (r'/images/(.*)',tornado.web.StaticFileHandler, {'path': os.path.join(settings['static_path'], 'images')},),
        ]
        
        super(Application, self).__init__(handlers, **settings)


def main():
    app = Application()
    port = int(os.environ.get("PORT", 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
