"""A person leans forward while leaving a doorway to the right. A foot projects from the left through the opening toward a jagged impact mark behind the departing figure.
Lucide user limb construction; no exact useful kick-scene match. Door jamb, projecting foot and departing stride retained. Separate impact zigzag omitted; direction is deliberately rightward.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e4661f1-6214-410b-ac73-2cf060f547fc'
SOURCE_PATH = 'pictographic-primitives/work/worker lay off fired user door kick_5e4661f1-6214-410b-ac73-2cf060f547fc.svg'
AUTHOR = 'gpt-6'


class PersonKickedThroughDoorway(Solo48):
    icon_id = 'person-kicked-through-doorway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    aliases = ()
    keywords = ('person', 'door', 'kick', 'leaving', 'dismissal', 'worker')

    def build(self) -> None:
        self.add_polyline('door', (20, 6), (6, 6), (6, 25), (6, 42), (20, 42), closed=False)
        self.add_polyline('foot', (6, 25), (16, 29), (18, 24), closed=False)
        self.relate("connect", 'foot', 'door')
        self.add_arc('head-top', (30, 10), (38, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (38, 10), (30, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (30, 23), (26, 32), (30, 42), closed=False)
        self.add_line('stride', (26, 32), (42, 38))
        self.relate("connect", 'stride', 'body')
        self.add_polyline('arm', (30, 23), (36, 28), (42, 28), closed=False)
        self.relate("connect", 'arm', 'body')
