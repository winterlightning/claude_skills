"""A broad chalice on a stem and flared foot. Lucide wine informs the coherent bowl, stem and foot; omit decorative stem beads."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '188e9da1-e301-5033-8cca-278e325932fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__greek-stemmed-chalice/20260927T032104Z-thuan-mac-1/reference/greek grail_188e9da1-e301-5033-8cca-278e325932fc.svg'
AUTHOR = "gpt-6"

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
        # Wide bowl, distinct inner band, and a stem flowing into a flared foot.
        self.add_polyline('rim', (8, 4), (40, 4), (40, 12))
        self.add_arc('bowl-right', (40, 12), (24, 28), radius_x=16)
        self.add_arc('bowl-left', (24, 28), (8, 12), radius_x=16)
        self.add_line('rim-left', (8, 12), (8, 4))
        self.add_contour('bowl', 'bowl-right', 'bowl-left', 'rim-left')
        self.relate('connect', 'bowl', 'rim')
        self.add_line('band', (8, 12), (40, 12))
        self.relate('connect', 'band', 'rim')
        self.relate('connect', 'band', 'bowl')
        self.add_line('stem', (24, 28), (24, 34))
        self.add_bezier('foot-left', (24, 34), ((24, 39), (18, 42), (12, 44)))
        self.add_line('foot-base', (12, 44), (36, 44))
        self.add_bezier('foot-right', (36, 44), ((30, 42), (24, 39), (24, 34)))
        self.add_contour('foot', 'foot-left', 'foot-base', 'foot-right', closed=True)
        self.relate('connect', 'stem', 'bowl')
        self.relate('connect', 'stem', 'foot')
