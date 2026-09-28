"""A broad chalice on a stem and flared foot. Lucide wine informs the coherent bowl, stem and foot; omit decorative stem beads."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '188e9da1-e301-5033-8cca-278e325932fc'
SOURCE_PATH = 'pictographic-primitives/religion/greek grail_188e9da1-e301-5033-8cca-278e325932fc.svg'
AUTHOR = 'gpt-6'

class StemmedChalice(Solo48):
    icon_id = 'greek-stemmed-chalice'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    categories = ("primitives", "religion")
    aliases = ()
    keywords = ('chalice', 'grail', 'cup', 'goblet', 'stem', 'vessel')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (8,4)-(40,44).
        self.add_polyline('rim',(8,4),(40,4),(40,12))
        self.add_arc('bowl-right',(40,12),(24,28),radius_x=16)
        self.add_arc('bowl-left',(24,28),(8,12),radius_x=16)
        self.add_line('rim-left',(8,12),(8,4))
        self.add_contour('bowl','bowl-right','bowl-left','rim-left')
        self.relate('connect','bowl','rim')
        self.add_line('band',(8,12),(40,12))
        self.relate('connect','band','rim');self.relate('connect','band','bowl')
        self.add_line('stem',(24,28),(24,36))
        self.add_polyline('foot',(12,44),(24,36),(36,44),(12,44))
        self.relate('connect','stem','bowl');self.relate('connect','stem','foot')
