"""Location Pin with Nearby Arcs. """
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '220bbf43-6896-4af5-81dd-f25dbd490f97'
SOURCE_PATH = 'pictographic-primitives/maps/close edge location_220bbf43-6896-4af5-81dd-f25dbd490f97.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'location-pin-nearby-arcs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/maps"
    aliases = ()
    keywords = ('location', 'nearby', 'pin', 'map', 'gps', 'place', 'proximity', 'area')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        points = [(cx,cy-ry),(cx+rx,cy),(cx,cy+ry),(cx-rx,cy)]
        for j in range(4):
            self.add_arc(f"{name}-{j}", points[j], points[(j+1)%4], radius_x=rx, radius_y=ry)
        self.add_contour(name, *(f"{name}-{j}" for j in range(4)), closed=True)

    def build(self):
        # Plan: symmetric pin above three nearby arcs. SQUARE extremes 6,6..42,42.
        # Lucide map-pin informs rounded head; retain the source's proximity arcs.
        self.add_arc("head",(13,17),(35,17),radius_x=11)
        self.add_arc("pin-right-round",(35,17),(31,25),radius_x=10)
        self.add_line("pin-right",(31,25),(24,32))
        self.add_line("pin-left",(24,32),(17,25))
        self.add_arc("pin-left-round",(17,25),(13,17),radius_x=10)
        self.add_contour("pin","head","pin-right-round","pin-right","pin-left","pin-left-round",closed=True)
        self.circle("hole",24,17,2)
        self.add_arc("ground",(16,42),(32,42),radius_x=8,radius_y=1)
        self.add_arc("nearby-left",(6,42),(10,32),radius_x=4,radius_y=10)
        self.add_arc("nearby-right",(38,32),(42,42),radius_x=4,radius_y=10)
