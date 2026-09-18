"""Independent 32px profile of hedgetrade.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '05838a60-695a-4d60-8b28-c99ff89ec819'
SOURCE_PATH = 'pictographic-primitives/symbol/hedgetrade_05838a60-695a-4d60-8b28-c99ff89ec819.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('05838a60-695a-4d60-8b28-c99ff89ec819', 'pictographic-primitives/symbol/hedgetrade_05838a60-695a-4d60-8b28-c99ff89ec819.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hedgetrade',)
SOLO_SOURCE_ICON_IDS = ('hedgetrade',)
REFERENCE_EXPORT_SHA256 = 'a2472afbb684de3b20ab380f6fb76b685cc29b7e92e3a7e69462b8d925f3c330'

class Drawing(Sub32):
    icon_id = 'hedgetrade-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 2), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (26, 16), (6, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 2), (23, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
