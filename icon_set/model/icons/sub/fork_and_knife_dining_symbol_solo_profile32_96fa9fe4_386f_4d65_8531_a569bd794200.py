"""Independent 32px profile of fork-and-knife-dining-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '96fa9fe4-386f-4d65-8531-a569bd794200'
SOURCE_PATH = 'pictographic-primitives/state/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('96fa9fe4-386f-4d65-8531-a569bd794200', 'pictographic-primitives/state/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fork-and-knife-dining-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('fork-and-knife-dining-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '49724c00817f2a191a568b756b87affadf10176d432cf5172660d50da0d24c68'

class Drawing(Sub32):
    icon_id = 'fork-and-knife-dining-symbol-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (10, 10), (10, 15))
        self.add_line('p2-r1-2', (10, 15), (13, 18))
        self.add_line('p2-r1-3', (13, 18), (16, 15))
        self.add_line('p2-r1-4', (16, 15), (16, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (13, 18), (13, 23))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 11), (22, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
