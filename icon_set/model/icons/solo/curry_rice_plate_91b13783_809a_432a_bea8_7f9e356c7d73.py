"""Plate of Curry and Rice.
Symbol plan: Concentric plate and food area, divided by a shallow wave. Radius20 centered24.
Construction reference: Supplied curry and rice; Lucide citrus concentric food sections.
Reduction: None; two food regions and broad plate rim remain.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91b13783-809a-432a-bea8-7f9e356c7d73'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/curry rice_91b13783-809a-432a-bea8-7f9e356c7d73.svg'
AUTHOR = 'gpt-6'

class CurryRicePlate(Solo48):
    icon_id = 'curry-rice-plate'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('curry', 'rice', 'plate')

    def build(self):
        axis=24
        self.loop('plate',axis,axis,20);self.loop('food',axis,axis,11)
        self.add_bezier('division',(axis,13),((18,19),(30,29),(axis,35)));self.relate('connect','division','food')

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
