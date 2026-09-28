"""Steam locomotive; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ebc729b-ff9e-4e94-8fec-0513c51573fe'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad locomotive_8ebc729b-ff9e-4e94-8fec-0513c51573fe.svg'
AUTHOR = 'gpt-6'

class SteamLocomotive(Solo48):
    icon_id = 'steam-locomotive'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('steam locomotive', 'train', 'locomotive', 'railway', 'vintage', 'engine', 'rail', 'chimney')

    def build(self) -> None:
        def wheel(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)
        # HRECT_L (6,8)-(42,40). Asymmetric cab, boiler, funnel and unequal wheels.
        self.add_polyline('engine',(4,28),(4,8),(20,8),(20,18),(30,18),(36,18),(36,28),(36,32),(34,32))
        self.add_polyline('cab-floor',(4,28),(16,28),(20,28),(20,18))
        self.relate('connect','engine','cab-floor')
        self.add_line('chimney',(30,18),(30,8))
        self.add_polyline('chimney-rim',(26,8),(30,8),(34,8))
        self.relate('connect','chimney','engine')
        self.relate('connect','chimney','chimney-rim')
        wheel('rear-wheel',16,34,6)
        wheel('front-wheel',34,36,4)
        self.relate('connect','rear-wheel','cab-floor')
        self.relate('connect','front-wheel','engine')
        self.add_polyline('rail',(4,40),(16,40),(34,40),(44,40))
        self.relate('connect','rail','rear-wheel')
        self.relate('connect','rail','front-wheel')

