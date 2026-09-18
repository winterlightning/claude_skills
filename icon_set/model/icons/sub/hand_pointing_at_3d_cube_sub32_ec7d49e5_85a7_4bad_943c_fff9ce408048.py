"""Independent 32px profile of hand-pointing-at-3d-cube-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ec7d49e5-85a7-4bad-943c-fff9ce408048'
SOURCE_PATH = 'pictographic-primitives/state/hand point cube_ec7d49e5-85a7-4bad-943c-fff9ce408048.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ec7d49e5-85a7-4bad-943c-fff9ce408048', 'pictographic-primitives/state/hand point cube_ec7d49e5-85a7-4bad-943c-fff9ce408048.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-pointing-at-3d-cube-solo',)
SOLO_SOURCE_ICON_IDS = ('hand-pointing-at-3d-cube-solo',)
REFERENCE_EXPORT_SHA256 = '0e04905611e451ab5d0a6d6e41b7eb57acab6019ea75f93e8c669e6cca7cf905'

class Drawing(Sub32):
    icon_id = 'hand-pointing-at-3d-cube-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 6), (23, 2))
        self.add_line('p1-r1-2', (23, 2), (30, 6))
        self.add_line('p1-r1-3', (30, 6), (30, 14))
        self.add_line('p1-r1-4', (30, 14), (23, 18))
        self.add_line('p1-r1-5', (23, 18), (16, 14))
        self.add_line('p1-r1-6', (16, 14), (16, 6))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 6), (23, 10))
        self.add_line('p2-r1-2', (23, 10), (30, 6))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (23, 10), (23, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (2, 25), ((2, 24), (3, 23), (4, 23)))
        self.add_bezier('p4-r1-2', (4, 23), ((4, 23), (5, 24), (5, 25)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (5, 25), (5, 20))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (5, 20), (11, 20), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (11, 20), (11, 27))
        self.add_line('p7-r1-2', (11, 27), (16, 28))
        self.add_line('p7-r1-3', (16, 28), (16, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
        self.relate("connect", 'p5-r1-1', 'p6-r1-1')
        self.relate("connect", 'p6-r1-1', 'p7-r1-1')
