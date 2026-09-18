"""Independent 32px profile of diagonal-pencil-plain-tip.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4c398c0b-71ae-4681-a50b-2dd50dab7c0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pencil_4c398c0b-71ae-4681-a50b-2dd50dab7c0f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4c398c0b-71ae-4681-a50b-2dd50dab7c0f', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pencil_4c398c0b-71ae-4681-a50b-2dd50dab7c0f.svg'), ('4f8e2fe8-7ce0-4a78-8f6d-47387d8649e8', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pencil_4f8e2fe8-7ce0-4a78-8f6d-47387d8649e8.svg'), ('af6d609a-560f-4248-a671-cfb36522af0d', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/pencil_af6d609a-560f-4248-a671-cfb36522af0d.svg'))
PROFILE_SOURCE_KEYS = ('solo/diagonal-pencil-plain-tip', 'solo/diagonal-writing-pencil-long-tip', 'solo/diagonal-writing-pencil-rounded-cap')
SOLO_SOURCE_ICON_IDS = ('diagonal-pencil-plain-tip', 'diagonal-writing-pencil-long-tip', 'diagonal-writing-pencil-rounded-cap')
REFERENCE_EXPORT_SHA256 = '26eaa7d972efbe3bc371901b426639b7fb0172714116ebfc08247b0c145b9cfb'

class DrawingContainerSymbol(Sub32):
    icon_id = 'diagonal-pencil-plain-tip-sub32-symbol'
    related_origin_icon_id = 'diagonal-pencil-plain-tip-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/diagonal-pencil-plain-tip-sub32'
    counterpart_icon_id = 'diagonal-pencil-plain-tip-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (5, 19))
        self.add_line('p1-r1-2', (5, 19), (18, 7))
        self.add_line('p1-r1-3', (18, 7), (21, 4))
        self.add_bezier('p1-r1-4', (21, 4), ((22, 2), (23, 2), (24, 2)))
        self.add_bezier('p1-r1-5', (24, 2), ((25, 2), (30, 7), (30, 8)))
        self.add_bezier('p1-r1-6', (30, 8), ((30, 9), (30, 10), (28, 11)))
        self.add_line('p1-r1-7', (28, 11), (25, 14))
        self.add_line('p1-r1-8', (25, 14), (13, 27))
        self.add_line('p1-r1-9', (13, 27), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (18, 7), (25, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
