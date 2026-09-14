"""Moved the equal capsule ends inward and retained both button divisions.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: mouse: tangent capsule construction.
"""
# Independent repair of two-button-mouse; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '74af51b8-794a-4a67-b95c-616f408607d0'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/mouse_74af51b8-794a-4a67-b95c-616f408607d0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('74af51b8-794a-4a67-b95c-616f408607d0', 'pictographic-primitives/computers/batch-03/mouse_74af51b8-794a-4a67-b95c-616f408607d0.svg'), ('dd2baaa6-8560-4803-ae47-3542cfdb8b76', 'pictographic-primitives/computers/batch-03/mouse_dd2baaa6-8560-4803-ae47-3542cfdb8b76.svg'))

class TwoButtonMouseVariant2(Solo48):
    icon_id = 'two-button-mouse-v2'
    variant_of = 'two-button-mouse'
    variant_label = 'Fit current SOLO48 bounds and spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('two', 'button', 'mouse')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_arc('upper-right', (24, 4), (40, 20), radius_x=16, radius_y=16, sweep=True)
        self.add_line('right-upper', (40, 20), (40, 22))
        self.add_line('right-lower', (40, 22), (40, 28))
        self.add_arc('lower-right', (40, 28), (24, 44), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('lower-left', (24, 44), (8, 28), radius_x=16, radius_y=16, sweep=True)
        self.add_line('left-lower', (8, 28), (8, 22))
        self.add_line('left-upper', (8, 22), (8, 20))
        self.add_arc('upper-left', (8, 20), (24, 4), radius_x=16, radius_y=16, sweep=True)
        self.add_contour('body', 'upper-right', 'right-upper', 'right-lower', 'lower-right', 'lower-left', 'left-lower', 'left-upper', 'upper-left', closed=True)
        self.add_line('button-left', (8, 22), (24, 22))
        self.add_line('button-right', (24, 22), (40, 22))
        self.add_contour('buttons', 'button-left', 'button-right', closed=False)
        self.add_line('divider', (24, 4), (24, 22))
        self.relate('connect', 'body', 'buttons')
        self.relate('connect', 'body', 'divider')
        self.relate('connect', 'buttons', 'divider')
