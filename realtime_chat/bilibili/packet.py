import json
import struct

import common

class Packet(object):
    """docstring for Packet"""
    packet_type = common.OPR_NORMAL

    def __init__(self):
        super(Packet, self).__init__()
        self.data = {}
    
    def to_bytes(self):
        str_data = json.dumps(self.data, separators=(',',':'))
        data = str_data.encode()
        size = common.HEAD_SIZE + len(data)

        head = [
            size,
            common.HEAD_SIZE,
            common.VERSION,
            self.packet_type,
            common.SEQ
        ]
        return struct.pack(common.HEAD_FORMAT, *head) + data


if __name__ == '__main__':
    p = Packet()
    p.data['uid'] = 293793435
    p.data['roomid'] = 21686237
    p.data['protover'] = 2
    p.data['platform'] = 'web'
    p.data['clientver'] = '1.10.3'
    p.data['type'] = 2
    p.data['key'] = 'CoKh_aIFBlQ2LWwdyNCk-i_BvrdrrUM2xWltb5wkTPNrDUI-sF2AVVODxCRB9idvt4F2MP1EJlMhIWk1Zisgn2ggflhrenOKe9zVemx5z_ZMCaUwL1epmzZS'
    p.data['clientver'] = '1.10.3'
    print(p.to_bytes())


