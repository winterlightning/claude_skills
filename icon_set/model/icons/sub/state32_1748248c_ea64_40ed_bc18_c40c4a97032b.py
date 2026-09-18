"""Independent 32px profile of state32-1748248c-ea64-40ed-bc18-c40c4a97032b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1748248c-ea64-40ed-bc18-c40c4a97032b'
SOURCE_PATH = 'icon_set/assets/combination-state32/1748248c-ea64-40ed-bc18-c40c4a97032b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1748248c-ea64-40ed-bc18-c40c4a97032b', 'icon_set/assets/combination-state32/1748248c-ea64-40ed-bc18-c40c4a97032b.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '5f9240c2b43bed416d04fc82c435e4ff28968dabade99df256280b20f91a93d1'

class Drawing(Sub32):
    icon_id = 'state32-1748248c-ea64-40ed-bc18-c40c4a97032b'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (3, 17), ((3, 15), (4.333333333333334, 14), (7, 14)))
        self.add_bezier('p1-r1-2', (7, 14), ((13, 14), (15, 8), (16, 4)))
        self.add_bezier('p1-r1-3', (16, 4), ((17, 3), (18, 2), (19, 2)))
        self.add_bezier('p1-r1-4', (19, 2), ((21, 2), (23, 4), (23, 7)))
        self.add_bezier('p1-r1-5', (23, 7), ((23, 7), (23, 7), (23, 8)))
        self.add_line('p1-r1-6', (23, 8), (21, 14))
        self.add_line('p1-r1-7', (21, 14), (26, 14))
        self.add_bezier('p1-r1-8', (26, 14), ((28, 14), (29, 15), (29, 17)))
        self.add_bezier('p1-r1-9', (29, 17), ((29, 18.333333333333332), (28.666666666666668, 19.666666666666668), (28, 21)))
        self.add_line('p1-r1-10', (28, 21), (26, 27))
        self.add_bezier('p1-r1-11', (26, 27), ((25.333333333333332, 29), (23.666666666666668, 30), (21, 30)))
        self.add_line('p1-r1-12', (21, 30), (10, 30))
        self.add_bezier('p1-r1-13', (10, 30), ((5.333333333333334, 30), (3, 28.666666666666668), (3, 26)))
        self.add_line('p1-r1-14', (3, 26), (3, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
