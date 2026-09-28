"""Plate and Fork.
Symbol plan: Plain plate and upright two-tine fork. Bounds (4,8)-(44,40).
Construction reference: Supplied plate and fork; Lucide utensils curved fork shoulders and straight handle.
Reduction: Three tines reduced to two for clear tine separation; plain circular plate retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8a63c5c-caf1-441f-8678-fb2e81e65bdf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/preparation_a8a63c5c-caf1-441f-8678-fb2e81e65bdf.svg'
AUTHOR = 'gpt-6'

class DiningPlateFork(Solo48):
    icon_id = 'dining-plate-fork'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('dining', 'plate', 'fork')

    def build(self):
        self.loop('plate',14,24,10)
        self.path('fork',(34,8),[(34,20),((34,24),(36,26),(39,26)),((42,26),(44,24),(44,20)),(44,8)])
        self.add_line('handle',(39,26),(39,40));self.relate('connect','handle','fork')

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
