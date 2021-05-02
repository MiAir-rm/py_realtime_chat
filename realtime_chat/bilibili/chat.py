import websocket
import json
import logging

import asyncio
from threading import Thread
from threading import Event

from realtime_chat.bilibili import blivedm
from realtime_chat.bilibili import common
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

    def get_room_id(self, url):
        short_id = [p for p in url.split('/') if p != ''][-1]
        data = common.getRoomInfo(short_id)
        self.short_id = short_id
        return data['data']['room_id']

    def isLive(self):
        data = common.getRoomInfo(self.short_id)
        return data['data']['live_status'] == 1

    def run(self, url):
        roomid = self.get_room_id(url)
        
        self._loop = asyncio.get_event_loop()
        session = blivedm.BLiveClient(roomid, loop=self._loop)
        session._on_receive_danmaku = lambda command: self._on_receive_danmaku(session, command)
        session._on_super_chat = lambda command: self._on_super_chat(session, command)
        session._on_receive_popularity = lambda command: self._on_receive_popularity(session, command)
        future = session.start()

        t = Thread(target = self.run_future, args= (future,))
        t.setDaemon(True)
        t.start()

        return self.__chats

    def run_future(self, future):
        asyncio.set_event_loop(self._loop)
        self._loop.run_forever()


    async def _on_receive_danmaku(self, bLiveClient, danmaku: blivedm.DanmakuMessage):
        chat = Chat(
            uid = danmaku.uid,
            username = danmaku.uname,
            timestamp = danmaku.timestamp / 1000,
            message = danmaku.msg
        )
        self.__chats.put(chat)

    async def _on_super_chat(self, bLiveClient, message: blivedm.SuperChatMessage):
        chat = Chat(
            uid = SuperChatMessage.uid,
            username = SuperChatMessage.uname,
            timestamp = SuperChatMessage.start_time / 1000,
            message = SuperChatMessage.message
        )
        self.__chats.put(chat)

    async def _on_receive_popularity(self, bLiveClient, popularity: int):
        if popularity == 1 and not self.isLive():
            self.__chats.close()
            bLiveClient.close()