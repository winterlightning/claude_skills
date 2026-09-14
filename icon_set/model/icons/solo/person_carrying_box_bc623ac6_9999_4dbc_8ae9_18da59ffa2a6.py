"""A left-facing person walks with a lowered head and rounded back while carrying a rectangular box at waist height. One arm crosses the box, and the legs separate into a long stride.
Lucide user construction. Lowered head, supporting arm, rectangular box and long stride retained. Clothing and doubled limb contours omitted; left-facing posture preserved.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc623ac6-9999-4dbc-8ae9-18da59ffa2a6'
SOURCE_PATH = 'pictographic-primitives/work/worker lay off fired user sad box_bc623ac6-9999-4dbc-8ae9-18da59ffa2a6.svg'
AUTHOR = 'gpt-6'


class PersonCarryingBox(Solo48):
    icon_id = 'person-carrying-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('person', 'box', 'carrying', 'walking', 'worker', 'leaving')

    def build(self) -> None:
        self.add_arc('head-top', (16, 10), (24, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (24, 10), (16, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('box', (6, 24), (22, 24), (22, 32), (6, 32), closed=True)
        self.add_polyline('body', (30, 23), (34, 32), (34, 36), (42, 42), closed=False)
        self.add_line('front-leg', (34, 32), (26, 42))
        self.relate("connect", 'front-leg', 'body')
        self.add_line('arm', (30, 23), (22, 32))
        self.relate("connect", 'arm', 'body')
        self.relate("connect", 'arm', 'box')
