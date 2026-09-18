"""Independent 32px profile of shield-check.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '35439928-bf3d-41d0-ac20-63c8b05f2354'
SOURCE_PATH = 'pictographic-primitives/apps/shield check_35439928-bf3d-41d0-ac20-63c8b05f2354.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('35439928-bf3d-41d0-ac20-63c8b05f2354', 'pictographic-primitives/apps/shield check_35439928-bf3d-41d0-ac20-63c8b05f2354.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shield-check',)
SOLO_SOURCE_ICON_IDS = ('shield-check',)
REFERENCE_EXPORT_SHA256 = '3c5eb57a8110eceb8f7e75e4e68dc9706319263a1dcf8f15d8b792878c03d30d'

class Drawing(Sub32):
    icon_id = 'shield-check-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'apps'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (21, 13), (14, 20))
        self.add_line('p1-r1-2', (14, 20), (11, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (5, 6), ((7, 5), (10, 5), (12, 4)))
        self.add_bezier('p2-r1-2', (12, 4), ((13, 4), (16, 2), (16, 2)))
        self.add_bezier('p2-r1-3', (16, 2), ((16, 2), (16, 2), (16, 2)))
        self.add_bezier('p2-r1-4', (16, 2), ((16, 2), (16, 2), (16, 2)))
        self.add_bezier('p2-r1-5', (16, 2), ((17, 2), (19, 3), (19, 3)))
        self.add_bezier('p2-r1-6', (19, 3), ((22, 5), (24, 6), (27, 7)))
        self.add_line('p2-r1-7', (27, 7), (27, 16))
        self.add_bezier('p2-r1-8', (27, 16), ((27, 16), (27, 17), (27, 17)))
        self.add_bezier('p2-r1-9', (27, 17), ((27, 18), (27, 18), (27, 19)))
        self.add_bezier('p2-r1-10', (27, 19), ((26, 23), (23, 26), (20, 28)))
        self.add_bezier('p2-r1-11', (20, 28), ((19, 29), (17, 30), (16, 30)))
        self.add_bezier('p2-r1-12', (16, 30), ((16, 30), (16, 30), (16, 30)))
        self.add_bezier('p2-r1-13', (16, 30), ((16, 30), (16, 30), (16, 30)))
        self.add_bezier('p2-r1-14', (16, 30), ((15, 30), (13, 28), (12, 28)))
        self.add_bezier('p2-r1-15', (12, 28), ((9, 26), (7, 23), (5, 20)))
        self.add_bezier('p2-r1-16', (5, 20), ((5, 19), (5, 18), (5, 17)))
        self.add_bezier('p2-r1-17', (5, 17), ((5, 17), (5, 17), (5, 17)))
        self.add_bezier('p2-r1-18', (5, 17), ((5, 17), (5, 17), (5, 17)))
        self.add_line('p2-r1-19', (5, 17), (5, 6))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', 'p2-r1-13', 'p2-r1-14', 'p2-r1-15', 'p2-r1-16', 'p2-r1-17', 'p2-r1-18', 'p2-r1-19', closed=False)
