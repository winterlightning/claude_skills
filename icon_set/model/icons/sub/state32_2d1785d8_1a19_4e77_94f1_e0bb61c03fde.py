"""Independent 32px profile of state32-2d1785d8-1a19-4e77-94f1-e0bb61c03fde.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2d1785d8-1a19-4e77-94f1-e0bb61c03fde'
SOURCE_PATH = 'icon_set/assets/combination-state32/2d1785d8-1a19-4e77-94f1-e0bb61c03fde.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2d1785d8-1a19-4e77-94f1-e0bb61c03fde', 'icon_set/assets/combination-state32/2d1785d8-1a19-4e77-94f1-e0bb61c03fde.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'ea7e14b0cb9dfca6175cf17e4620edb7c3e2543c4c94e3cf06f02cbff1ea2fce'

class Drawing(Sub32):
    icon_id = 'state32-2d1785d8-1a19-4e77-94f1-e0bb61c03fde'
    keyshape = Keyshape.HRECT_S
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (17, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p1-r2-1', (11, 11), (17, 16))
        self.add_line('p1-r2-2', (17, 16), (11, 21))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_arc('p2-r1-1', (21, 16), (30, 16), radius_x=4.5, radius_y=4.5, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (21, 16), radius_x=4.5, radius_y=4.5, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p1-r2-1')
        self.relate("connect", 'p1-r1-1', 'p1-r2-2')
