"""Kitchen Dough Rolling Pin.
Symbol plan: Diagonal long barrel with matching single-stroke handles. Bounds (6,6)-(42,42); diagonal preserves a narrow barrel at SOLO48.
Construction reference: Supplied rolling pin; Lucide utensils simple handle treatment.
Reduction: Narrow handle outlines reduced to single strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffc638d5-81ce-551c-a6ed-c0d843df166c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/roller_ffc638d5-81ce-551c-a6ed-c0d843df166c.svg'
AUTHOR = 'gpt-6'

class KitchenDoughRollingPin(Solo48):
    icon_id = 'kitchen-dough-rolling-pin'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('kitchen', 'dough', 'rolling', 'pin')

    def build(self):
        self.path('barrel',(12,26),[(26,12),((28,10),(30,10),(32,12)),(34,14),(36,16),((38,18),(38,20),(36,22)),(22,36),((20,38),(18,38),(16,36)),(14,34),(12,32),((10,30),(10,28),(12,26))],True)
        self.add_line('left',(14,34),(6,42));self.relate('connect','left','barrel')
        self.add_line('right',(34,14),(42,6));self.relate('connect','right','barrel')

    def path(self, name, start, commands, closed=False):
        members=[]
        for j,c in enumerate(commands):
            tag=f'{name}-{j}'
            if len(c)==2:self.add_line(tag,start,c);start=c
            else:self.add_bezier(tag,start,c);start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def loop(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-r',(x,y-ry),(x,y+ry),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-l',(x,y+ry),(x,y-ry),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-r',name+'-l',closed=True)

    def steam(self,x,top,bottom,name):
        mid=(top+bottom)//2
        self.add_bezier(name,(x+1,top),((x-2,top+2),(x-2,mid),(x,mid)),((x+2,mid),(x+2,bottom-2),(x-1,bottom)))
