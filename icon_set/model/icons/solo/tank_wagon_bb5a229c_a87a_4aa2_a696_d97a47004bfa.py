"""Tank wagon; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb5a229c-a87a-4aa2-a696-d97a47004bfa'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad wagon_bb5a229c-a87a-4aa2-a696-d97a47004bfa.svg'
AUTHOR = 'gpt-6'

class TankWagon(Solo48):
    icon_id = 'tank-wagon'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('tank wagon', 'tanker', 'rail car', 'railway', 'freight', 'fuel', 'wagon', 'train')

    def build(self) -> None:
        def wheel(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)
        # HRECT_L (6,8)-(42,40). Capsule tank, raised hatch and one ladder rung.
        self.add_line('tank-top-1', (15, 12), (20, 12))
        self.add_line('tank-top-2', (20, 12), (20, 8))
        self.add_line('tank-top-3', (20, 8), (28, 8))
        self.add_line('tank-top-4', (28, 8), (28, 12))
        self.add_line('tank-top-5', (28, 12), (33, 12))
        self.add_arc('tank-right',(33,12),(33,34),radius_x=11)
        self.add_line('tank-bottom',(33,34),(15,34))
        self.add_arc('tank-lower-left',(15,34),(6,23),radius_x=11)
        self.add_arc('tank-upper-left',(6,23),(15,12),radius_x=11)
        self.add_contour('tank',*[f'tank-top-{i}' for i in range(6,6)],'tank-right','tank-bottom','tank-lower-left','tank-upper-left',closed=True)
        self.add_polyline('ladder-post',(15,12),(15,23),(15,34))
        self.add_line('ladder-rung',(6,23),(15,23))
        self.relate('connect','ladder-post','tank')
        self.relate('connect','ladder-rung','tank')
        self.relate('connect','ladder-post','ladder-rung')
        for name,x in [('rear',15),('front',33)]:
            wheel(name+'-wheel',x,37,3)
            self.relate('connect',name+'-wheel','tank')
        self.relate('connect','rear-wheel','ladder-post')

