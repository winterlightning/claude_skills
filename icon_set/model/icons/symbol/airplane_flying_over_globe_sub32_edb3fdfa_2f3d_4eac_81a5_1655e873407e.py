"""Independent 32px profile of airplane-flying-over-globe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'edb3fdfa-2f3d-4eac-81a5-1655e873407e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/globe plane_edb3fdfa-2f3d-4eac-81a5-1655e873407e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('edb3fdfa-2f3d-4eac-81a5-1655e873407e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/globe plane_edb3fdfa-2f3d-4eac-81a5-1655e873407e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airplane-flying-over-globe',)
SOLO_SOURCE_ICON_IDS = ('airplane-flying-over-globe',)
REFERENCE_EXPORT_SHA256 = '24d08038d039b09ecb0e3c74809f55f1632ec08ca4fa654051dd9ba6579fd980'

class Drawing(Sub32):
    icon_id = 'airplane-flying-over-globe-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Globe (circle with cross lines) and a small airplane flying past it, 4 units clear.
        self.add_arc('g-1', (2, 10), (10, 2), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('g-2', (10, 2), (18, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('g-3', (18, 10), (10, 18), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('g-4', (10, 18), (2, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('globe', 'g-1', 'g-2', 'g-3', 'g-4', closed=True)
        self.add_line('lat', (2, 10), (18, 10))
        self.add_line('lon', (10, 2), (10, 18))
        self.add_polyline('wings', (20, 30), (25, 25), (30, 20))
        self.add_polyline('body', (22, 22), (25, 25), (29, 30))
        self.add_line('tail', (16, 30), (20, 30))
        for a, b in (('globe', 'lat'), ('globe', 'lon'), ('lat', 'lon'), ('wings', 'body'), ('wings', 'tail')):
            self.relate('connect', a, b)
