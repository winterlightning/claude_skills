"""Independent 32px profile of heart-pulse.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3ec61357-503d-46af-90a8-2fa210293e19'
SOURCE_PATH = 'pictographic-primitives/symbol/heart throb_3ec61357-503d-46af-90a8-2fa210293e19.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ec61357-503d-46af-90a8-2fa210293e19', 'pictographic-primitives/symbol/heart throb_3ec61357-503d-46af-90a8-2fa210293e19.svg'), ('a9dc34df-bbc3-4ab4-a859-ebdb7d92a804', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/sports/heart rate_a9dc34df-bbc3-4ab4-a859-ebdb7d92a804.svg'), ('468beab8-6edf-4e7f-9ee2-0f23f5c3b360', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/sports/heart rate_468beab8-6edf-4e7f-9ee2-0f23f5c3b360.svg'), ('a954f676-1cce-4e19-81eb-ec067ec52edc', 'icon_set/dist/gallery/combination-originals/a954f676-1cce-4e19-81eb-ec067ec52edc.svg'))
PROFILE_SOURCE_KEYS = ('solo/heart-pulse',)
SOLO_SOURCE_ICON_IDS = ('heart-pulse',)
REFERENCE_EXPORT_SHA256 = 'a0e0a468015204b48ebba4e5778af58a1ff414247475f0f869116cff52877287'

class DrawingContainerSymbol(Sub32):
    icon_id = 'heart-pulse-sub32-symbol'
    related_origin_icon_id = 'heart-pulse-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/heart-pulse-sub32'
    counterpart_icon_id = 'heart-pulse-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Heart with a pulse line across its widest point and one spike, 4 units clear of the outline.
        self.add_arc('p1-r1-1', (2, 8), (16, 8), radius_x=7, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 8), (30, 8), radius_x=7, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-3', (30, 8), ((30, 11), (30, 14), (29, 16)))
        self.add_line('p1-r1-4', (29, 16), (16, 28))
        self.add_line('p1-r1-5', (16, 28), (3, 16))
        self.add_bezier('p1-r1-6', (3, 16), ((2, 14), (2, 11), (2, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=True)
        self.add_line('p2-r1-1', (3, 16), (9, 16))
        self.add_line('p2-r1-2', (9, 16), (12, 12))
        self.add_line('p2-r1-3', (12, 12), (15, 16))
        self.add_line('p2-r1-4', (15, 16), (29, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-4')
        self.relate('connect', 'p1-r1-4', 'p2-r1-4')
