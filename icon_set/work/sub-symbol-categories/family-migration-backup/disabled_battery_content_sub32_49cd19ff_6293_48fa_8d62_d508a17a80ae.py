"""Independent 32px profile of disabled-battery-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '49cd19ff-6293-48fa-8d62-d508a17a80ae'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/49cd19ff-6293-48fa-8d62-d508a17a80ae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('49cd19ff-6293-48fa-8d62-d508a17a80ae', 'icon_set/dist/gallery/combination-originals/49cd19ff-6293-48fa-8d62-d508a17a80ae.svg'),)
PROFILE_SOURCE_KEYS = ('solo/disabled-battery-content', 'solo/disabled-battery-content-v2')
SOLO_SOURCE_ICON_IDS = ('disabled-battery-content', 'disabled-battery-content-v2')
REFERENCE_EXPORT_SHA256 = 'a98a496e1c6721f13ec21b2a77a27cc660b7362d8c92d84883761d5006df722d'

class Drawing(Sub32):
    icon_id = 'disabled-battery-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 18), (2, 8))
        self.add_arc('p1-r1-2', (2, 8), (5, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (5, 5), (22, 5))
        self.add_arc('p1-r1-4', (22, 5), (24, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 8), (24, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (24, 19), (24, 24))
        self.add_arc('p2-r1-2', (24, 24), (22, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (22, 27), (5, 27))
        self.add_arc('p2-r1-4', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (30, 13), (30, 19))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 27), (24, 5))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
