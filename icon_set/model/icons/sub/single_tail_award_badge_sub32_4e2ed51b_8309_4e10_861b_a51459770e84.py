"""Independent 32px profile of single-tail-award-badge.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4e2ed51b-8309-4e10-861b-a51459770e84'
SOURCE_PATH = 'pictographic-primitives/rewards/badge_4e2ed51b-8309-4e10-861b-a51459770e84.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e2ed51b-8309-4e10-861b-a51459770e84', 'pictographic-primitives/rewards/badge_4e2ed51b-8309-4e10-861b-a51459770e84.svg'),)
PROFILE_SOURCE_KEYS = ('solo/single-tail-award-badge',)
SOLO_SOURCE_ICON_IDS = ('single-tail-award-badge',)
REFERENCE_EXPORT_SHA256 = 'cfcb94ead085503027d1aa95c3ffb1e312499fc2f5d9f21ef717ca752e5bf81e'

class Drawing(Sub32):
    icon_id = 'single-tail-award-badge-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/award'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 10), (27, 10), radius_x=11, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (27, 10), (24, 16), radius_x=11, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (24, 16), (8, 16), radius_x=11, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (8, 16), (5, 10), radius_x=11, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (8, 16), (8, 30))
        self.add_line('p2-r1-2', (8, 30), (16, 24))
        self.add_line('p2-r1-3', (16, 24), (24, 30))
        self.add_line('p2-r1-4', (24, 30), (24, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-4')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-4')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
