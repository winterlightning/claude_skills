"""Ice Cream Sundae with Cherry.
Symbol plan: Stemmed sundae cup, two scoops, cherry with stem, diagonal spoon. Bounds (8,4)-(40,44).
Construction reference: Lucide ice-cream-bowl: scoops, cup and foot; supplied reference: cherry and left-leaning spoon.
Reduction: Extra scoop divisions omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cd29f28-935b-4556-948b-8d74f8ec867e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ice cream bowl_0cd29f28-935b-4556-948b-8d74f8ec867e.svg'
AUTHOR = 'gpt-6'

class CherryIceCreamSundae(Solo48):
    icon_id = 'cherry-ice-cream-sundae'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('cherry', 'ice', 'cream', 'sundae')

    def build(self):
        for i,x in enumerate((16,32)):
            self.add_arc(f'scoop-{i}-l',(x-8,28),(x,20),radius_x=8)
            self.add_arc(f'scoop-{i}-r',(x,20),(x+8,28),radius_x=8)
            self.add_contour(f'scoop-{i}',f'scoop-{i}-l',f'scoop-{i}-r')
        self.add_polyline('rim',(8,28),(24,28),(40,28))
        self.path('cup',(8,28),[((8,34),(16,36),(24,36)),((32,36),(40,34),(40,28))])
        self.loop('cherry',28,8,2)
        self.path('cherry-stem',(28,6),[((28,4),(30,4),(32,4))])
        self.add_line('spoon',(8,4),(16,20));self.add_line('stem',(24,36),(24,44))
        self.add_polyline('foot',(14,44),(24,44),(34,44))
        for a,b in [('scoop-0','rim'),('scoop-1','rim'),('scoop-0','scoop-1'),('cup','rim'),('cup','scoop-0'),('cup','scoop-1'),('spoon','scoop-0'),('cherry','cherry-stem'),('stem','cup'),('stem','foot')]:self.relate('connect',a,b)

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
