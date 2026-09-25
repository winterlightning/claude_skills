"""Popsicle Ice Cream Bar.
Symbol plan: Rounded popsicle, two matching grooves and central stick. Bounds (8,4)-(40,44).
Construction reference: Supplied popsicle; Lucide popsicle rounded ice body and simple stick.
Reduction: Long grooves shortened to preserve cap and base clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a87af899-140a-41c3-84df-64415d40b167'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ice cream stick_a87af899-140a-41c3-84df-64415d40b167.svg'
AUTHOR = 'gpt-6'

class PopsicleTwinGroove(Solo48):
    icon_id = 'popsicle-twin-groove'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('popsicle', 'twin', 'groove')

    def build(self):
        axis=24
        self.path('bar',(8,16),[((8,8),(16,4),(axis,4)),((32,4),(40,8),(40,16)),(40,31),((40,34),(39,35),(36,35)),(axis,35),(12,35),((9,35),(8,34),(8,31)),(8,16)],True)
        for j,x in enumerate((18,30)):self.add_line('groove-'+str(j),(x,15),(x,25))
        self.add_line('stick',(axis,35),(axis,44));self.relate('connect','stick','bar')

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
