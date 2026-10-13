"""Independent 32px profile of bulb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9c7b548b-f26b-4b87-8dac-75d503bfd7a8'
SOURCE_PATH = 'pictographic-primitives/work/bulb_9c7b548b-f26b-4b87-8dac-75d503bfd7a8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c7b548b-f26b-4b87-8dac-75d503bfd7a8', 'pictographic-primitives/work/bulb_9c7b548b-f26b-4b87-8dac-75d503bfd7a8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bulb',)
SOLO_SOURCE_ICON_IDS = ('bulb',)
REFERENCE_EXPORT_SHA256 = 'd5fddd089f172cf11dfe70931054bb5aa9b03c0c8e03a6670c4cc2adca612a98'

class Drawing(Sub32):
    icon_id = 'bulb-sub32'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'work'
    categories = ('work', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Light bulb: round top narrowing smoothly into a straight neck with a flat base.
        self.add_arc('globe', (8, 10), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_bezier('shoulder-r', (24, 10), ((24, 15), (20, 17), (20, 20)))
        self.add_line('neck-r', (20, 20), (20, 30))
        self.add_line('base', (20, 30), (12, 30))
        self.add_line('neck-l', (12, 30), (12, 20))
        self.add_bezier('shoulder-l', (12, 20), ((12, 17), (8, 15), (8, 10)))
        self.add_contour('bulb', 'globe', 'shoulder-r', 'neck-r', 'base', 'neck-l', 'shoulder-l', closed=True)
