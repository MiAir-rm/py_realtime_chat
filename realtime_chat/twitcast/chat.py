import twitcasting
import websocket
import json

from threading import Thread
from threading import Event 
from queue import Queue

from realtime_chat.common import Chat

class ChatDownloader(object):
    """docstring for ChatDownloader"""
    def __init__(self):
        super(ChatDownloader, self).__init__()
        self.__queue = Queue(-1)
        self.__close_event = Event()
        self.__close_event.clear()

    def get_video_id(self, url):
        user_id = [p for p in url.split('/') if p != ''][-1]
        return twitcasting.get_video_id(user_id)

    @property
    def chats(self):
        while True:
            yield self.__queue.get()

    def run(self, url):
        self.__cached_url = url
        video_id = self.get_video_id(url)
        sock_address = twitcasting.get_event_pubsub_url(video_id)
        app = websocket.WebSocketApp(
            sock_address,
            on_open = self.__on_open,
            on_message = self.__on_message,
            on_error = self.__on_error,
            on_close = self.__on_close,
        )
        t = Thread(target=app.run_forever, args=tuple())
        t.setDaemon(True)
        t.start()
        return self.chats

    def __on_open(self, ws):
        pass

    def __on_message(self, ws, message):
        try:
            if message == "[]":
                return
            
            datas = json.loads(message)
            for data in datas:
                chat = Chat(
                    uid = data['author']['id'],
                    username = data['author']['name'],
                    timestamp = data['createdAt'],
                    message = data['message']
                )
                self.__queue.put(chat)
        except Exception as ex:
            pass

    def __on_error(self, ws, error):
        self.__close_event.set()

    def __on_close(self, ws):
        self.__close_event.set()
    
