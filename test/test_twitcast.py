import unittest
import re
import requests as rq
import sys

from realtime_chat.twitcast import ChatDownloader
from realtime_chat.chats import Chat

class TestTwitcastingChat(unittest.TestCase):

    def setUp(self):
        resp = rq.get('https://twitcasting.tv/')
        video_info = re.findall('<a href="/(\S+)/movie/(\d+)" class="tw-movie">', resp.text)
        self.user_id = video_info[0][0]
        self.video_id = int(video_info[0][1])
        self.url = 'https://twitcasting.tv/{user_id}'.format(user_id = self.user_id)

    def test_chat(self):
        session = ChatDownloader()
        chats = session.run(self.url)
        data = next(chats)
        self.assertIsInstance(data, Chat)

    def test_video_id(self):
        session = ChatDownloader()
        video_id = session.get_video_id(self.url)
        self.assertEqual(video_id, self.video_id)


if __name__ == "__main__":
    unittest.main()