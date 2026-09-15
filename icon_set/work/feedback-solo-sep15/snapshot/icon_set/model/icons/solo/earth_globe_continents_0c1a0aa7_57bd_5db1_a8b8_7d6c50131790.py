"""Earth Globe with Continents. """
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0c1a0aa7-57bd-5db1-a8b8-7d6c50131790'
SOURCE_PATH = 'pictographic-primitives/maps/earth 1_0c1a0aa7-57bd-5db1-a8b8-7d6c50131790.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'earth-globe-continents'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/maps"
    aliases = ()
    keywords = ('earth', 'globe', 'world', 'planet', 'continents', 'map', 'global', 'geography')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        points = [(cx,cy-ry),(cx+rx,cy),(cx,cy+ry),(cx-rx,cy)]
        for j in range(4):
            self.add_arc(f"{name}-{j}", points[j], points[(j+1)%4], radius_x=rx, radius_y=ry)
        self.add_contour(name, *(f"{name}-{j}" for j in range(4)), closed=True)

    def build(self):
        # Plan: radius-20 earth; two distinct coastlines join exact rim nodes.
        # Lucide earth informs few coherent coastline arcs; intentional land asymmetry.
        pts=[(24,4),(36,8),(44,24),(36,40),(24,44),(12,40),(4,24),(12,8)]
        for j in range(len(pts)):
            self.add_arc(f"rim-{j}",pts[j],pts[(j+1)%len(pts)],radius_x=20)
        self.add_contour("rim",*(f"rim-{j}" for j in range(len(pts))),closed=True)
        self.add_line("west-start",(12,8),(12,12))
        self.add_arc("west-upper",(12,12),(20,20),radius_x=8,sweep=False)
        self.add_arc("west-middle",(20,20),(26,26),radius_x=6)
        self.add_line("west-run",(26,26),(26,32))
        self.add_arc("west-lower",(26,32),(36,40),radius_x=10,radius_y=8,sweep=False)
        self.add_contour("west","west-start","west-upper","west-middle","west-run","west-lower")
        self.add_line("east-upper",(36,8),(32,16))
        self.add_arc("east-bend",(32,16),(40,24),radius_x=8,sweep=False)
        self.add_line("east-end",(40,24),(44,24))
        self.add_contour("east","east-upper","east-bend","east-end")
        self.relate("connect","rim","west")
        self.relate("connect","rim","east")
