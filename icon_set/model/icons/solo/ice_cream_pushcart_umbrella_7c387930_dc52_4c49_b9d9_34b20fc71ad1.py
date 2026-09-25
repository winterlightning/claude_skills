"""Ice Cream Cart with Umbrella.
Symbol plan: Broad umbrella over a one-wheel cart, left leg and right push handle. Bounds (6,6)-(42,42).
Construction reference: Lucide umbrella: broad continuous dome; supplied reference: single wheel, support leg and handle.
Reduction: Four canopy scallops reduced to two; small ribs omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c387930-dc52-4c49-b9d9-34b20fc71ad1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ice cream stand_7c387930-dc52-4c49-b9d9-34b20fc71ad1.svg'
AUTHOR = 'gpt-6'

class IceCreamPushcartUmbrella(Solo48):
    icon_id = 'ice-cream-pushcart-umbrella'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'pushcart', 'umbrella')

    def build(self):
        self.path('canopy',(6,16),[((6,11),(14,6),(24,6)),((34,6),(42,11),(42,16)),((38,20),(28,20),(24,16)),((20,20),(10,20),(6,16))],True)
        self.add_line('pole',(24,16),(24,28))
        self.path('box',(24,36),[(8,36),(8,28),(24,28),(36,28),(36,36)])
        self.loop('wheel',36,39,3)
        self.add_line('leg',(8,36),(8,42));self.add_line('handle',(36,28),(42,25))
        for a,b in [('pole','canopy'),('pole','box'),('leg','box'),('handle','box'),('wheel','box')]:self.relate('connect',a,b)

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
