# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '14e0f209-1f73-4be1-9637-df2de37b666b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_14e0f209-1f73-4be1-9637-df2de37b666b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14e0f209-1f73-4be1-9637-df2de37b666b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_14e0f209-1f73-4be1-9637-df2de37b666b.svg'), ('bc1a4fc0-cd35-423d-909c-bad3ddffd5c9', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_bc1a4fc0-cd35-423d-909c-bad3ddffd5c9.svg'))
PROFILE_SOURCE_KEYS = ('solo/open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b', 'solo/open-palm-hand-bc1a4fc0-cd35-423d-909c-bad3ddffd5c9')
SOLO_SOURCE_ICON_IDS = ('open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b', 'open-palm-hand-bc1a4fc0-cd35-423d-909c-bad3ddffd5c9')
REFERENCE_EXPORT_SHA256 = '5d94efe90b12f2752213ae028698de92ef1533350fab01ddd1a3106fde411d38'

class DrawingContainerSymbol(Sub32):
    icon_id = 'open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b-sub32-symbol'
    variant_of = 'open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b-sub32'
    counterpart_icon_id = 'open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'holidays'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 19), (8, 9))
        self.add_arc('p1-r1-2', (8, 9), (13, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (13, 9), (13, 8))
        self.add_arc('p1-r1-4', (13, 8), (19, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (19, 8), (19, 9))
        self.add_arc('p1-r1-6', (19, 9), (24, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (24, 9), (24, 13))
        self.add_arc('p1-r1-8', (24, 13), (30, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (30, 13), (30, 19))
        self.add_arc('p1-r1-10', (30, 19), (22, 27), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (22, 27), (16, 27))
        self.add_bezier('p1-r1-12', (16, 27), ((10, 27), (6, 23), (2, 19)))
        self.add_bezier('p1-r1-13', (2, 19), ((2, 17), (3, 16), (4, 16)))
        self.add_bezier('p1-r1-14', (4, 16), ((5, 16), (6, 17), (8, 19)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
        self.add_line('p2-r1-1', (13, 9), (13, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (19, 9), (19, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 13), (24, 17))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p4-r1-1')
        self.relate('connect', 'p1-r1-8', 'p4-r1-1')
