"""Independent 32px profile of state32-345d1bc8-d8f0-4c03-9e3d-6cd720f0912d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '345d1bc8-d8f0-4c03-9e3d-6cd720f0912d'
SOURCE_PATH = 'icon_set/assets/combination-state32/345d1bc8-d8f0-4c03-9e3d-6cd720f0912d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('345d1bc8-d8f0-4c03-9e3d-6cd720f0912d', 'icon_set/assets/combination-state32/345d1bc8-d8f0-4c03-9e3d-6cd720f0912d.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '7fac56f8a051a879e3fb80b8b9d80e9e18b704bc5c2136af37cb5c6b4dcaba8e'

class Drawing(Sub32):
    icon_id = 'state32-345d1bc8-d8f0-4c03-9e3d-6cd720f0912d'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (4, 25), ((6.666666666666666, 21), (8, 16), (8, 10)))
        self.add_bezier('p1-r1-2', (8, 10), ((8, 5), (12, 2), (16, 2)))
        self.add_bezier('p1-r1-3', (16, 2), ((20, 2), (24, 5), (24, 10)))
        self.add_bezier('p1-r1-4', (24, 10), ((24, 16), (25.333333333333332, 21), (28, 25)))
        self.add_line('p1-r1-5', (28, 25), (4, 25))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p1-r2-1', (13, 30), (19, 30))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
