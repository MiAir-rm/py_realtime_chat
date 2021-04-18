import os
import sys
import logging
from .common import console_entry
from argparse import ArgumentParser
from argparse import FileType

from .twitcast import ChatDownloader 

def initArgumentParser(ap):
    ap.add_argument('url', help = '视频网址')
    ap.add_argument('--output', help = '输出文件(默认stdout)', 
        type = FileType('w', encoding='utf-8'), default = sys.stdout)
    ap.add_argument('--format', help = '输出内容格式(默认ass)',
        choices = ['csv', 'ass'])
    return ap

@console_entry(initArgumentParser)
def main(ap):
    session = ChatDownloader()
    chats = session.run(ap.url)
    if ap.format == 'csv':
        chats.to_csv(ap.output)
    elif ap.format == 'ass':
        chats.to_ass(ap.output)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])