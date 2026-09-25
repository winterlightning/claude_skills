"""Desk Globe on Stand. """
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd7db4bca-68d7-4e3b-b134-1375e3f3d159'
SOURCE_PATH = 'pictographic-primitives/maps/earth model_d7db4bca-68d7-4e3b-b134-1375e3f3d159.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'desk-globe-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "maps"
    categories = ("maps", "primitives")
    aliases = ()
    keywords = ('globe', 'desk globe', 'earth', 'world', 'geography', 'school', 'stand', 'map')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        points = [(cx,cy-ry),(cx+rx,cy),(cx,cy+ry),(cx-rx,cy)]
        for j in range(4):
            self.add_arc(f"{name}-{j}", points[j], points[(j+1)%4], radius_x=rx, radius_y=ry)
        self.add_contour(name, *(f"{name}-{j}" for j in range(4)), closed=True)

    def build(self):
        # Plan: radius-10 globe and concentric radius-20 support, tilted 3:4 axis.
        # Exact integer attachment nodes; VRECT_L extremes (8,4)..(40,44).
        # Lucide globe informs circles; omit continent to preserve support clearance.
        self.add_arc("globe-a",(20,10),(36,22),radius_x=10)
        self.add_arc("globe-b",(36,22),(20,10),radius_x=10)
        self.add_contour("globe","globe-a","globe-b",closed=True)
        self.add_arc("support-a",(12,4),(8,16),radius_x=20,sweep=False)
        self.add_arc("support-b",(8,16),(28,36),radius_x=20,sweep=False)
        self.add_arc("support-c",(28,36),(40,32),radius_x=20,sweep=False)
        self.add_contour("support","support-a","support-b","support-c")
        self.add_line("axis-top",(12,4),(20,10))
        self.add_line("axis-bottom",(36,22),(40,32))
        for part in ("axis-top","axis-bottom"):
            self.relate("connect",part,"support")
            self.relate("connect",part,"globe")
        self.add_line("post",(28,36),(28,44))
        self.add_polyline("base",(16,44),(28,44),(40,44))
        self.relate("connect","post","support")
        self.relate("connect","post","base")
