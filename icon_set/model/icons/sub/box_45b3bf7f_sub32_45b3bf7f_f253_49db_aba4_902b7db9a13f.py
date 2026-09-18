"""Independent 32px profile of box-45b3bf7f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '45b3bf7f-f253-49db-aba4-902b7db9a13f'
SOURCE_PATH = 'pictographic-primitives/shipping/box_45b3bf7f-f253-49db-aba4-902b7db9a13f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('45b3bf7f-f253-49db-aba4-902b7db9a13f', 'pictographic-primitives/shipping/box_45b3bf7f-f253-49db-aba4-902b7db9a13f.svg'), ('20c6ed49-886d-4ca0-b960-c8322bf94767', 'pictographic-primitives/shipping/box_20c6ed49-886d-4ca0-b960-c8322bf94767.svg'))
PROFILE_SOURCE_KEYS = ('solo/box-45b3bf7f', 'solo/box-shipping')
SOLO_SOURCE_ICON_IDS = ('box-45b3bf7f', 'box-shipping')
REFERENCE_EXPORT_SHA256 = 'ae048e94a81a6c26aeb92df3e96b51046060420e801744f469d20ed59fbfc800'

class Drawing(Sub32):
    icon_id = 'box-45b3bf7f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'shipping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 10), (9, 6))
        self.add_line('p1-r1-2', (9, 6), (16, 2))
        self.add_line('p1-r1-3', (16, 2), (30, 10))
        self.add_line('p1-r1-4', (30, 10), (30, 22))
        self.add_line('p1-r1-5', (30, 22), (16, 30))
        self.add_line('p1-r1-6', (16, 30), (2, 22))
        self.add_line('p1-r1-7', (2, 22), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (2, 10), (16, 18))
        self.add_line('p2-r1-2', (16, 18), (23, 14))
        self.add_line('p2-r1-3', (23, 14), (30, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (16, 18), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
        self.relate("connect", 'p1-r1-4', 'p2-r1-3')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
