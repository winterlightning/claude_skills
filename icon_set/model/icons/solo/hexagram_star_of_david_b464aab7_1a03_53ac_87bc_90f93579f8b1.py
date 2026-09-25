"""A complete six-pointed hexagram with two intersecting triangles. Preserve the central hexagon and six triangular openings; no useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b464aab7-1a03-53ac-87bc-90f93579f8b1'
SOURCE_PATH = 'pictographic-primitives/religion/hexagram_b464aab7-1a03-53ac-87bc-90f93579f8b1.svg'
AUTHOR = 'gpt-6'

class HexagramStarOfDavid(Solo48):
    icon_id = 'hexagram-star-of-david'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('star', 'david', 'hexagram', 'judaism', 'symbol', 'triangle')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (6,6)-(42,42); crossings are shared integer nodes.
        self.add_polyline('up',(24,6),(30,15),(36,24),(42,33),(30,33),(18,33),(6,33),(12,24),(18,15),closed=True)
        self.add_polyline('down',(6,15),(18,15),(30,15),(42,15),(36,24),(30,33),(24,42),(18,33),(12,24),closed=True)
        self.relate('connect','up','down')
