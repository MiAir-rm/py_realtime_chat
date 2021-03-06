import unittest
import os
import re
import requests as rq


from realtime_chat.main import main

class TestMain(unittest.TestCase):
    """docstring for TestMain"""

    def setUpClass():
        f = './test/temp/TestMain.ass'
        if os.path.isfile(f):
            os.remove(f)

    def setUp(self):
        resp = rq.get('https://twitcasting.tv/')
        video_info = re.findall('<a href="/(\S+)/movie/(\d+)" class="tw-movie">', resp.text)
        self.user_id = video_info[0][0]
        self.video_id = int(video_info[0][1])
        self.url = 'https://twitcasting.tv/{user_id}'.format(user_id = self.user_id)
        self.ytb_url = 'https://www.youtube.com/watch?v=xyHLAcDtCwE'

    @unittest.skip('block for test')
    def test_twitcasting_to_ass(self):
        main('%s --output ./test/temp/TestMain.ass --format ass' % self.url)

    def test_youtube_to_ass(self):
        main('%s --output ./test/temp/TestMain.csv --format csv' % self.ytb_url)


if __name__ == "__main__":
    unittest.main()