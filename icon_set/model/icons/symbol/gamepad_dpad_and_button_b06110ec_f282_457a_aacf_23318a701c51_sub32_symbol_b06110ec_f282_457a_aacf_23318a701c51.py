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
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'medias'
    categories = ('medias', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Gamepad: body with two grips, a small d-pad cross and one button, each 4 units from the outline.
        self.add_line('p1-r1-1', (8, 2), (24, 2))
        self.add_arc('p1-r1-2', (24, 2), (30, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 8), (30, 24))
        self.add_arc('p1-r1-4', (30, 24), (24, 30), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 30), (20, 26))
        self.add_line('p1-r1-6', (20, 26), (12, 26))
        self.add_line('p1-r1-7', (12, 26), (8, 30))
        self.add_arc('p1-r1-8', (8, 30), (2, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (2, 24), (2, 8))
        self.add_arc('p1-r1-10', (2, 8), (8, 2), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=True)
        self.add_line('p2-r1-1', (10, 12), (14, 12))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (12, 10), (12, 14))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 12), (22, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
