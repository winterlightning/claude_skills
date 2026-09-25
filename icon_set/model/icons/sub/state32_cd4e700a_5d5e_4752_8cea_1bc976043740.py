"""Independent 32px profile of state32-cd4e700a-5d5e-4752-8cea-1bc976043740.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'cd4e700a-5d5e-4752-8cea-1bc976043740'
SOURCE_PATH = 'icon_set/assets/combination-state32/cd4e700a-5d5e-4752-8cea-1bc976043740.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cd4e700a-5d5e-4752-8cea-1bc976043740', 'icon_set/assets/combination-state32/cd4e700a-5d5e-4752-8cea-1bc976043740.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '62440f4998b3f9061dbd68a235aa83497ba7425283cecc521ac4dfaff798332d'

class Drawing(Sub32):
    icon_id = 'state32-cd4e700a-5d5e-4752-8cea-1bc976043740'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (2, 9))
        self.add_bezier('p1-r1-2', (2, 9), ((2, 4), (6, 2), (9, 2)))
        self.add_bezier('p1-r1-3', (9, 2), ((12, 2), (15, 4), (15, 8)))
        self.add_line('p1-r1-4', (15, 8), (15, 17))
        self.add_bezier('p1-r1-5', (15, 17), ((15, 18.333333333333332), (14.333333333333334, 19), (13, 19)))
        self.add_bezier('p1-r1-6', (13, 19), ((12.333333333333334, 19), (11, 18.666666666666668), (9, 18)))
        self.add_line('p1-r1-7', (9, 18), (9, 30))
        self.add_line('p1-r1-8', (9, 30), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_bezier('p2-r1-1', (21, 9), ((22.333333333333332, 11), (23, 13), (23, 15)))
        self.add_bezier('p2-r1-2', (23, 15), ((23, 17), (22.333333333333332, 19), (21, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p2-r2-1', (26, 4), ((28.666666666666668, 7.333333333333333), (30, 11), (30, 15)))
        self.add_bezier('p2-r2-2', (30, 15), ((30, 18.333333333333332), (28.666666666666668, 22), (26, 26)))
        self.add_contour('path-2-2', 'p2-r2-1', 'p2-r2-2', closed=False)
