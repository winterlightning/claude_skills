"""A capsule computer mouse with two divided buttons.

VRECT_L: centerline extremes (8,2)-(40,46).
Lucide mouse: concentric arcs / matched tangent corners and shared-axis geometry.
Source duplicates are retained in SOURCE_REFERENCES.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74af51b8-794a-4a67-b95c-616f408607d0'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/mouse_74af51b8-794a-4a67-b95c-616f408607d0.svg'
SOURCE_REFERENCES = (('74af51b8-794a-4a67-b95c-616f408607d0', 'pictographic-primitives/computers/batch-03/mouse_74af51b8-794a-4a67-b95c-616f408607d0.svg'), ('dd2baaa6-8560-4803-ae47-3542cfdb8b76', 'pictographic-primitives/computers/batch-03/mouse_dd2baaa6-8560-4803-ae47-3542cfdb8b76.svg'))


class TwoButtonMouse(Solo48):
    icon_id = 'two-button-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('two', 'button', 'mouse')

    def build(self) -> None:
        self.add_arc('upper-right', (24, 2), (40, 18), radius_x=16, radius_y=16, sweep=True)
        self.add_line('right-upper', (40, 18), (40, 20))
        self.add_line('right-lower', (40, 20), (40, 30))
        self.add_arc('lower-right', (40, 30), (24, 46), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('lower-left', (24, 46), (8, 30), radius_x=16, radius_y=16, sweep=True)
        self.add_line('left-lower', (8, 30), (8, 20))
        self.add_line('left-upper', (8, 20), (8, 18))
        self.add_arc('upper-left', (8, 18), (24, 2), radius_x=16, radius_y=16, sweep=True)
        self.add_contour('body', 'upper-right', 'right-upper', 'right-lower', 'lower-right', 'lower-left', 'left-lower', 'left-upper', 'upper-left', closed=True)
        self.add_line('button-left', (8, 20), (24, 20))
        self.add_line('button-right', (24, 20), (40, 20))
        self.add_contour('buttons', 'button-left', 'button-right', closed=False)
        self.add_line('divider', (24, 2), (24, 20))
        self.relate("connect", 'body', 'buttons')
        self.relate("connect", 'body', 'divider')
        self.relate("connect", 'buttons', 'divider')
