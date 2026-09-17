"""Meat Tenderizer Mallet.
Symbol plan: Diagonal rectangular mallet head with central long handle. Bounds (6,6)-(42,42).
Construction reference: Supplied tenderizer; Lucide hammer diagonal head and grip relationship.
Reduction: Handle outline simplified; head is broad and flat-ended rather than clawed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec913abd-42a3-4770-bf57-4fa619dc8c64'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hammer meat_ec913abd-42a3-4770-bf57-4fa619dc8c64.svg'
AUTHOR = 'gpt-6'

class MeatTenderizerMallet(Solo48):
    icon_id = 'meat-tenderizer-mallet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('meat', 'tenderizer', 'mallet')

    def build(self):
        self.add_polyline('head',(24,6),(42,24),(32,34),(23,25),(14,16),closed=True)
        self.add_line('handle',(23,25),(6,42));self.relate('connect','handle','head')

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
