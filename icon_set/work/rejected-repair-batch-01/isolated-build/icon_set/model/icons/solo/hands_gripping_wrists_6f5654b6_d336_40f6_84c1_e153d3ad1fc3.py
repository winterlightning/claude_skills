"""Four hands and forearms form a square loop around a small central opening. Each hand wraps around the neighboring wrist, with bent fingers marking the four outer corners.
Lucide hand grip and repeated corner construction. Four quarter-turn grips surround a square opening. Small fingers reduced to diagonal grip seams; shared radii and rotational symmetry retained.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f5654b6-d336-40f6-84c1-e153d3ad1fc3'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork hand lock_6f5654b6-d336-40f6-84c1-e153d3ad1fc3.svg'
AUTHOR = 'gpt-6'


class HandsGrippingWrists(Solo48):
    icon_id = 'hands-gripping-wrists'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('hands', 'wrist', 'grip', 'teamwork', 'unity', 'cooperation')

    def build(self) -> None:
        self.add_line('outer-t', (12, 6), (36, 6))
        self.add_arc('outer-ne', (36, 6), (42, 12), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('outer-r', (42, 12), (42, 36))
        self.add_arc('outer-se', (42, 36), (36, 42), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('outer-b', (36, 42), (12, 42))
        self.add_arc('outer-sw', (12, 42), (6, 36), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('outer-l', (6, 36), (6, 12))
        self.add_arc('outer-nw', (6, 12), (12, 6), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('outer', 'outer-t', 'outer-ne', 'outer-r', 'outer-se', 'outer-b', 'outer-sw', 'outer-l', 'outer-nw', closed=True)
        self.add_polyline('opening', (18, 18), (30, 18), (30, 30), (18, 30), closed=True)
        self.add_polyline('grip-0', (18, 6), (26, 18), closed=False)
        self.relate("connect", 'grip-0', 'outer')
        self.relate("connect", 'grip-0', 'opening')
        self.add_polyline('grip-1', (42, 18), (30, 26), closed=False)
        self.relate("connect", 'grip-1', 'outer')
        self.relate("connect", 'grip-1', 'opening')
        self.add_polyline('grip-2', (30, 42), (22, 30), closed=False)
        self.relate("connect", 'grip-2', 'outer')
        self.relate("connect", 'grip-2', 'opening')
        self.add_polyline('grip-3', (6, 30), (18, 22), closed=False)
        self.relate("connect", 'grip-3', 'outer')
        self.relate("connect", 'grip-3', 'opening')
