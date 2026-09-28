"""Ice Cream Cart with Umbrella.
Symbol plan: Broad umbrella over a one-wheel cart, left leg and right push handle. Bounds (6,6)-(42,42).
Construction reference: Lucide umbrella: broad continuous dome; supplied reference: single wheel, support leg and handle.
Reduction: Four source scallops retained; small ribs omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7c387930-dc52-4c49-b9d9-34b20fc71ad1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ice-cream-pushcart-umbrella/20260927T145836Z-thuan-mac-1/reference/ice cream stand_7c387930-dc52-4c49-b9d9-34b20fc71ad1.svg'
AUTHOR = 'gpt-6'

class IceCreamPushcartUmbrella(Solo48):
    icon_id = 'ice-cream-pushcart-umbrella'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('ice', 'cream', 'pushcart', 'umbrella')

    def build(self):
        # Four small scallops and a central cusp follow the market umbrella.
        self.path('canopy',(6,16),[((6,11),(14,6),(24,6)),((34,6),(42,11),(42,16)),((41,20),(35,20),(33,16)),((31,20),(26,20),(24,16)),((22,20),(17,20),(15,16)),((13,20),(7,20),(6,16))],True)
        self.add_line('pole',(24,16),(24,28))
        self.path('box',(24,36),[(8,36),(8,28),(24,28),(36,28),(36,36)])
        self.loop('wheel',36,39,3)
        self.add_line('leg',(8,36),(8,42));self.add_line('handle',(36,28),(42,27))
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
