"""A person carrying a rectangular box walks left with a lowered head. A second figure stands behind on the right, extending one arm horizontally toward the departing worker.
Lucide user circles and shared limb joints. Box carrier and pointing director remain distinct figures; hands, feet outlines and clothing omitted. Leftward departure retained.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18bef7d9-966c-46ce-9638-fea7a1c81585'
SOURCE_PATH = 'pictographic-primitives/work/worker lay off fired user finger box_18bef7d9-966c-46ce-9638-fea7a1c81585.svg'
AUTHOR = 'gpt-6'


class PersonDirectingBoxCarrier(Solo48):
    icon_id = 'person-directing-box-carrier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('person', 'box', 'worker', 'leaving', 'dismissal', 'carrying')

    def build(self) -> None:
        self.add_arc('carrier-head-top', (13, 11), (19, 11), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('carrier-head-bottom', (19, 11), (13, 11), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('carrier-head', 'carrier-head-top', 'carrier-head-bottom', closed=True)
        self.add_polyline('box', (6, 24), (16, 24), (16, 32), (6, 32), closed=True)
        self.add_polyline('carrier', (24, 23), (24, 32), (18, 42), closed=False)
        self.add_line('back-leg', (24, 32), (28, 42))
        self.relate("connect", 'back-leg', 'carrier')
        self.add_line('carrying-arm', (24, 23), (16, 32))
        self.relate("connect", 'carrying-arm', 'carrier')
        self.relate("connect", 'carrying-arm', 'box')
        self.add_arc('director-head-top', (33, 9), (39, 9), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('director-head-bottom', (39, 9), (33, 9), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('director-head', 'director-head-top', 'director-head-bottom', closed=True)
        self.add_polyline('director', (36, 23), (36, 42), (42, 42), closed=False)
        self.add_line('pointing-arm', (36, 23), (24, 23))
        self.relate("connect", 'pointing-arm', 'director')
        self.relate("connect", 'pointing-arm', 'carrier')
        self.relate("connect", 'pointing-arm', 'carrying-arm')
