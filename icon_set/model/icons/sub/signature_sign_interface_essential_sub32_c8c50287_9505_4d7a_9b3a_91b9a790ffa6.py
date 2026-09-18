"""Independent 32px profile of signature-sign-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c8c50287-9505-4d7a-9b3a-91b9a790ffa6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/signature sign_c8c50287-9505-4d7a-9b3a-91b9a790ffa6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8c50287-9505-4d7a-9b3a-91b9a790ffa6', 'pictographic-primitives/interface-essential/signature sign_c8c50287-9505-4d7a-9b3a-91b9a790ffa6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/signature-sign-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('signature-sign-interface-essential',)
REFERENCE_EXPORT_SHA256 = '68d19f827c26741ee8476de576396b8a5579d08f2f840118b92d79a834ac3d01'

class Drawing(Sub32):
    icon_id = 'signature-sign-interface-essential-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 27), (10, 9))
        self.add_bezier('p1-r1-2', (10, 9), ((12, 5), (13, 5), (15, 5)))
        self.add_bezier('p1-r1-3', (15, 5), ((15, 5), (15, 5), (15, 5)))
        self.add_bezier('p1-r1-4', (15, 5), ((17, 5), (17, 6), (17, 7)))
        self.add_bezier('p1-r1-5', (17, 7), ((17, 9), (15, 13), (14, 16)))
        self.add_bezier('p1-r1-6', (14, 16), ((12, 20), (11, 23), (11, 25)))
        self.add_bezier('p1-r1-7', (11, 25), ((11, 26), (12, 27), (13, 27)))
        self.add_bezier('p1-r1-8', (13, 27), ((16, 27), (20, 16), (22, 16)))
        self.add_bezier('p1-r1-9', (22, 16), ((23, 15), (24, 15), (25, 15)))
        self.add_bezier('p1-r1-10', (25, 15), ((26, 15), (26, 15), (26, 16)))
        self.add_bezier('p1-r1-11', (26, 16), ((26, 18), (26, 19), (25, 21)))
        self.add_bezier('p1-r1-12', (25, 21), ((24, 22), (24, 24), (24, 25)))
        self.add_bezier('p1-r1-13', (24, 25), ((24, 26), (25, 27), (26, 27)))
        self.add_bezier('p1-r1-14', (26, 27), ((29, 27), (29, 25), (30, 24)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
