"""Kitchen Stand Mixer.
Symbol plan: Open C-shaped stand with broad motor and hanging teardrop whisk. Bounds (6,6)-(42,42).
Construction reference: Supplied open stand mixer; Lucide paintbrush smooth continuous shoulder construction.
Reduction: Whisk inner wire omitted; loop and shaft carry identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b53d460e-16c9-4f56-841a-186933b2d151'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/stand alone mixer_b53d460e-16c9-4f56-841a-186933b2d151.svg'
AUTHOR = 'gpt-6'

class KitchenStandMixerWhisk(Solo48):
    icon_id = 'kitchen-stand-mixer-whisk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('kitchen', 'stand', 'mixer', 'whisk')

    def build(self):
        self.path('head',(15,6),[(33,6),((39,6),(42,9),(42,16)),(15,16),(6,16),((6,9),(9,6),(15,6))],True)
        self.add_polyline('stand',(42,16),(42,42),(6,42));self.relate('connect','stand','head')
        self.add_line('shaft',(15,16),(15,22));self.relate('connect','shaft','head')
        self.path('whisk',(15,22),[((11,26),(9,27),(9,29)),((9,34),(21,34),(21,29)),((21,27),(19,26),(15,22))],True);self.relate('connect','shaft','whisk')

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
