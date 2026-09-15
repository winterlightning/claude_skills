"""Hermes wears a domed helmet with wings above a blank face and shoulders. Lucide user-round informs the face and shoulder hierarchy; omit small feather notches and garment folds."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9dae5c70-c645-5587-b513-02581cd8c48f'
SOURCE_PATH = 'pictographic-primitives/religion/hermes_9dae5c70-c645-5587-b513-02581cd8c48f.svg'
AUTHOR = 'gpt-6'

class HermesWithWingedHelmet(Solo48):
    icon_id = 'hermes-with-winged-helmet'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('hermes', 'helmet', 'wing', 'head', 'greek', 'mythology', 'portrait')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (4,8)-(44,40), shared axis x=24.
        self.add_arc('helmet',(14,19),(34,19),radius_x=10,radius_y=11)
        self.add_line('band',(14,19),(34,19));self.relate('connect','helmet','band')
        self.add_arc('face',(34,19),(14,19),radius_x=10,radius_y=9)
        self.relate('connect','face','helmet');self.relate('connect','face','band')
        self.add_polyline('wing-left',(14,19),(7,17),(4,9),(14,10))
        self.add_polyline('wing-right',(34,19),(41,17),(44,9),(34,10))
        self.relate('connect','wing-left','helmet');self.relate('connect','wing-left','band');self.relate('connect','wing-left','face')
        self.relate('connect','wing-right','helmet');self.relate('connect','wing-right','band');self.relate('connect','wing-right','face')
        self.add_arc('shoulders',(8,40),(40,40),radius_x=16,radius_y=3)
