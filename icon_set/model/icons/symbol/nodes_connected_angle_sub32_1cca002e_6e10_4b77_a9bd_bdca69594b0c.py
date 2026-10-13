"""Independent 32px profile of nodes-connected-angle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1cca002e-6e10-4b77-a9bd-bdca69594b0c'
SOURCE_PATH = 'pictographic-primitives/symbol/design vector_1cca002e-6e10-4b77-a9bd-bdca69594b0c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1cca002e-6e10-4b77-a9bd-bdca69594b0c', 'pictographic-primitives/symbol/design vector_1cca002e-6e10-4b77-a9bd-bdca69594b0c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/nodes-connected-angle',)
SOLO_SOURCE_ICON_IDS = ('nodes-connected-angle',)
REFERENCE_EXPORT_SHA256 = 'bba367cd84ecddddc29bf8b1e1a37018d15ae135e7392c94f9ac13a899122211'

class Drawing(Sub32):
    icon_id = 'nodes-connected-angle-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Connected nodes: a large node linked to two small ones, links ending exactly on the rings.
        self.add_arc('n0-1', (4, 16), (14, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('n0-2', (14, 16), (4, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('hub', 'n0-1', 'n0-2', closed=True)
        for k, y in enumerate((6, 26)):
            self.add_arc(f'n{k + 1}-1', (20, y), (28, y), radius_x=4, radius_y=4, large_arc=False, sweep=True)
            self.add_arc(f'n{k + 1}-2', (28, y), (20, y), radius_x=4, radius_y=4, large_arc=False, sweep=True)
            self.add_contour(f'node-{k}', f'n{k + 1}-1', f'n{k + 1}-2', closed=True)
        self.add_line('link-0', (12, 12), (20, 6))
        self.add_line('link-1', (12, 20), (20, 26))
        for a, b in (('hub', 'link-0'), ('node-0', 'link-0'), ('hub', 'link-1'), ('node-1', 'link-1')):
            self.relate('connect', a, b)
