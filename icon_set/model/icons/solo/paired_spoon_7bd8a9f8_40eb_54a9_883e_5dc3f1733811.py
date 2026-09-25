"""Pair of Spoons.
Symbol plan: Identical oval spoon bowls and long stems from one series. Bounds (8,4)-(40,44).
Construction reference: Supplied spoon pair; Lucide utensils single-line handles and rounded bowls.
Reduction: Handle outlines and widened grip tips reduced to plain stems.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bd8a9f8-40eb-54a9-883e-5dc3f1733811'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/spoon set_7bd8a9f8-40eb-54a9-883e-5dc3f1733811.svg'
AUTHOR = 'gpt-6'

class PairedSpoon(Solo48):
    icon_id = 'paired-spoon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('paired', 'spoon')

    def build(self):
        for j,x in enumerate((13,35)):
         self.loop('bowl-'+str(j),x,14,5,10)
         self.add_line('handle-'+str(j),(x,24),(x,44));self.relate('connect','handle-'+str(j),'bowl-'+str(j))

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
