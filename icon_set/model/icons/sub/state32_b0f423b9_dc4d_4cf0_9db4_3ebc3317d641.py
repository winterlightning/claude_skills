"""Independent 32px profile of state32-b0f423b9-dc4d-4cf0-9db4-3ebc3317d641.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b0f423b9-dc4d-4cf0-9db4-3ebc3317d641'
SOURCE_PATH = 'icon_set/assets/combination-state32/b0f423b9-dc4d-4cf0-9db4-3ebc3317d641.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b0f423b9-dc4d-4cf0-9db4-3ebc3317d641', 'icon_set/assets/combination-state32/b0f423b9-dc4d-4cf0-9db4-3ebc3317d641.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '233fe8ba5be58854a010a405ba9fab371b34e2a1c4c6675334c0148ed4e9065e'

class Drawing(Sub32):
    icon_id = 'state32-b0f423b9-dc4d-4cf0-9db4-3ebc3317d641'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((13, 6), (12, 9), (12, 11)))
        self.add_bezier('p1-r1-2', (12, 11), ((12, 14), (14, 16), (16, 16)))
        self.add_bezier('p1-r1-3', (16, 16), ((18, 16), (20, 14), (20, 11)))
        self.add_bezier('p1-r1-4', (20, 11), ((20, 9), (19, 6), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (8, 16), ((5, 21), (3, 24), (3, 25)))
        self.add_bezier('p2-r1-2', (3, 25), ((3, 28), (6, 30), (8, 30)))
        self.add_bezier('p2-r1-3', (8, 30), ((10, 30), (12, 28), (12, 25)))
        self.add_bezier('p2-r1-4', (12, 25), ((12, 24), (11, 21), (8, 16)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (24, 16), ((21, 21), (20, 24), (20, 25)))
        self.add_bezier('p3-r1-2', (20, 25), ((20, 28), (22, 30), (24, 30)))
        self.add_bezier('p3-r1-3', (24, 30), ((26, 30), (29, 28), (29, 25)))
        self.add_bezier('p3-r1-4', (29, 25), ((29, 24), (27, 21), (24, 16)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
