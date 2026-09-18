"""Independent 32px profile of vertical-temperature-measurement-thermometer-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9c8949d3-833c-43ae-a29e-7b03ccb3f36b'
SOURCE_PATH = 'pictographic-primitives/other/thermometer_9c8949d3-833c-43ae-a29e-7b03ccb3f36b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c8949d3-833c-43ae-a29e-7b03ccb3f36b', 'pictographic-primitives/other/thermometer_9c8949d3-833c-43ae-a29e-7b03ccb3f36b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vertical-temperature-measurement-thermometer-solo',)
SOLO_SOURCE_ICON_IDS = ('vertical-temperature-measurement-thermometer-solo',)
REFERENCE_EXPORT_SHA256 = '29553c9bd62a6bc2d6b5970ba59b83429952e35800bbea38de40229fab789c2f'

class Drawing(Sub32):
    icon_id = 'vertical-temperature-measurement-thermometer-solo-profile32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 18), (6, 8))
        self.add_bezier('p1-r1-2', (6, 8), ((6, 5), (9, 2), (12, 2)))
        self.add_bezier('p1-r1-3', (12, 2), ((16, 2), (19, 5), (19, 8)))
        self.add_line('p1-r1-4', (19, 8), (19, 18))
        self.add_bezier('p1-r1-5', (19, 18), ((21, 20), (22, 22), (22, 24)))
        self.add_bezier('p1-r1-6', (22, 24), ((22, 27), (19, 30), (13, 30)))
        self.add_bezier('p1-r1-7', (13, 30), ((5, 30), (5, 27), (5, 24)))
        self.add_bezier('p1-r1-8', (5, 24), ((5, 22), (6, 20), (6, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (13, 16), (13, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (26, 11), (27, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
