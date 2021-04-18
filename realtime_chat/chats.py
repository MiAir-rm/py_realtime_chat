from threading import Thread
from threading import Event

from datetime import datetime

class Chat(object):
    """docstring for Chat"""
    def __init__(self, uid, username, timestamp, message):
        super(Chat, self).__init__()
        self.uid = uid
        self.username = username
        self.timestamp = timestamp
        self.message = message


class Chats(object):
    """docstring for Chats"""
    def __init__(self):
        super(Chats, self).__init__()
        self.__close_event = Event()
        self.__close_event.clear()
        self.__update_event = Event()
        self.__update_event.clear()
        self.__chats = []
        self.__start_timestamp = None

    @property
    def chats(self):
        index = 0

        # 先导出缓冲区内容
        for c in self.__chats:
            yield c
            index += 1

        while not self.__close_event.isSet():
            if index < len(self.__chats):
                yield self.__chats[index]
                index += 1
            else:
                self.__update_event.clear()
                self.__update_event.wait()

    @property
    def start_timestamp(self):
        if self.__start_timestamp is None:
            self.__start_timestamp = next(self.chats).timestamp
        return self.__start_timestamp

    def close(self):
        self.__close_event.set()

    def put(self, value):
        self.__update_event.set()
        self.__chats.append(value)

    def to_ass(self, fp):
        start_timestamp = self.start_timestamp
        to_time = lambda x: '%02d:%02d:%02d' % (x // 3600, x % 3600 // 60, x % 60 // 1)
        dialogue = '\nDialogue: 0,%s.00,%s.00,Default,,0,0,0,,%s'
        datas = ((c.timestamp - start_timestamp, c.message) for c in self.chats)
        datas = (dialogue % (to_time(t), to_time(t + 3 + len(s) // 8), s) for t, s in datas)

        fp.write('[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text')
        for d in datas:
            fp.write(d)

    def to_csv(self, fp):
        datas = ('%d,"%s",%s,"%s"\n' % 
            (c.timestamp, c.username, c.uid, c.message) for c in self.chats)
        for d in datas:
            fp.write(d)



