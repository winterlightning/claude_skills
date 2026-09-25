"""Independent 32px profile of angled-dental-explorer-curved-tip.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '34b397e2-5944-4499-8303-bd0af66a4a03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/tooth_34b397e2-5944-4499-8303-bd0af66a4a03.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('34b397e2-5944-4499-8303-bd0af66a4a03', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/tooth_34b397e2-5944-4499-8303-bd0af66a4a03.svg'),)
PROFILE_SOURCE_KEYS = ('solo/angled-dental-explorer-curved-tip',)
SOLO_SOURCE_ICON_IDS = ('angled-dental-explorer-curved-tip',)
REFERENCE_EXPORT_SHA256 = '0226169cf0b9cc66b5dfacdbeaa1f12017437828cfc23dc524326c9eadbbec91'

class Drawing(Sub32):
    icon_id = 'angled-dental-explorer-curved-tip-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (16, 16))
        self.add_line('p1-r1-2', (16, 16), (21, 11))
        self.add_line('p1-r1-3', (21, 11), (21, 7))
        self.add_arc('p1-r1-4', (21, 7), (25, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (25, 2), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (30, 7), (30, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 16), (22, 22))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
