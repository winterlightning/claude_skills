"""Independent 32px profile of front-view-bathroom-toilet.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4b4b156b-56c7-45c1-80c4-fb442761ed90'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/toilet_4b4b156b-56c7-45c1-80c4-fb442761ed90.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4b4b156b-56c7-45c1-80c4-fb442761ed90', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/toilet_4b4b156b-56c7-45c1-80c4-fb442761ed90.svg'),)
PROFILE_SOURCE_KEYS = ('solo/front-view-bathroom-toilet',)
SOLO_SOURCE_ICON_IDS = ('front-view-bathroom-toilet',)
REFERENCE_EXPORT_SHA256 = 'c5cf4949bfa9d694b3a9b7307b2b0d8695639c869df55d23acb4eeb4c92ee2d0'

class DrawingVariant3(Sub32):
    icon_id = 'front-view-bathroom-toilet-sub32-v3'
    related_origin_icon_id = 'front-view-bathroom-toilet-sub32-v2'
    variant_label = 'Redraw shape and structural proportions'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('tank-left', (8, 14), (8, 4))
        self.add_bezier('tank-tl', (8, 4), ((8, 2), (10, 2), (12, 2)))
        self.add_line('tank-top', (12, 2), (20, 2))
        self.add_bezier('tank-tr', (20, 2), ((22, 2), (24, 2), (24, 4)))
        self.add_line('tank-right', (24, 4), (24, 14))
        self.add_contour('tank', 'tank-left', 'tank-tl', 'tank-top', 'tank-tr', 'tank-right')
        self.add_line('seat', (4, 14), (28, 14))
        self.add_bezier('bowl-right', (28, 14), ((28, 20), (24, 22), (20, 24)))
        self.add_line('foot-right', (20, 24), (22, 30))
        self.add_line('base', (22, 30), (10, 30))
        self.add_line('foot-left', (10, 30), (12, 24))
        self.add_bezier('bowl-left', (12, 24), ((8, 22), (4, 20), (4, 14)))
        self.add_contour('bowl', 'seat', 'bowl-right', 'foot-right', 'base', 'foot-left', 'bowl-left', closed=True)
        self.relate('connect', 'tank', 'bowl')
