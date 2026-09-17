"""Kitchen Stand Mixer.
Symbol plan: Rounded motor with left support; deep semicircular bowl shares shaft and pedestal axis30. Bounds (8,4)-(40,44).
Construction reference: Supplied bowl mixer; Lucide soup for deep bowl and simple rim.
Reduction: Motor knob and small under-head collar omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9af76bfa-c95a-50a8-81fb-d37928a549c7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/appliances stand alone mixer_9af76bfa-c95a-50a8-81fb-d37928a549c7.svg'
AUTHOR = 'gpt-6'

class KitchenStandMixerBowl(Solo48):
    icon_id = 'kitchen-stand-mixer-bowl'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('kitchen', 'stand', 'mixer', 'bowl')

    def build(self):
        self.path('head',(16,4),[(29,4),((35,4),(38,8),(38,14)),(30,14),(8,14),((8,8),(10,4),(16,4))],True)
        self.add_polyline('stand',(8,14),(8,44),(30,44),(40,44));self.relate('connect','stand','head')
        axis=30
        self.add_polyline('rim',(20,24),(axis,24),(40,24))
        self.add_arc('bowl-left',(20,24),(axis,34),radius_x=10,sweep=False)
        self.add_arc('bowl-right',(axis,34),(40,24),radius_x=10,sweep=False)
        self.add_contour('bowl','bowl-left','bowl-right');self.relate('connect','bowl','rim')
        self.add_line('shaft',(axis,14),(axis,24));self.relate('connect','shaft','head');self.relate('connect','shaft','rim')
        self.add_line('seat',(axis,34),(axis,44));self.relate('connect','seat','bowl');self.relate('connect','seat','stand')

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
