"""Independent 32px profile of flame-with-inner-drop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd11d120b-44dc-4986-8c2a-a773c8830e0c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/flame_d11d120b-44dc-4986-8c2a-a773c8830e0c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d11d120b-44dc-4986-8c2a-a773c8830e0c', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/flame_d11d120b-44dc-4986-8c2a-a773c8830e0c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flame-with-inner-drop',)
SOLO_SOURCE_ICON_IDS = ('flame-with-inner-drop',)
REFERENCE_EXPORT_SHA256 = '6480a8274acccf6a7f1325e9837658e0827c5d5b5d6b54a54acbb3a1bddf168a'

class Drawing(Sub32):
    icon_id = 'flame-with-inner-drop-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/fire'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (12, 30), ((7, 27), (5, 24), (5, 20)))
        self.add_bezier('p1-r1-2', (5, 20), ((5, 13), (15, 11), (15, 5)))
        self.add_bezier('p1-r1-3', (15, 5), ((15, 4), (14, 3), (14, 2)))
        self.add_bezier('p1-r1-4', (14, 2), ((19, 5), (21, 8), (21, 12)))
        self.add_bezier('p1-r1-5', (21, 12), ((21, 13), (21, 14), (20, 15)))
        self.add_bezier('p1-r1-6', (20, 15), ((24, 15), (27, 13), (27, 10)))
        self.add_bezier('p1-r1-7', (27, 10), ((27, 14), (27, 17), (27, 20)))
        self.add_bezier('p1-r1-8', (27, 20), ((27, 24), (24, 28), (20, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_bezier('p2-r1-1', (12, 30), ((11, 28), (10, 27), (10, 25)))
        self.add_bezier('p2-r1-2', (10, 25), ((10, 21), (13, 19), (16, 17)))
        self.add_bezier('p2-r1-3', (16, 17), ((16, 21), (21, 22), (21, 26)))
        self.add_bezier('p2-r1-4', (21, 26), ((21, 27), (21, 29), (20, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-4')
