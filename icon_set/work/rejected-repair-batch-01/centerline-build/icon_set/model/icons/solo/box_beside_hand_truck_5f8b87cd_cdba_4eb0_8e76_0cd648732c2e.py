from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f8b87cd-cdba-4eb0-8e76-0cd648732c2e'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse package box_5f8b87cd-cdba-4eb0-8e76-0cd648732c2e.svg'
AUTHOR = 'gpt-6-astra'


class BoxBesideHandTruck(Solo48):
    icon_id = 'box-beside-hand-truck'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shipping"
    aliases = ()
    keywords = ('box', 'handtruck', 'parcel', 'warehouse', 'frame', 'handling')

    def build(self) -> None:
        # Square centerlines (6,6)-(42,42); box occludes the left lower rail.
        self.add_polyline("frame", (26,24), (26,14), (26,6))
        self.add_polyline("rail", (42,6), (42,14), (42,24), (42,36))
        self.add_arc("heel", (42,36), (36,42), radius_x=6)
        self.add_line("toe", (36,42), (32,42))
        self.add_contour("foot", "heel", "toe")
        self.relate("connect", "rail", "foot")
        self.add_line("crossbar", (26,14), (42,14))
        self.relate("connect", "frame", "crossbar")
        self.relate("connect", "rail", "crossbar")
        self.add_polyline("box", (6,26), (18,20), (26,24), (30,26), (30,36), (18,42), (6,36), (6,26))
        self.add_polyline("lid", (6,26), (18,32), (30,26))
        self.add_line("corner", (18,32), (18,42))
        self.relate("connect", "box", "lid")
        self.relate("connect", "box", "corner")
        self.relate("connect", "lid", "corner")
        self.relate("connect", "frame", "box")
