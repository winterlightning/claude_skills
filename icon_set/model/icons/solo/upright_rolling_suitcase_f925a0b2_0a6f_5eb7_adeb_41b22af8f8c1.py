"""An upright wheeled suitcase with a raised handle and two front ribs.

Construction: luggage: repeated rounded corners, shared handle axis and paired ribs.
Reduction: Wheel circles reduced to short stubs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f925a0b2-0a6f-5eb7-adeb-41b22af8f8c1'
SOURCE_PATH = 'pictographic-primitives/travel/baggage_f925a0b2-0a6f-5eb7-adeb-41b22af8f8c1.svg'
AUTHOR = 'gpt-6'

class UprightRollingSuitcase(Solo48):
    icon_id = 'upright-rolling-suitcase'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    categories = ('travel', 'primitives')
    aliases = ()
    keywords = ('suitcase', 'luggage', 'baggage', 'travel', 'trolley', 'bag', 'trip')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        left, right, top, bottom, r = (8, 40, 14, 40, 6)
        self.add_line('top-left', (14, top), (16, top))
        self.add_line('top-middle', (16, top), (32, top))
        self.add_line('top-right', (32, top), (34, top))
        self.add_arc('tr', (34, top), (right, 20), radius_x=r)
        self.add_line('right', (right, 20), (right, 34))
        self.add_arc('br', (right, 34), (34, bottom), radius_x=r)
        self.add_line('bottom-right', (34, bottom), (32, bottom))
        self.add_line('bottom-middle', (32, bottom), (16, bottom))
        self.add_line('bottom-left', (16, bottom), (14, bottom))
        self.add_arc('bl', (14, bottom), (left, 34), radius_x=r)
        self.add_line('left', (left, 34), (left, 20))
        self.add_arc('tl', (left, 20), (14, top), radius_x=r)
        self.add_contour('body', 'top-left', 'top-middle', 'top-right', 'tr', 'right', 'br', 'bottom-right', 'bottom-middle', 'bottom-left', 'bl', 'left', 'tl', closed=True)
        self.add_polyline('handle', (16, 14), (16, 4), (32, 4), (32, 14))
        self.relate('connect', 'body', 'handle')
        for i, x in enumerate((16, 32)):
            self.add_line(f'wheel-{i}', (x, 40), (x, 44))
            self.relate('connect', 'body', f'wheel-{i}')
        for i, x in enumerate((20, 28)):
            self.add_line(f'rib-{i}', (x, 23), (x, 31))
