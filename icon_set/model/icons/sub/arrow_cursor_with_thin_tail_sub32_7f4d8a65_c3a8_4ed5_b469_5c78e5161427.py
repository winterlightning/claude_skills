"""Independent 32px profile of arrow-cursor-with-thin-tail.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7f4d8a65-c3a8-4ed5-b469-5c78e5161427'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor left 1_7f4d8a65-c3a8-4ed5-b469-5c78e5161427.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7f4d8a65-c3a8-4ed5-b469-5c78e5161427', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor left 1_7f4d8a65-c3a8-4ed5-b469-5c78e5161427.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-cursor-with-thin-tail',)
SOLO_SOURCE_ICON_IDS = ('arrow-cursor-with-thin-tail',)
REFERENCE_EXPORT_SHA256 = 'cb4e3b694ebaffe9bf4778119dc74e683d25bc75414141d43b077f8441ff9d59'

class Drawing(Sub32):
    icon_id = 'arrow-cursor-with-thin-tail-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (30, 14))
        self.add_line('p1-r1-2', (30, 14), (18, 18))
        self.add_line('p1-r1-3', (18, 18), (14, 30))
        self.add_line('p1-r1-4', (14, 30), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (18, 18), (28, 28))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
