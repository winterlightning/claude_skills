# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of front-view-bathroom-toilet.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4b4b156b-56c7-45c1-80c4-fb442761ed90'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/toilet_4b4b156b-56c7-45c1-80c4-fb442761ed90.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4b4b156b-56c7-45c1-80c4-fb442761ed90', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/toilet_4b4b156b-56c7-45c1-80c4-fb442761ed90.svg'),)
PROFILE_SOURCE_KEYS = ('solo/front-view-bathroom-toilet',)
SOLO_SOURCE_ICON_IDS = ('front-view-bathroom-toilet',)
REFERENCE_EXPORT_SHA256 = 'c5cf4949bfa9d694b3a9b7307b2b0d8695639c869df55d23acb4eeb4c92ee2d0'

class DrawingVariant2(Sub32):
    icon_id = 'front-view-bathroom-toilet-sub32-v2'
    variant_of = 'front-view-bathroom-toilet-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (9, 16), (8, 2))
        self.add_line('p1-r1-2', (8, 2), (24, 2))
        self.add_line('p1-r1-3', (24, 2), (23, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (short_low, 16), (9, 16))
        self.add_line('p2-r1-2', (9, 16), (23, 16))
        self.add_line('p2-r1-3', (23, 16), (short_high, 16))
        self.add_bezier('p2-r1-4', (short_high, 16), ((short_high, 22), (23, 23), (22, 24)))
        self.add_line('p2-r1-5', (22, 24), (24, 30))
        self.add_line('p2-r1-6', (24, 30), (8, 30))
        self.add_line('p2-r1-7', (8, 30), (10, 24))
        self.add_bezier('p2-r1-8', (10, 24), ((9, 23), (short_low, 22), (short_low, 16)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-3')
