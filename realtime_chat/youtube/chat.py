import websocket
import json
from threading import Thread
from threading import Event

from chat_downloader   import ChatDownloader as YtbChatDownloader

from realtime_chat.chats import Chat
from realtime_chat.chats import Chats

class ChatDownloader(object):
    """docstring for ChatDownloader"""
    def __init__(self):
        super(ChatDownloader, self).__init__()
        self.__chats = Chats()


    @property
    def chats(self):
        return self.__chats.chats

    def run(self, url):
        session = YtbChatDownloader()
        chats = session.get_chat(url = url)
        t = Thread(target=self.__put, args=(chats,))
        t.setDaemon(True)
        t.start()
        return self.__chats

    def __put(self, chats):
        for data in chats:
            chat = Chat(
                uid = data['author']['id'],

                username = data['author']['name'],
                timestamp = data['timestamp'] / 1000000,
                message = data['message']
            )
            self.__chats.put(chat)
        self.__chats.close()
