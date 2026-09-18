"""Independent 32px profile of snail-shell-spiral.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ac736fb4-930d-5099-ae75-efdc2b2a7f88'
SOURCE_PATH = 'pictographic-primitives/animals/snail shell_ac736fb4-930d-5099-ae75-efdc2b2a7f88.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ac736fb4-930d-5099-ae75-efdc2b2a7f88', 'pictographic-primitives/animals/snail shell_ac736fb4-930d-5099-ae75-efdc2b2a7f88.svg'), ('7795da4a-94f4-4d32-9e97-2b2255bfc247', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hotels/food_7795da4a-94f4-4d32-9e97-2b2255bfc247.svg'))
PROFILE_SOURCE_KEYS = ('solo/snail-shell-spiral',)
SOLO_SOURCE_ICON_IDS = ('snail-shell-spiral',)
REFERENCE_EXPORT_SHA256 = '1444cd7a823cb50fe31978627f1c05970268303a149f3844fef758cbd1fc32ff'

class Drawing(Sub32):
    icon_id = 'snail-shell-spiral-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature/animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (10, 16), radius_x=10, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (10, 16), (22, 16), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (22, 16), (18, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
