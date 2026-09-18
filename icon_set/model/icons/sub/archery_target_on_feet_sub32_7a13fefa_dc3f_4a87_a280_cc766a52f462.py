"""Independent 32px profile of archery-target-on-feet.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7a13fefa-dc3f-4a87-a280-cc766a52f462'
SOURCE_PATH = 'pictographic-primitives/business/target center_7a13fefa-dc3f-4a87-a280-cc766a52f462.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7a13fefa-dc3f-4a87-a280-cc766a52f462', 'pictographic-primitives/business/target center_7a13fefa-dc3f-4a87-a280-cc766a52f462.svg'), ('95837240-8ef3-49ed-a3f0-513c4f947fe2', 'pictographic-primitives/business/target center_95837240-8ef3-49ed-a3f0-513c4f947fe2.svg'))
PROFILE_SOURCE_KEYS = ('solo/archery-target-on-feet',)
SOLO_SOURCE_ICON_IDS = ('archery-target-on-feet',)
REFERENCE_EXPORT_SHA256 = '57b6699287339605e334d241220f56431b494e3a63bc5a333f4542a1cbbc2c2a'

class Drawing(Sub32):
    icon_id = 'archery-target-on-feet-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (25, 16), (21, 25), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (21, 25), (7, 25), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (7, 25), (2, 16), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (2, 16), (14, 4), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (7, 25), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 25), (25, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (14, 16), (23, 7))
        self.add_line('p4-r1-2', (23, 7), (28, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (23, 2), (23, 7))
        self.add_line('p5-r1-2', (23, 7), (30, 7))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-2')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-2')
