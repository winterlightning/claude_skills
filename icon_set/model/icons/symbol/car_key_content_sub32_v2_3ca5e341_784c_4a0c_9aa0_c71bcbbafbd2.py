"""Independent 32px profile of car-key-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3ca5e341-784c-4a0c-9aa0-c71bcbbafbd2'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/3ca5e341-784c-4a0c-9aa0-c71bcbbafbd2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ca5e341-784c-4a0c-9aa0-c71bcbbafbd2', 'icon_set/dist/gallery/combination-originals/3ca5e341-784c-4a0c-9aa0-c71bcbbafbd2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-key-content',)
SOLO_SOURCE_ICON_IDS = ('car-key-content',)
REFERENCE_EXPORT_SHA256 = 'c3ef8204cd2eabfdb69ddf83678b6a340d0a5e58dfd09d770ecdd7ef0c329cb1'

class DrawingVariant2(Sub32):
    icon_id = 'car-key-content-sub32-v2'
    related_origin_icon_id = 'car-key-content-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 27), (short_low, 21))
        self.add_line('p1-r1-2', (short_low, 21), (8, 17))
        self.add_line('p1-r1-3', (8, 17), (24, 17))
        self.add_line('p1-r1-4', (24, 17), (short_high, 21))
        self.add_line('p1-r1-5', (short_high, 21), (short_high, 27))
        self.add_line('p1-r1-6', (short_high, 27), (short_low, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 27), (8, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 27), (24, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (20, 6), (short_high, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (short_high, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (short_low, 6), (20, 6))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (9, 6), (9, 11))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-2', 'p5-r1-1')
