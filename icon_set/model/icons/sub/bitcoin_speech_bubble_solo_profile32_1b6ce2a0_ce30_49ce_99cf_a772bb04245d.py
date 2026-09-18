"""Independent 32px profile of bitcoin-speech-bubble-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1b6ce2a0-ce30-49ce-99cf-a772bb04245d'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b6ce2a0-ce30-49ce-99cf-a772bb04245d', 'pictographic-primitives/symbol/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'), ('692b5811-84ae-4db0-8d66-219feaafec3e', 'pictographic-primitives/symbol/messages bubble square bitcoin_692b5811-84ae-4db0-8d66-219feaafec3e.svg'))
PROFILE_SOURCE_KEYS = ('solo/bitcoin-speech-bubble-solo', 'solo/bitcoin-message-speech-bubble-solo')
SOLO_SOURCE_ICON_IDS = ('bitcoin-speech-bubble-solo', 'bitcoin-message-speech-bubble-solo')
REFERENCE_EXPORT_SHA256 = 'b73c31329ae01f27540a1ce72ce15f754c4ac94d8a3a365ecbe392c12cd61ff2'

class Drawing(Sub32):
    icon_id = 'bitcoin-speech-bubble-solo-profile32'
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
        self.add_line('p2-r1-1', (11, 9), (17, 9))
        self.add_arc('p2-r1-2', (17, 9), (17, 15), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (17, 15), (17, 20), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (17, 20), (11, 20))
        self.add_line('p2-r1-5', (11, 20), (11, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (11, 15), (17, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (11, 9), (11, 8))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (11, 20), (11, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (17, 9), (17, 8))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (17, 20), (17, 21))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p6-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p6-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p7-r1-1')
        self.relate("connect", 'p2-r1-4', 'p5-r1-1')
        self.relate("connect", 'p2-r1-4', 'p7-r1-1')
        self.relate("connect", 'p2-r1-5', 'p4-r1-1')
        self.relate("connect", 'p2-r1-5', 'p5-r1-1')
