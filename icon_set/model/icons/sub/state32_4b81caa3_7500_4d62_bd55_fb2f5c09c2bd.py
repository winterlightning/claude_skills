"""Independent 32px profile of state32-4b81caa3-7500-4d62-bd55-fb2f5c09c2bd.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4b81caa3-7500-4d62-bd55-fb2f5c09c2bd'
SOURCE_PATH = 'icon_set/assets/combination-state32/4b81caa3-7500-4d62-bd55-fb2f5c09c2bd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4b81caa3-7500-4d62-bd55-fb2f5c09c2bd', 'icon_set/assets/combination-state32/4b81caa3-7500-4d62-bd55-fb2f5c09c2bd.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'c19ac330fc0c845df48032ec296f83ae7835e8c6db43aa03d899b8dde22f8847'

class Drawing(Sub32):
    icon_id = 'state32-4b81caa3-7500-4d62-bd55-fb2f5c09c2bd'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (3, 8), ((7.666666666666666, 4.666666666666667), (12, 3), (16, 3)))
        self.add_bezier('p1-r1-2', (16, 3), ((20, 3), (24.333333333333336, 4.666666666666667), (29, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p1-r2-1', (9, 13), ((11, 11), (13.333333333333334, 10), (16, 10)))
        self.add_bezier('p1-r2-2', (16, 10), ((18.666666666666668, 10), (21, 11), (23, 13)))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_bezier('p1-r3-1', (7, 19), ((4, 19), (2, 22), (2, 25)))
        self.add_bezier('p1-r3-2', (2, 25), ((2, 27), (3, 29), (5, 29)))
        self.add_bezier('p1-r3-3', (5, 29), ((5, 29), (6, 29), (6, 29)))
        self.add_line('p1-r3-4', (6, 29), (12, 26))
        self.add_bezier('p1-r3-5', (12, 26), ((13.333333333333334, 25.333333333333332), (14.666666666666666, 25), (16, 25)))
        self.add_bezier('p1-r3-6', (16, 25), ((17.333333333333332, 25), (18.666666666666668, 25.333333333333332), (20, 26)))
        self.add_line('p1-r3-7', (20, 26), (26, 29))
        self.add_bezier('p1-r3-8', (26, 29), ((26, 29), (27, 29), (27, 29)))
        self.add_bezier('p1-r3-9', (27, 29), ((29, 29), (30, 27), (30, 25)))
        self.add_bezier('p1-r3-10', (30, 25), ((30, 22), (28, 19), (25, 19)))
        self.add_line('p1-r3-11', (25, 19), (7, 19))
        self.add_contour('path-1-3', 'p1-r3-1', 'p1-r3-2', 'p1-r3-3', 'p1-r3-4', 'p1-r3-5', 'p1-r3-6', 'p1-r3-7', 'p1-r3-8', 'p1-r3-9', 'p1-r3-10', 'p1-r3-11', closed=False)
