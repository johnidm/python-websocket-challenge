import tornado
import app

from tornado.testing import AsyncHTTPTestCase


class TestHTTPHandler(AsyncHTTPTestCase):

    def get_app(self):
        return app.Application()

    def test_index_page(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)

        self.assertIn('Chat Room Interview', response.body)
        self.assertIn('click any button to open the chat room', response.body)
        self.assertIn('/chat', response.body)
        self.assertIn('index.css', response.body)

    def test_chat_page(self):
        response = self.fetch('/chatroom')
        self.assertEqual(response.code, 200)

        self.assertIn('normalize.css', response.body)
        self.assertIn('chatroom.css', response.body)
        self.assertIn('Welcome to Chat Room', response.body)
        self.assertIn('chatroom.js', response.body)

    @tornado.testing.gen_test
    def test_websocket(self):
        ws_url = "ws://localhost:" + str(self.get_http_port()) + "/chat"
        ws_client = yield tornado.websocket.websocket_connect(ws_url)

        message = {
            "message": "Hi,",
            "uuid": "8sdssodf8yhguUBJHBJUFODUS",
            "avatar": "images/ko.png",
        }

        ws_client.write_message(tornado.escape.json_encode(message))

        response_body = yield ws_client.read_message()
        response_data = tornado.escape.json_decode(response_body)

        self.assertEqual(response_data['message'], message['message'])
        self.assertEqual(response_data['uuid'], message['uuid'])
        self.assertEqual(response_data['avatar'], message['avatar'])
        self.assertTrue('date' in response_data)
