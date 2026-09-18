"""Independent 32px profile of gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b06110ec-f282-457a-aacf-23318a701c51'
SOURCE_PATH = 'pictographic-primitives/medias/gaming_b06110ec-f282-457a-aacf-23318a701c51.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b06110ec-f282-457a-aacf-23318a701c51', 'pictographic-primitives/medias/gaming_b06110ec-f282-457a-aacf-23318a701c51.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51',)
SOLO_SOURCE_ICON_IDS = ('gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51',)
REFERENCE_EXPORT_SHA256 = '9934ba54fd0ca9c5f69b82ef829f07382dcb65e789b1e35490934e236c5c4d93'

class DrawingContainerSymbol(Sub32):
    icon_id = 'gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51-sub32-symbol'
    related_origin_icon_id = 'gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51-sub32'
    counterpart_icon_id = 'gamepad-dpad-and-button-b06110ec-f282-457a-aacf-23318a701c51-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/media'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 5), (23, 5))
        self.add_arc('p1-r1-2', (23, 5), (30, 22), radius_x=7, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (30, 22), (19, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (19, 22), (13, 22), radius_x=3, radius_y=1, large_arc=False, sweep=False)
        self.add_arc('p1-r1-5', (13, 22), (2, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (2, 22), (9, 5), radius_x=7, radius_y=17, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (11, 14), (9, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (11, 14), (13, 14))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (11, 14), (11, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (11, 14), (11, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (22, 14), (22, 14))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
