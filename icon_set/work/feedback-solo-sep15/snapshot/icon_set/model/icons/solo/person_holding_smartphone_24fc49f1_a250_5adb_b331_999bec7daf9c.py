"""A front-facing person holds an upright smartphone on the right side of the body. A bent forearm curls around the phone, while the opposite arm hangs straight below the rounded shoulder.
Lucide user head and shoulders; physical upright phone held by the bent right arm. Screen details and finger creases omitted; deliberate right-side asymmetry.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24fc49f1-a250-5adb-b331-999bec7daf9c'
SOURCE_PATH = 'pictographic-primitives/work/meeting smartphone hold_24fc49f1-a250-5adb-b331-999bec7daf9c.svg'
AUTHOR = 'gpt-6'


class PersonHoldingSmartphone(Solo48):
    icon_id = 'person-holding-smartphone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('person', 'smartphone', 'phone', 'holding', 'meeting', 'mobile')

    def build(self) -> None:
        self.add_arc('head-top', (13, 11), (23, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (23, 11), (13, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulder', (6, 36), (16, 26), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('shoulder-top', (16, 26), (22, 26))
        self.add_line('left-arm', (6, 42), (6, 36))
        self.add_contour('body', 'left-arm', 'shoulder', 'shoulder-top', closed=False)
        self.add_polyline('phone', (32, 17), (42, 17), (42, 33), (32, 33), closed=True)
        self.add_polyline('holding-arm', (22, 35), (28, 42), (36, 42), (42, 36), (42, 33), closed=False)
        self.relate("connect", 'holding-arm', 'phone')
