"""Wireframe Globe. """
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5178166e-bac1-49a8-a6de-9ef7d95312d6'
SOURCE_PATH = 'pictographic-primitives/maps/earth_5178166e-bac1-49a8-a6de-9ef7d95312d6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'wireframe-globe'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "maps"
    categories = ("maps", "other", "primitives-generate")
    aliases = ()
    keywords = ('globe', 'earth', 'world', 'wireframe', 'meridian', 'internet', 'global', 'map')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        points = [(cx,cy-ry),(cx+rx,cy),(cx,cy+ry),(cx-rx,cy)]
        for j in range(4):
            self.add_arc(f"{name}-{j}", points[j], points[(j+1)%4], radius_x=rx, radius_y=ry)
        self.add_contour(name, *(f"{name}-{j}" for j in range(4)), closed=True)

    def build(self):
        # Plan: concentric circle and meridian ellipse; shared equator nodes.
        # CIRCLE radius 20 at (24,24). Lucide globe informs symmetric meridians.
        self.circle("rim",24,24,20)
        self.circle("meridian",24,24,9,20)
        self.add_polyline("equator",(4,24),(15,24),(33,24),(44,24))
        self.relate("connect","rim","meridian","equator")
