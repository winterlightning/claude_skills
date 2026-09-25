"""Independent 32px profile of house-with-upright-chimney-stroke.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd0a49d2c-ca23-4f73-a310-7bd929b19be2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_d0a49d2c-ca23-4f73-a310-7bd929b19be2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d0a49d2c-ca23-4f73-a310-7bd929b19be2', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_d0a49d2c-ca23-4f73-a310-7bd929b19be2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/house-with-upright-chimney-stroke',)
SOLO_SOURCE_ICON_IDS = ('house-with-upright-chimney-stroke',)
REFERENCE_EXPORT_SHA256 = '947867565fa0937b35ee537791d5ad9b0afd462b79100c213fc773d305bcf6e4'

class Drawing(Sub32):
    icon_id = 'house-with-upright-chimney-stroke-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (5, 13))
        self.add_line('p1-r1-2', (5, 13), (16, 2))
        self.add_line('p1-r1-3', (16, 2), (25, 11))
        self.add_line('p1-r1-4', (25, 11), (27, 13))
        self.add_line('p1-r1-5', (27, 13), (30, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (5, 13), (5, 28))
        self.add_arc('p2-r1-2', (5, 28), (7, 30), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p2-r1-3', (7, 30), (25, 30))
        self.add_arc('p2-r1-4', (25, 30), (27, 28), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (27, 28), (27, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (25, 2), (25, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-5')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-5')
