"""Independent 32px profile of money-chat-bubble-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e2581dc8-469f-4d41-8bc1-20ad32b80072'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble square dollar sign_e2581dc8-469f-4d41-8bc1-20ad32b80072.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2581dc8-469f-4d41-8bc1-20ad32b80072', 'pictographic-primitives/symbol/messages bubble square dollar sign_e2581dc8-469f-4d41-8bc1-20ad32b80072.svg'), ('a0e713ab-5594-48b4-9fb9-5bd0a13657f4', 'pictographic-primitives/other/messages bubble round dollar sign_a0e713ab-5594-48b4-9fb9-5bd0a13657f4.svg'), ('93c99818-8211-47c5-bf92-9fa83e3cab72', 'pictographic-primitives/other/message dollar sign lines_93c99818-8211-47c5-bf92-9fa83e3cab72.svg'))
PROFILE_SOURCE_KEYS = ('solo/money-chat-bubble-solo', 'solo/dollar-sign-chat-bubble-solo', 'solo/money-message-bubble-solo')
SOLO_SOURCE_ICON_IDS = ('money-chat-bubble-solo', 'dollar-sign-chat-bubble-solo', 'money-message-bubble-solo')
REFERENCE_EXPORT_SHA256 = 'a0eb804bb7dcb76a17857cbff085f2d0c34ad5451f33cc871fe310fcb1e19a5e'

class Drawing(Sub32):
    icon_id = 'money-chat-bubble-solo-profile32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 2), (23, 2))
        self.add_arc('p1-r1-2', (23, 2), (27, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 6), (27, 23))
        self.add_arc('p1-r1-4', (27, 23), (23, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (23, 27), (12, 27))
        self.add_line('p1-r1-6', (12, 27), (5, 30))
        self.add_line('p1-r1-7', (5, 30), (5, 6))
        self.add_arc('p1-r1-8', (5, 6), (9, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (20, 9), (16, 9))
        self.add_arc('p2-r1-2', (16, 9), (16, 15), radius_x=4, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (16, 15), (16, 20), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (16, 20), (12, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, 8), (16, 9))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 20), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p4-r1-1')
        self.relate("connect", 'p2-r1-4', 'p4-r1-1')
