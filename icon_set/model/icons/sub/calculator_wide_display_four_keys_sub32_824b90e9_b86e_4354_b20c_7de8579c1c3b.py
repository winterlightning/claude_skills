"""Independent 32px profile of calculator-wide-display-four-keys.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '824b90e9-b86e-4354-b20c-7de8579c1c3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/calculator_824b90e9-b86e-4354-b20c-7de8579c1c3b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('824b90e9-b86e-4354-b20c-7de8579c1c3b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/calculator_824b90e9-b86e-4354-b20c-7de8579c1c3b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/calculator-wide-display-four-keys',)
SOLO_SOURCE_ICON_IDS = ('calculator-wide-display-four-keys',)
REFERENCE_EXPORT_SHA256 = '96f55966fc1f89e2376e26daac3d1b363c26e15194c11492a1c9af2a43adedc5'

class Drawing(Sub32):
    icon_id = 'calculator-wide-display-four-keys-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (27, 5), (27, 11))
        self.add_line('p1-r1-4', (27, 11), (27, 27))
        self.add_arc('p1-r1-5', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (24, 30), (8, 30))
        self.add_arc('p1-r1-7', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (5, 27), (5, 11))
        self.add_line('p1-r1-9', (5, 11), (5, 5))
        self.add_arc('p1-r1-10', (5, 5), (8, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (5, 11), (27, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (11, 17), (13, 17))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (19, 17), (21, 17))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (11, 24), (13, 24))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (19, 24), (21, 24))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
