"""A standing shaman with branching antlers and raised arms. Keep round head, antlers and spread stance; omit redundant tines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b77ac2e9-85d4-43f9-97bb-8e44e6d4df95'
SOURCE_PATH = 'pictographic-primitives/religion/shaman_b77ac2e9-85d4-43f9-97bb-8e44e6d4df95.svg'
AUTHOR = 'gpt-6'

class AntleredShamanFigure(Solo48):
    icon_id = 'antlered-shaman-figure'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    categories = ("primitives", "religion")
    aliases = ()
    keywords = ('shaman', 'antler', 'figure', 'ritual', 'horn', 'person')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (6,6)-(42,42), mirrored gestures and antlers.
        self.oval('head',24,16,5)
        self.add_polyline('body',(24,21),(24,26),(24,31))
        self.relate('connect','head','body')
        self.add_polyline('legs',(11,42),(24,31),(37,42));self.relate('connect','body','legs')
        self.add_polyline('arms',(8,22),(15,28),(24,26),(33,28),(40,22));self.relate('connect','arms','body')
        for side in (-1,1):
         self.add_polyline('antler-'+str(side),(24+side*5,16),(24+side*10,16),(24+side*18,12),(24+side*18,6))
         self.add_line('tine-'+str(side),(24+side*10,16),(24+side*10,8))
         self.relate('connect','head','antler-'+str(side));self.relate('connect','antler-'+str(side),'tine-'+str(side))
