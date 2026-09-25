"""A hand wraps around the right side of a circular stopwatch, with four fingers stacked along its edge. A top plunger rises above the dial, which contains one short diagonal hand.
Lucide timer circular dial and diagonal needle; hand construction from pointer. Plunger, wrapped palm and wrist retained. Four fingers simplified into one curved grip; asymmetry follows the right-handed grasp.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a430fc9d-29f3-4753-b308-1283a45b63e1'
SOURCE_PATH = 'pictographic-primitives/work/workflow coaching stopwatch hand_a430fc9d-29f3-4753-b308-1283a45b63e1.svg'
AUTHOR = 'gpt-6'


class HandHoldingStopwatch(Solo48):
    icon_id = 'hand-holding-stopwatch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('hand', 'stopwatch', 'timer', 'time', 'holding', 'coaching')

    def build(self) -> None:
        self.add_line('plunger', (22, 6), (22, 10))
        self.add_arc('dial-right', (22, 10), (22, 38), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('dial-left', (22, 38), (22, 10), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_contour('watch', 'plunger', 'dial-right', 'dial-left', closed=False)
        self.add_polyline('button', (18, 6), (22, 6), (26, 6), closed=False)
        self.relate("connect", 'button', 'watch')
        self.add_line('needle', (22, 24), (18, 20))
        self.add_line('fingers-top', (36, 24), (38, 24))
        self.add_arc('finger-round', (38, 24), (42, 28), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('fingers-side', (42, 28), (42, 34))
        self.add_arc('palm', (42, 34), (38, 38), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('palm-base', (38, 38), (28, 38))
        self.add_line('wrist-slope', (28, 38), (18, 42))
        self.add_line('wrist', (18, 42), (6, 42))
        self.add_contour('hand', 'fingers-top', 'finger-round', 'fingers-side', 'palm', 'palm-base', 'wrist-slope', 'wrist', closed=False)
        self.relate("connect", 'hand', 'watch')
        self.add_line('upper-wrist', (6, 30), (8, 24))
        self.relate("connect", 'upper-wrist', 'watch')
