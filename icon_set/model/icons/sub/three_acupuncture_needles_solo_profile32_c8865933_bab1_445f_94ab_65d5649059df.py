"""Independent 32px profile of three-acupuncture-needles-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c8865933-bab1-445f-94ab-65d5649059df'
SOURCE_PATH = 'pictographic-primitives/other/needles three_c8865933-bab1-445f-94ab-65d5649059df.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8865933-bab1-445f-94ab-65d5649059df', 'pictographic-primitives/other/needles three_c8865933-bab1-445f-94ab-65d5649059df.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-acupuncture-needles-solo',)
SOLO_SOURCE_ICON_IDS = ('three-acupuncture-needles-solo',)
REFERENCE_EXPORT_SHA256 = '2d386e10d9b13b264798a4d70b7aec73fc7e9d497f0edc7260a52ce404fef020'

class Drawing(Sub32):
    icon_id = 'three-acupuncture-needles-solo-profile32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 8), (24, 8))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (24, 8), (30, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 8), (24, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 16), (12, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (12, 16), (17, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (17, 16), (12, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 24), (24, 24))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (24, 24), (30, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p6-r1-2', (30, 24), (24, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-2')
        self.relate("connect", 'p5-r1-1', 'p6-r1-1')
        self.relate("connect", 'p5-r1-1', 'p6-r1-2')
