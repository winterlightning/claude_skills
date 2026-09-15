"""Zeus with long hair, a robe and a lightning bolt above his hand. Lucide zap informs the sharp zigzag; user-round informs the simple figure. Omit facial details and garment folds."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '339413a2-9f25-4881-9b93-a087f3da321c'
SOURCE_PATH = 'pictographic-primitives/religion/zeus_339413a2-9f25-4881-9b93-a087f3da321c.svg'
AUTHOR = 'gpt-6'

class ZeusWithLightningBolt(Solo48):
    icon_id = 'zeus-with-lightning-bolt'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('zeus', 'lightning', 'bolt', 'greek', 'god', 'mythology', 'figure')

    def oval(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (8,4)-(40,44); bolt and arm extend to the right.
        self.oval('head',15,10,6)
        self.add_line('hair',(9,10),(8,20));self.relate('connect','head','hair')
        self.add_polyline('gown',(13,27),(8,44),(27,44),(25,34),(23,27),(13,27))
        self.add_polyline('arm',(25,34),(31,34),(31,28));self.relate('connect','arm','gown')
        self.add_polyline('bolt',(40,4),(28,18),(39,18),(31,28))
        self.relate('connect','bolt','arm')
