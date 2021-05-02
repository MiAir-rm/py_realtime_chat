import unittest
import re
import sys

from realtime_chat.bilibili import ChatDownloader
from realtime_chat.bilibili.common import getRoomInfo, getRoomId
from realtime_chat.chats import Chat

class TestBilibiliChat(unittest.TestCase):

    def setUp(self):
        self.url = 'https://live.bilibili.com/21320551'
        self.short_id = 12235923
        self.mid = 349991143

    def test_common(self):
        room_info = getRoomInfo(self.short_id)
        self.assertIn("data", room_info.keys())
        self.assertIn("room_id", room_info['data'].keys())

    def test_chat(self):
        session = ChatDownloader()
        room_id = session.get_room_id(self.url)
        self.assertEqual(room_id, 21320551)
        self.assertTrue(session.isLive())
        session.run(self.url)
        data = next(session.chats)
        self.assertIsInstance(data, Chat)


if __name__ == "__main__":
    unittest.main()