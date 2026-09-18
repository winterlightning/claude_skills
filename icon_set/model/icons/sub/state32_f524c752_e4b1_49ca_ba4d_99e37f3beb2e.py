"""Independent 32px profile of state32-f524c752-e4b1-49ca-ba4d-99e37f3beb2e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f524c752-e4b1-49ca-ba4d-99e37f3beb2e'
SOURCE_PATH = 'icon_set/assets/combination-state32/f524c752-e4b1-49ca-ba4d-99e37f3beb2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f524c752-e4b1-49ca-ba4d-99e37f3beb2e', 'icon_set/assets/combination-state32/f524c752-e4b1-49ca-ba4d-99e37f3beb2e.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'adf757ddd981766a8abbb6455a259d36c736b6bda66bcf46d88547befc931dd7'

class Drawing(Sub32):
    icon_id = 'state32-f524c752-e4b1-49ca-ba4d-99e37f3beb2e'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (15, 2))
        self.add_bezier('p1-r1-2', (15, 2), ((16.333333333333332, 2), (17.333333333333332, 2.3333333333333335), (18, 3)))
        self.add_line('p1-r1-3', (18, 3), (29, 14))
        self.add_bezier('p1-r1-4', (29, 14), ((29.666666666666668, 14.666666666666666), (30, 15.333333333333334), (30, 16)))
        self.add_bezier('p1-r1-5', (30, 16), ((30, 16.666666666666668), (29.666666666666668, 17.333333333333332), (29, 18)))
        self.add_line('p1-r1-6', (29, 18), (18, 29))
        self.add_bezier('p1-r1-7', (18, 29), ((17.333333333333332, 29.666666666666668), (16.666666666666668, 30), (16, 30)))
        self.add_bezier('p1-r1-8', (16, 30), ((15.333333333333334, 30), (14.666666666666666, 29.666666666666668), (14, 29)))
        self.add_line('p1-r1-9', (14, 29), (3, 18))
        self.add_bezier('p1-r1-10', (3, 18), ((2.3333333333333335, 17.333333333333332), (2, 16.333333333333332), (2, 15)))
        self.add_line('p1-r1-11', (2, 15), (2, 5))
        self.add_bezier('p1-r1-12', (2, 5), ((2, 3), (3, 2), (5, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (8, 8), (8, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
