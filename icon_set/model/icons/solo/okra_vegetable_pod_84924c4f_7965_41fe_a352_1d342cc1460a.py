"""Okra Vegetable Pod.
Symbol plan: Diagonal pointed pod, central ridge and short upper-right stem. Bounds (6,6)-(42,42).
Construction reference: Supplied okra; Lucide bean smooth continuous vegetable outline.
Reduction: Multiple long ridges reduced to one; direction and pointed tip retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84924c4f-7965-41fe-a352-1d342cc1460a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/okra_84924c4f-7965-41fe-a352-1d342cc1460a.svg'
AUTHOR = 'gpt-6'

class OkraVegetablePod(Solo48):
    icon_id = 'okra-vegetable-pod'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('okra', 'vegetable', 'pod')

    def build(self):
        self.path('pod',(6,42),[((6,10),(22,6),(34,14)),((42,26),(38,42),(6,42))],True)
        self.add_line('ridge',(6,42),(34,14));self.relate('connect','ridge','pod')
        self.add_line('stem',(34,14),(42,6));self.relate('connect','stem','pod');self.relate('connect','stem','ridge')

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
