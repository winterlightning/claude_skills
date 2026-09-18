"""Independent 32px profile of car-dashboard-e-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '98f23329-d944-4453-ac48-9d771dfe4fae'
SOURCE_PATH = 'pictographic-primitives/symbol/car dashboard e 1_98f23329-d944-4453-ac48-9d771dfe4fae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('98f23329-d944-4453-ac48-9d771dfe4fae', 'pictographic-primitives/symbol/car dashboard e 1_98f23329-d944-4453-ac48-9d771dfe4fae.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-dashboard-e-1',)
SOLO_SOURCE_ICON_IDS = ('car-dashboard-e-1',)
REFERENCE_EXPORT_SHA256 = '5fb2f3dce3acf6d7f97ac497637c58939f026089cc1dcbbd1ed7d9128141e62d'

class Drawing(Sub32):
    icon_id = 'car-dashboard-e-1-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 2), (5, 2))
        self.add_line('p1-r1-2', (5, 2), (5, 18))
        self.add_line('p1-r1-3', (5, 18), (13, 18))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (5, 10), (12, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27, 12), (9, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
