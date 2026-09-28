"""Independent 32px profile of three-node-share-network.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ecd8b795-2136-4812-b9c9-6bdce0f5da6a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/share_ecd8b795-2136-4812-b9c9-6bdce0f5da6a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ecd8b795-2136-4812-b9c9-6bdce0f5da6a', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/share_ecd8b795-2136-4812-b9c9-6bdce0f5da6a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-node-share-network',)
SOLO_SOURCE_ICON_IDS = ('three-node-share-network',)
REFERENCE_EXPORT_SHA256 = '9a581f3329daa0c6b715d0de3d41be2f102f1d180e155c7adf0c0140711856a8'

class Drawing(Sub32):
    icon_id = 'three-node-share-network-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (6, 12), (9, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (9, 14), (10, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (10, 16), (9, 18), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (9, 18), (6, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (6, 20), (2, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (2, 16), (6, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_arc('p2-r1-1', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (30, 6), (26, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (26, 10), (23, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (23, 8), (22, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-5', (22, 6), (26, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_arc('p3-r1-1', (23, 24), (26, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (26, 22), (30, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (26, 30), (22, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-5', (22, 26), (23, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (9, 14), (23, 8))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (9, 18), (23, 24))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p1-r1-3', 'p5-r1-1')
        self.relate("connect", 'p1-r1-4', 'p5-r1-1')
        self.relate("connect", 'p2-r1-3', 'p4-r1-1')
        self.relate("connect", 'p2-r1-4', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-5', 'p5-r1-1')
