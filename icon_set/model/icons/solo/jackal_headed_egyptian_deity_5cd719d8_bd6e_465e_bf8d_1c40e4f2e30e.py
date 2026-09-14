"""A right-facing jackal deity with upright ear, long muzzle and hanging headdress. Remove fine folds; preserve the directional animal profile."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cd719d8-bd6e-465e-bf8d-1c40e4f2e30e'
SOURCE_PATH = 'pictographic-primitives/religion/egyptian mythology_5cd719d8-bd6e-465e-bf8d-1c40e4f2e30e.svg'
AUTHOR = 'gpt-6'


class JackalHeadedEgyptianDeity(Solo48):
    icon_id = 'jackal-headed-egyptian-deity'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('egyptian', 'deity', 'jackal', 'head', 'headdress', 'mythology', 'profile')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Square envelope, a coherent asymmetric jackal silhouette.
        self.add_polyline('ear-and-muzzle',(6,42),(6,26),(12,18),(8,6),(21,18),(28,18),(34,23),(42,23),(37,33),(29,33),(29,42),(20,42),(17,33),(6,42))
        self.add_line('shoulder',(29,42),(40,42))
        self.relate('connect','ear-and-muzzle','shoulder')
