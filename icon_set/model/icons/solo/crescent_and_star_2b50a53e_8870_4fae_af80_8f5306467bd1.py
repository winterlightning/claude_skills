"""A right-opening crescent beside a five-pointed star, an established religious symbol. Lucide moon informs the coherent outer and inner lunar arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b50a53e-8870-4fae-af80-8f5306467bd1'
SOURCE_PATH = 'pictographic-primitives/religion/islam_2b50a53e-8870-4fae-af80-8f5306467bd1.svg'
AUTHOR = 'gpt-6'

class CrescentAndStar(Solo48):
    icon_id = 'crescent-and-star'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    categories = ("primitives", "religion")
    aliases = ()
    keywords = ('crescent', 'star', 'islam', 'moon', 'symbol', 'religion')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (6,6)-(42,42).
        self.add_arc('moon-outer-top',(24,6),(6,24),radius_x=18,sweep=False)
        self.add_arc('moon-outer-bottom',(6,24),(24,42),radius_x=18,sweep=False)
        self.add_arc('moon-inner',(24,42),(24,6),radius_x=24)
        self.add_contour('crescent','moon-outer-top','moon-outer-bottom','moon-inner',closed=True)
        self.add_polyline('star',(34,16),(36,21),(42,22),(38,26),(39,32),(34,29),(29,32),(30,26),(26,22),(32,21),closed=True)
