import os
import sys
import logging
from common import console_entry
from argparse import ArgumentParser

def initArgumentParser(ap):
    # ap.add_argument()
    return ap

@console_entry(initArgumentParser)
def main(ap):
    pass


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])