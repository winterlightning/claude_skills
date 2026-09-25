"""Independent 32px profile of refresh.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2fd1c079-cf3a-416d-9512-f7ec606bfef0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/refresh_2fd1c079-cf3a-416d-9512-f7ec606bfef0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2fd1c079-cf3a-416d-9512-f7ec606bfef0', 'pictographic-primitives/interface-essential/refresh_2fd1c079-cf3a-416d-9512-f7ec606bfef0.svg'), ('d1b39612-4343-4bf6-ac61-b3e0ef51391b', 'pictographic-primitives/interface-essential/refresh_d1b39612-4343-4bf6-ac61-b3e0ef51391b.svg'))
PROFILE_SOURCE_KEYS = ('solo/refresh', 'solo/refresh-interface-essential')
SOLO_SOURCE_ICON_IDS = ('refresh', 'refresh-interface-essential')
REFERENCE_EXPORT_SHA256 = '3ee72e744cf019a9db7001938e187e86d38fbe6364f5c26522e3e7754c7d0b9c'

class DrawingContainerSymbol(Sub32):
    icon_id = 'refresh-sub32-symbol'
    related_origin_icon_id = 'refresh-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/refresh-sub32'
    counterpart_icon_id = 'refresh-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (2, 16), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-3', (16, 2), ((21, 2), (25, 5), (28, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (28, 2), (28, 10))
        self.add_line('p2-r1-2', (28, 10), (21, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
