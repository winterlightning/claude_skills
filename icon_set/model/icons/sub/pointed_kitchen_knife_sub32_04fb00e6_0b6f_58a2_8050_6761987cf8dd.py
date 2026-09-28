"""Independent 32px profile of pointed-kitchen-knife.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '04fb00e6-0b6f-58a2-8050-6761987cf8dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/knife_04fb00e6-0b6f-58a2-8050-6761987cf8dd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('04fb00e6-0b6f-58a2-8050-6761987cf8dd', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/knife_04fb00e6-0b6f-58a2-8050-6761987cf8dd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pointed-kitchen-knife',)
SOLO_SOURCE_ICON_IDS = ('pointed-kitchen-knife',)
REFERENCE_EXPORT_SHA256 = '78a87f02cc0e4275a41235b8f65850f4768c83744735c081b7261f60e3d49a27'

class Drawing(Sub32):
    icon_id = 'pointed-kitchen-knife-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'food'
    categories = ('food', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 18), (2, 27))
        self.add_bezier('p1-r1-2', (2, 27), ((2, 29), (4, 30), (7, 30)))
        self.add_bezier('p1-r1-3', (7, 30), ((9, 30), (11, 29), (11, 28)))
        self.add_line('p1-r1-4', (11, 28), (18, 24))
        self.add_line('p1-r1-5', (18, 24), (11, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (11, 18), (30, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (30, 2), ((30, 10), (24, 19), (18, 24)))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
