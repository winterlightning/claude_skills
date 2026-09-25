"""Cluster of Three Pins. """
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7e29c513-d49d-4943-a3b9-d82d5a705611'
SOURCE_PATH = 'pictographic-primitives/maps/trip pin multiple_7e29c513-d49d-4943-a3b9-d82d5a705611.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'three-pin-cluster'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "maps"
    categories = ("maps", "primitives")
    aliases = ()
    keywords = ('pins', 'locations', 'multiple', 'trip', 'map', 'places', 'markers', 'route')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        points = [(cx,cy-ry),(cx+rx,cy),(cx,cy+ry),(cx-rx,cy)]
        for j in range(4):
            self.add_arc(f"{name}-{j}", points[j], points[(j+1)%4], radius_x=rx, radius_y=ry)
        self.add_contour(name, *(f"{name}-{j}" for j in range(4)), closed=True)

    def build(self):
        # Plan: three overlapping pin silhouettes; mirrored rear lobes, front pin.
        # HRECT_L extremes 4,8..44,40. Lucide map-pin supplies teardrop construction.
        # Occluded rear edges are omitted; contacts use shared front shoulder nodes.
        self.add_arc("rear-left-head",(4,16),(20,16),radius_x=8)
        self.add_line("rear-left-in",(20,16),(16,24))
        self.add_line("rear-left-out",(4,16),(4,24))
        self.add_arc("rear-left-round",(4,24),(12,32),radius_x=8,sweep=False)
        self.add_line("rear-left-tip",(12,32),(16,24))
        self.add_contour("rear-left","rear-left-head","rear-left-in")
        self.add_contour("rear-left-tail","rear-left-out","rear-left-round","rear-left-tip")
        self.add_arc("rear-right-head",(28,16),(44,16),radius_x=8)
        self.add_line("rear-right-out",(44,16),(44,24))
        self.add_arc("rear-right-round",(44,24),(36,32),radius_x=8)
        self.add_line("rear-right-tip",(36,32),(32,24))
        self.add_contour("rear-right","rear-right-head","rear-right-out","rear-right-round","rear-right-tip")
        self.add_line("rear-right-in",(28,16),(32,24))
        self.add_arc("front-head",(16,24),(32,24),radius_x=8)
        self.add_line("front-tip-1",(32,24),(24,36))
        self.add_line("front-tip-2",(24,36),(16,24))
        self.add_contour("front","front-head","front-tip-1","front-tip-2",closed=True)
        self.add_line("stem",(24,36),(24,40))
        self.relate("connect","stem","front")
        for a,b in (("rear-left","rear-left-tail"),("rear-left","front"),("rear-left-tail","front"),("rear-right","front"),("rear-right-in","front"),("rear-right-in","rear-right")):
            self.relate("connect",a,b)
