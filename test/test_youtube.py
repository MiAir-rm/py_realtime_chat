import unittest
import re
import requests as rq
import sys

from realtime_chat.youtube import ChatDownloader
from realtime_chat.chats import Chat

class TestTwitcastingChat(unittest.TestCase):

    def setUp(self):
        self.url = 'https://www.youtube.com/watch?v=xyHLAcDtCwE'

    def test_chat(self):
        session = ChatDownloader()
        session.run(self.url)
        data = next(session.chats)
        self.assertIsInstance(data, Chat)


if __name__ == "__main__":
    unittest.main()