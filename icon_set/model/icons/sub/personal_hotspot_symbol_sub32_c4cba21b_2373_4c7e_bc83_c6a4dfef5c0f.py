"""Independent 32px profile of personal-hotspot-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f'
SOURCE_PATH = 'pictographic-primitives/symbol/personal hotspot_c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f', 'pictographic-primitives/symbol/personal hotspot_c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/personal-hotspot-symbol',)
SOLO_SOURCE_ICON_IDS = ('personal-hotspot-symbol',)
REFERENCE_EXPORT_SHA256 = '6b807b0b866d81159ae09ae242167260eea0adca3f12adfcc612443fea02d978'

class Drawing(Sub32):
    icon_id = 'personal-hotspot-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (20, 20), ((19, 21), (18, 21), (18, 21)))
        self.add_bezier('p1-r1-2', (18, 21), ((17, 21), (17, 22), (16, 22)))
        self.add_bezier('p1-r1-3', (16, 22), ((16, 22), (15, 21), (14, 21)))
        self.add_bezier('p1-r1-4', (14, 21), ((14, 21), (14, 21), (14, 21)))
        self.add_bezier('p1-r1-5', (14, 21), ((14, 21), (14, 21), (14, 21)))
        self.add_bezier('p1-r1-6', (14, 21), ((13, 21), (12, 21), (11, 21)))
        self.add_bezier('p1-r1-7', (11, 21), ((8, 20), (6, 17), (5, 14)))
        self.add_bezier('p1-r1-8', (5, 14), ((5, 14), (5, 13), (5, 13)))
        self.add_bezier('p1-r1-9', (5, 13), ((5, 13), (5, 13), (5, 13)))
        self.add_bezier('p1-r1-10', (5, 13), ((5, 12), (5, 12), (5, 12)))
        self.add_bezier('p1-r1-11', (5, 12), ((5, 9), (7, 5), (10, 3)))
        self.add_bezier('p1-r1-12', (10, 3), ((11, 3), (12, 2), (13, 2)))
        self.add_line('p1-r1-13', (13, 2), (21, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_line('p2-r1-1', (12, 30), (18, 30))
        self.add_bezier('p2-r1-2', (18, 30), ((18, 30), (18, 30), (18, 30)))
        self.add_bezier('p2-r1-3', (18, 30), ((18, 30), (18, 30), (18, 30)))
        self.add_bezier('p2-r1-4', (18, 30), ((18, 30), (18, 30), (18, 30)))
        self.add_bezier('p2-r1-5', (18, 30), ((23, 30), (27, 25), (27, 20)))
        self.add_bezier('p2-r1-6', (27, 20), ((27, 20), (27, 20), (27, 20)))
        self.add_bezier('p2-r1-7', (27, 20), ((27, 20), (27, 20), (27, 20)))
        self.add_bezier('p2-r1-8', (27, 20), ((27, 15), (23, 11), (19, 11)))
        self.add_line('p2-r1-9', (19, 11), (15, 11))
        self.add_bezier('p2-r1-10', (15, 11), ((14, 11), (13, 11), (12, 12)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
