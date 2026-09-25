"""Location Crosshair. """
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9962da7a-8bcb-57a1-963a-b4daa96b9602'
SOURCE_PATH = 'pictographic-primitives/maps/location target_9962da7a-8bcb-57a1-963a-b4daa96b9602.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'location-crosshair'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "maps"
    aliases = ()
    keywords = ('crosshair', 'target', 'location', 'gps', 'locate', 'aim', 'center', 'map')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        points = [(cx,cy-ry),(cx+rx,cy),(cx,cy+ry),(cx-rx,cy)]
        for j in range(4):
            self.add_arc(f"{name}-{j}", points[j], points[(j+1)%4], radius_x=rx, radius_y=ry)
        self.add_contour(name, *(f"{name}-{j}" for j in range(4)), closed=True)

    def build(self):
        # Plan: concentric rings with four identical radial ticks, radius-20 envelope.
        # Lucide locate-fixed supplies the ring/tick hierarchy. Small circle r=3.
        self.circle("rim",24,24,14)
        self.circle("center",24,24,3)
        for name,outer,node,inner in (
            ("top",(24,4),(24,10),(24,12)),
            ("right",(44,24),(38,24),(36,24)),
            ("bottom",(24,44),(24,38),(24,36)),
            ("left",(4,24),(10,24),(12,24))):
            self.add_polyline(name,outer,node,inner)
            self.relate("connect",name,"rim")
