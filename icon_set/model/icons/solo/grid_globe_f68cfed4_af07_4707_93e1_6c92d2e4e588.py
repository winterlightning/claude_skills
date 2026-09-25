"""Grid Globe. """
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f68cfed4-af07-4707-93e1-6c92d2e4e588'
SOURCE_PATH = 'pictographic-primitives/maps/earth_f68cfed4-af07-4707-93e1-6c92d2e4e588.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'grid-globe'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "maps"
    aliases = ()
    keywords = ('globe', 'earth', 'world', 'grid', 'latitude', 'longitude', 'global', 'map')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        points = [(cx,cy-ry),(cx+rx,cy),(cx,cy+ry),(cx-rx,cy)]
        for j in range(4):
            self.add_arc(f"{name}-{j}", points[j], points[(j+1)%4], radius_x=rx, radius_y=ry)
        self.add_contour(name, *(f"{name}-{j}" for j in range(4)), closed=True)

    def build(self):
        # Plan: radius-20 rim; exact 12-16-20 nodes for two straight chords.
        # Reflect about x=24. Lucide globe informs circular rim and equator.
        pts=[(24,4),(36,8),(44,24),(36,40),(24,44),(12,40),(4,24),(12,8)]
        for j in range(8):
            self.add_arc(f"rim-{j}",pts[j],pts[(j+1)%8],radius_x=20)
        self.add_contour("rim",*(f"rim-{j}" for j in range(8)),closed=True)
        for side,x in (("left",12),("right",36)):
            self.add_polyline(side,(x,8),(x,24),(x,40))
            self.relate("connect",side,"rim")
        self.add_polyline("equator",(4,24),(12,24),(36,24),(44,24))
        for part in ("rim","left","right"):
            self.relate("connect","equator",part)
