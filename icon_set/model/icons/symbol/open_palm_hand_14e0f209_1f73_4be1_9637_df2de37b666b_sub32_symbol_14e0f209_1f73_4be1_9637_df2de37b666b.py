"""Independent 32px profile of open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '14e0f209-1f73-4be1-9637-df2de37b666b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_14e0f209-1f73-4be1-9637-df2de37b666b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14e0f209-1f73-4be1-9637-df2de37b666b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_14e0f209-1f73-4be1-9637-df2de37b666b.svg'), ('bc1a4fc0-cd35-423d-909c-bad3ddffd5c9', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_bc1a4fc0-cd35-423d-909c-bad3ddffd5c9.svg'))
PROFILE_SOURCE_KEYS = ('solo/open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b', 'solo/open-palm-hand-bc1a4fc0-cd35-423d-909c-bad3ddffd5c9')
SOLO_SOURCE_ICON_IDS = ('open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b', 'open-palm-hand-bc1a4fc0-cd35-423d-909c-bad3ddffd5c9')
REFERENCE_EXPORT_SHA256 = '5d94efe90b12f2752213ae028698de92ef1533350fab01ddd1a3106fde411d38'

class DrawingContainerSymbol(Sub32):
    icon_id = 'open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b-sub32-symbol'
    related_origin_icon_id = 'open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b-sub32'
    counterpart_icon_id = 'open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Open palm: three 8-unit fingers (middle one tallest) over a rounded palm, finger dividers.
        self.add_line('h-1', (4, 22), (4, 10))
        self.add_arc('h-2', (4, 10), (12, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('h-3', (12, 10), (12, 6))
        self.add_arc('h-4', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('h-5', (20, 6), (20, 10))
        self.add_arc('h-6', (20, 10), (28, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('h-7', (28, 10), (28, 22))
        self.add_arc('h-8', (28, 22), (20, 30), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('h-9', (20, 30), (12, 30))
        self.add_arc('h-10', (12, 30), (4, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('hand', 'h-1', 'h-2', 'h-3', 'h-4', 'h-5', 'h-6', 'h-7', 'h-8', 'h-9', 'h-10', closed=True)
        self.add_line('gap-1', (12, 10), (12, 18))
        self.add_line('gap-2', (20, 10), (20, 18))
        self.relate('connect', 'hand', 'gap-1')
        self.relate('connect', 'hand', 'gap-2')
