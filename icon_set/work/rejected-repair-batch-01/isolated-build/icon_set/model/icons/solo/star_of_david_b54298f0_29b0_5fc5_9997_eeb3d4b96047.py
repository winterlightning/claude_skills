"""A six-pointed Star of David. Shared vertical and horizontal axes preserve the hexagram silhouette; preserve both crossing triangles and omit only the tiny source tip notches."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b54298f0-29b0-5fc5-9997-eeb3d4b96047'
SOURCE_PATH = 'pictographic-primitives/religion/astrology david_b54298f0-29b0-5fc5-9997-eeb3d4b96047.svg'
AUTHOR = 'gpt-6'


class StarOfDavid(Solo48):
    icon_id = 'star-of-david'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('star', 'david', 'hexagram', 'judaism', 'symbol', 'triangle')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Live SQUARE centerline box (6,6)-(42,42).
        # Both triangles share exact crossing nodes; vertical axis x=24.
        self.add_polyline('up',(24,6),(30,15),(36,24),(42,33),(30,33),(18,33),(6,33),(12,24),(18,15),closed=True)
        self.add_polyline('down',(6,15),(18,15),(30,15),(42,15),(36,24),(30,33),(24,42),(18,33),(12,24),closed=True)
        self.relate('connect','up','down')
