"""Independent 32px profile of rainbow-arcs.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ffe2ea11-dc9b-4412-89d9-6f62d969d59c'
SOURCE_PATH = 'pictographic-primitives/symbol/rainbow_ffe2ea11-dc9b-4412-89d9-6f62d969d59c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ffe2ea11-dc9b-4412-89d9-6f62d969d59c', 'pictographic-primitives/symbol/rainbow_ffe2ea11-dc9b-4412-89d9-6f62d969d59c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rainbow-arcs',)
SOLO_SOURCE_ICON_IDS = ('rainbow-arcs',)
REFERENCE_EXPORT_SHA256 = 'dcdb5a295e2a9ffe1d326ffeb613ed7bba7e24a93b9b05789dcfeed462075113'

class Drawing(Sub32):
    icon_id = 'rainbow-arcs-sub32'
    keyshape = Keyshape.HRECT_M
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 23), (30, 23), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (8, 23), (24, 23), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (15, 23), (17, 23), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
