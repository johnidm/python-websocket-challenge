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
        self.render('chat.html')


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
            "user": body["user"],
        }
        
        response = tornado.escape.json_encode(chat)
        for client in WebSocketChatRoomHandler.clients:
            client.write_message(response)


class Application(tornado.web.Application):
    
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/chat", ChatHandler),
            (r"/chatroom", WebSocketChatRoomHandler),
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