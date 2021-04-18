import sys
import logging
from collections import namedtuple

def console_entry(initArgumentParser):
    import sys
    def decorate(func):
        from functools import wraps
        @wraps(func)
        def www(argv = None):
            from argparse import ArgumentParser, Namespace
            if isinstance(argv, str):
                argv = argv.split()
            elif argv is None:
                argv = sys.argv[1:]
            if isinstance(argv, list):
                try:
                    ap = ArgumentParser()
                    ap = initArgumentParser(ap)
                    ap_args = ap.parse_args(argv)
                except Exception as e:
                    ap.print_help()
                    sys.exit(0)
            elif isinstance(argv, Namespace):
                ap_args = argv
            else:
                ap.print_help()
                sys.exit(0)
            try:
                return func(ap_args)
            except Exception as e:
                logging.exception(e);
        return www
    return decorate

def create_sub_parser(subparsers, title, name, docs, init_ap):
    ap = subparsers.add_parser(name, help = docs)
    ap.add_argument('--' + title, default = name)
    init_ap(ap)
    return subparsers


class Chat(object):
    """docstring for Chat"""
    def __init__(self, uid, username, timestamp, message):
        super(Chat, self).__init__()
        self.uid = uid
        self.username = username
        self.timestamp = timestamp
        self.message = message
