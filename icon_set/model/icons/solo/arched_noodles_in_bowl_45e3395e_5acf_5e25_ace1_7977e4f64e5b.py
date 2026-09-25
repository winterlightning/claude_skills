"""Bowl of Hot Noodles."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45e3395e-5acf-5e25-ace1-7977e4f64e5b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/noodles bowl_45e3395e-5acf-5e25-ace1-7977e4f64e5b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-noodles-in-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('noodle', 'bowl', 'pasta', 'meal', 'kitchen', 'food', 'serving')

    def build(self):
        # Plan: Two nested noodle arches attached to split rim of footed bowl. Lucide soup. Three arches reduced to two, shared center axis. Envelope (6,6)-(42,42).
        xs=(6,8,17,31,40,42);y=24
        for j,(a,b) in enumerate(zip(xs,xs[1:])):self.add_line(f'rim-{j}',(a,y),(b,y))
        self.add_bezier('right',(42,y),((42,34),(36,38),(30,38)))
        self.add_line('fr',(30,38),(30,42));self.add_line('fb',(30,42),(18,42));self.add_line('fl',(18,42),(18,38))
        self.add_bezier('left',(18,38),((12,38),(6,34),(6,y)))
        self.add_contour('bowl',*[f'rim-{j}' for j in range(len(xs)-1)],'right','fr','fb','fl','left',closed=True)

        for i,(l,r,ry) in enumerate(((8,40,18),(17,31,9))):
         self.add_arc(f'noodle-{i}',(l,24),(r,24),radius_x=(r-l)//2,radius_y=ry)
         self.relate('connect',f'noodle-{i}','bowl')
