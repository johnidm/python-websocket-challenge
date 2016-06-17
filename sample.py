import tornado.ioloop
import tornado.web
import tornado.websocket


class Hello(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message("Hello, world")

    def on_message(self, message):
        pass

    def on_close(self):
        pass


class Main(tornado.web.RequestHandler):
    def get(self):
        # This could be a template, too.
        self.write('''
<script>
ws = new WebSocket("ws://localhost:8888/websocket");
ws.onmessage = function(e) {
    alert('message received: ' + e.data);
};
</script>''')


application = tornado.web.Application([
    (r"/", Main),
    (r"/websocket", Hello),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()