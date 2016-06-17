from tornado.testing import AsyncHTTPTestCase
import app


class TestHandlerHTTP(AsyncHTTPTestCase):

    def get_app(self):
        return app.Application()

    def test_index_page(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)

        self.assertIn('Chat Room Interview', response.body)
        self.assertIn('click any button to open chat room', response.body)
        self.assertIn('/chat', response.body)
        self.assertIn('index.css', response.body)

    def test_chat_page(self):
        response = self.fetch('/chat')
        self.assertEqual(response.code, 200)

        self.assertIn('normalize.css', response.body)
        self.assertIn('chatroom.css', response.body)
        self.assertIn('Welcome to Chat Room', response.body)
        self.assertIn('chatroom.js', response.body)
