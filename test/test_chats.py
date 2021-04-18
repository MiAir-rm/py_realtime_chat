import unittest
import re
import requests as rq
import sys

from realtime_chat.chats import Chat,Chats


class TestChats(unittest.TestCase):

    def setUpClass():
        open('./test/temp/TestChats.ass', 'w', encoding='utf-8').close()
        open('./test/temp/TestChats.csv', 'w', encoding='utf-8').close()

    def setUp(self):
        self.chats = [
            Chat("1", 'test', 1618729300, 'TestChats'),
            Chat("1", 'test', 1618729301, 'TestChats'),
            Chat("1", 'test', 1618729309, 'TestChats'),
            Chat("1", 'test', 1618732000, 'TestChats')
        ]
        self.assfp = open('./test/temp/TestChats.ass', 'a', encoding='utf-8')
        self.csvfp = open('./test/temp/TestChats.csv', 'a', encoding='utf-8')

    def test_to_ass(self):
        chats = Chats()
        for c in self.chats:
            chats.put(c)
        chats.close()
        chats.to_ass(self.assfp)

    # @unittest.SkipTest
    def test_to_csv(self):
        chats = Chats()
        for c in self.chats:
            chats.put(c)
        chats.close()
        chats.to_csv(self.csvfp)

    def tearDown(self):
        self.assfp.close()
        self.csvfp.close()





if __name__ == "__main__":
    unittest.main()