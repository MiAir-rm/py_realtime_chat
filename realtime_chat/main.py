import os
import sys
import logging
from .common import console_entry
from argparse import ArgumentParser
from argparse import FileType

from .twitcast import ChatDownloader as TcChatDownloader
from .youtube import ChatDownloader as YtbChatDownloader
from .bilibili import ChatDownloader as BLiveChatDownloader

def initArgumentParser(ap):
    ap.add_argument('url', help = '视频网址')
    ap.add_argument('--output', help = '输出文件(默认stdout)', 
        type = FileType('w', encoding='utf-8'), default = sys.stdout)
    ap.add_argument('--format', help = '输出内容格式(默认csv)',
        choices = ['csv', 'ass'], default = 'csv')
    return ap

@console_entry(initArgumentParser)
def main(ap):
    if 'youtube' in ap.url:
        chatDownloader = YtbChatDownloader()
    elif 'twitcasting' in ap.url:
        chatDownloader = TcChatDownloader()
    elif 'bilibili' in ap.url:
        chatDownloader = BLiveChatDownloader()
    chats = chatDownloader.run(ap.url)
    if ap.format == 'csv':
        chats.to_csv(ap.output)
    elif ap.format == 'ass':
        chats.to_ass(ap.output)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])