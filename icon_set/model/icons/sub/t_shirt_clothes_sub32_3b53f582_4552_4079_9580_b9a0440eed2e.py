"""Independent 32px profile of t-shirt-clothes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3b53f582-4552-4079-9580-b9a0440eed2e'
SOURCE_PATH = 'pictographic-primitives/clothes/t shirt_3b53f582-4552-4079-9580-b9a0440eed2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3b53f582-4552-4079-9580-b9a0440eed2e', 'pictographic-primitives/clothes/t shirt_3b53f582-4552-4079-9580-b9a0440eed2e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/t-shirt-clothes',)
SOLO_SOURCE_ICON_IDS = ('t-shirt-clothes',)
REFERENCE_EXPORT_SHA256 = '5b4e5ac8c022667cf3ac40dbb4523522c7474644542029ebea9addbaf6dbce02'

class Drawing(Sub32):
    icon_id = 't-shirt-clothes-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'clothes'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (11, 5), ((12, 6), (14, 7), (16, 7)))
        self.add_bezier('p1-r1-2', (16, 7), ((18, 7), (20, 6), (21, 5)))
        self.add_line('p1-r1-3', (21, 5), (30, 9))
        self.add_line('p1-r1-4', (30, 9), (27, 15))
        self.add_line('p1-r1-5', (27, 15), (22, 15))
        self.add_line('p1-r1-6', (22, 15), (22, 27))
        self.add_line('p1-r1-7', (22, 27), (10, 27))
        self.add_line('p1-r1-8', (10, 27), (10, 15))
        self.add_line('p1-r1-9', (10, 15), (5, 15))
        self.add_line('p1-r1-10', (5, 15), (2, 9))
        self.add_line('p1-r1-11', (2, 9), (11, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
