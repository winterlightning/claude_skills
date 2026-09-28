"""Ice Cream Cart with Umbrella.
Symbol plan: Vending box with umbrella, two wheels and a simple cycle steering post/frame. Bounds (8,4)-(40,44).
Construction reference: Lucide umbrella: dome and pole; supplied cycle cart: box, two wheels and front post.
Reduction: Canopy panel ribs, projecting lid and fine cycle frame details omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9377babb-2c2f-45f6-b15f-554b5fa1d7e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ice cream truck_9377babb-2c2f-45f6-b15f-554b5fa1d7e2.svg'
AUTHOR = 'gpt-6'

class IceCreamCycleCart(Solo48):
    icon_id = 'ice-cream-cycle-cart'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('ice', 'cream', 'cycle', 'cart')

    def build(self):
        self.path('canopy',(20,12),[((20,8),(24,4),(30,4)),((36,4),(40,8),(40,12)),(30,12),(20,12)],True)
        self.add_line('pole',(30,12),(30,20))
        self.add_polyline('box',(24,20),(30,20),(40,20),(40,28),(36,28),(24,28),closed=True)
        for i,x in enumerate((12,36)):self.loop(f'wheel-{i}',x,40,4)
        self.add_polyline('post',(12,36),(12,28),(12,20))
        self.add_polyline('saddle',(8,20),(12,20),(16,20))
        self.add_line('frame',(12,28),(24,28));self.add_line('rear-axle',(36,28),(36,36))
        for a,b in [('pole','canopy'),('pole','box'),('post','saddle'),('post','frame'),('post','wheel-0'),('frame','box'),('rear-axle','box'),('rear-axle','wheel-1')]:self.relate('connect',a,b)

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
