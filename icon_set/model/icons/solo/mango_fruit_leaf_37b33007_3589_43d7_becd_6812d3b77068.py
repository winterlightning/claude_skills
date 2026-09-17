"""Mango Fruit with Leaf.
Symbol plan: Offset mango body, upper-right shoulder and pointed leaf above. Bounds (6,6)-(42,42).
Construction reference: Supplied mango; no useful direct Lucide match.
Reduction: No leaf vein; uneven shoulder and broad drooping fruit retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37b33007-3589-43d7-becd-6812d3b77068'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/mango_37b33007-3589-43d7-becd-6812d3b77068.svg'
AUTHOR = 'gpt-6'

class MangoFruitLeaf(Solo48):
    icon_id = 'mango-fruit-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('mango', 'fruit', 'leaf')

    def build(self):
        self.path('fruit',(32,17),[((39,19),(42,25),(42,30)),((42,38),(32,42),(22,42)),((13,42),(6,39),(6,34)),((6,28),(13,27),(18,23)),((23,19),(26,17),(32,17))],True)
        self.path('leaf',(32,17),[((21,19),(15,13),(14,6)),((23,6),(30,9),(32,17))],True);self.relate('connect','leaf','fruit')
        self.add_line('stem',(32,17),(37,8));self.relate('connect','stem','fruit');self.relate('connect','stem','leaf')

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
