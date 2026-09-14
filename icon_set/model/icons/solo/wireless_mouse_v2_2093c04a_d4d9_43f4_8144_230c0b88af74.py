"""Inset equal capsule ends and moved the wheel for a certified gap.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: mouse: tangent capsule and single wheel stroke.
"""
# Independent repair of wireless-mouse; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2093c04a-d4d9-43f4-8144-230c0b88af74'
SOURCE_PATH = 'pictographic-primitives/computers/batch-07/mouse smart_2093c04a-d4d9-43f4-8144-230c0b88af74.svg'
AUTHOR = 'gpt-6'

class WirelessMouseVariant2(Solo48):
    icon_id = 'wireless-mouse-v2'
    variant_of = 'wireless-mouse'
    variant_label = 'Fit current SOLO48 bounds and spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ('cordless mouse',)
    keywords = ('mouse', 'wireless', 'scroll wheel', 'computer', 'peripheral')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_line('body-top', (22, 4), (26, 4))
        self.add_arc('body-ne', (26, 4), (40, 18), radius_x=14)
        self.add_line('body-right', (40, 18), (40, 30))
        self.add_arc('body-se', (40, 30), (26, 44), radius_x=14)
        self.add_line('body-bottom', (26, 44), (22, 44))
        self.add_arc('body-sw', (22, 44), (8, 30), radius_x=14)
        self.add_line('body-left', (8, 30), (8, 18))
        self.add_arc('body-nw', (8, 18), (22, 4), radius_x=14)
        self.add_contour('body', 'body-top', 'body-ne', 'body-right', 'body-se', 'body-bottom', 'body-sw', 'body-left', 'body-nw', closed=True)
        self.add_line('scroll-wheel', (24, 13), (24, 20))
