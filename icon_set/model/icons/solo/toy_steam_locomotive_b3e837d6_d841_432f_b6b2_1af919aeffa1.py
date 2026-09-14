"""Toy steam locomotive; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3e837d6-d841-432f-b6b2-1af919aeffa1'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad wagon_b3e837d6-d841-432f-b6b2-1af919aeffa1.svg'
AUTHOR = 'gpt-6'

class ToySteamLocomotive(Solo48):
    icon_id = 'toy-steam-locomotive'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('steam locomotive', 'train', 'toy train', 'locomotive', 'railway', 'vintage', 'engine', 'wheels')

    def build(self) -> None:
        def wheel(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)
        # SQUARE (6,6)-(42,42). Three evenly spaced small round wheels retain the toy identity.
        self.add_line('cab-roof-boiler-1', (6, 6), (20, 6))
        self.add_line('cab-roof-boiler-2', (20, 6), (20, 20))
        self.add_line('cab-roof-boiler-3', (20, 20), (32, 20))
        self.add_arc('boiler-nose',(32,20),(38,26),radius_x=6)
        self.add_line('front-floor-1', (38, 26), (38, 30))
        self.add_line('front-floor-2', (38, 30), (42, 36))
        self.add_line('front-floor-3', (42, 36), (39, 36))
        self.add_line('front-floor-4', (39, 36), (24, 36))
        self.add_line('front-floor-5', (24, 36), (9, 36))
        self.add_line('front-floor-6', (9, 36), (6, 36))
        self.add_line('front-floor-7', (6, 36), (6, 20))
        self.add_line('front-floor-8', (6, 20), (6, 6))
        self.add_contour('body','cab-roof-boiler-1','cab-roof-boiler-2','cab-roof-boiler-3','boiler-nose',*[f'front-floor-{i}' for i in range(6,9)],closed=True)
        self.add_line('window-base',(6,20),(20,20))
        self.add_line('roof-overhang',(20,6),(24,6))
        self.relate('connect','window-base','body')
        self.relate('connect','roof-overhang','body')
        self.add_line('chimney',(32,20),(32,10))
        self.add_polyline('chimney-rim',(30,10),(32,10),(34,10))
        self.relate('connect','chimney','body')
        self.relate('connect','chimney','chimney-rim')
        for j,x in enumerate([9,24,39]):
            wheel('wheel-'+str(j),x,39,3)
            self.relate('connect','wheel-'+str(j),'body')

