"""Independent 32px profile of clock.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '05b85708-b328-4db0-9c82-4b28b3be56f5'
SOURCE_PATH = 'pictographic-primitives/office/clock_05b85708-b328-4db0-9c82-4b28b3be56f5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('05b85708-b328-4db0-9c82-4b28b3be56f5', 'pictographic-primitives/office/clock_05b85708-b328-4db0-9c82-4b28b3be56f5.svg'), ('4ab76b4c-c88a-4586-b84f-4ffd7244d650', 'pictographic-primitives/office/clock_4ab76b4c-c88a-4586-b84f-4ffd7244d650.svg'), ('9f37004b-ad82-4bff-ba0a-63d3fdc12e97', 'pictographic-primitives/office/clock_9f37004b-ad82-4bff-ba0a-63d3fdc12e97.svg'), ('e7f654f6-570d-40dd-84e5-be7ff0923e87', 'pictographic-primitives/office/clock_e7f654f6-570d-40dd-84e5-be7ff0923e87.svg'), ('282df875-ad80-4f27-9f87-f3b69a27f229', 'pictographic-primitives/office/clock_282df875-ad80-4f27-9f87-f3b69a27f229.svg'))
PROFILE_SOURCE_KEYS = ('solo/clock', 'solo/clock-4ab76b4c', 'solo/clock-9f37004b', 'solo/clock-e7f654f6', 'solo/clock-office')
SOLO_SOURCE_ICON_IDS = ('clock', 'clock-4ab76b4c', 'clock-9f37004b', 'clock-e7f654f6', 'clock-office')
REFERENCE_EXPORT_SHA256 = '67967de3ce3da04a245c136daacce4ac2b999fd318a8e7fa7ed24de1c16aa015'

class DrawingContainerSymbol(Sub32):
    icon_id = 'clock-sub32-symbol'
    related_origin_icon_id = 'clock-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/clock-sub32'
    counterpart_icon_id = 'clock-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'office'
    categories = ('office', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 8), (16, 16))
        self.add_line('p2-r1-2', (16, 16), (21, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
