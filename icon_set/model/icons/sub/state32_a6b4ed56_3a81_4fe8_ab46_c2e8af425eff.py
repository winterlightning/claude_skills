"""Independent 32px profile of state32-a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a6b4ed56-3a81-4fe8-ab46-c2e8af425eff'
SOURCE_PATH = 'icon_set/assets/combination-state32/a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a6b4ed56-3a81-4fe8-ab46-c2e8af425eff', 'icon_set/assets/combination-state32/a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '4a838ec94d35a4f0a20167cb8ecc071f73ce0bfd66c14bb01e820ff761d83893'

class Drawing(Sub32):
    icon_id = 'state32-a6b4ed56-3a81-4fe8-ab46-c2e8af425eff'
    keyshape = Keyshape.HRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 12), (28, 12))
        self.add_bezier('p1-r1-2', (28, 12), ((29.333333333333332, 12), (30, 12.666666666666666), (30, 14)))
        self.add_line('p1-r1-3', (30, 14), (30, 18))
        self.add_bezier('p1-r1-4', (30, 18), ((30, 19.333333333333332), (29.333333333333332, 20), (28, 20)))
        self.add_line('p1-r1-5', (28, 20), (4, 20))
        self.add_bezier('p1-r1-6', (4, 20), ((2.666666666666667, 20), (2, 19.333333333333332), (2, 18)))
        self.add_line('p1-r1-7', (2, 18), (2, 14))
        self.add_bezier('p1-r1-8', (2, 14), ((2, 12.666666666666666), (2.666666666666667, 12), (4, 12)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
