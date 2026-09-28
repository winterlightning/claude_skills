"""Honey Dipper with Drip.
Symbol plan: Three diagonal rounded ridge strokes, shared step (6,-6), upper-right handle, lower-left drop. Bounds (6,6)-(42,42).
Construction reference: Supplied honey dipper; Lucide croissant for distinct rounded ribs.
Reduction: Ridge outlines reduced to three broad strokes; diagonal handle retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '938032ae-5024-5ede-94da-88527f48269f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/honey_938032ae-5024-5ede-94da-88527f48269f.svg'
AUTHOR = 'gpt-6'

class HoneyDipperDrip(Solo48):
    icon_id = 'honey-dipper-drip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('honey', 'dipper', 'drip')

    def build(self):
        for i in range(3):
            x,y=8+6*i,18-6*i
            if i==2:self.add_polyline(f'ridge-{i}',(x,y),(x+6,y+6),(x+12,y+12))
            else:self.add_line(f'ridge-{i}',(x,y),(x+12,y+12))
        self.add_line('handle',(26,12),(42,6))
        self.relate('connect','handle','ridge-2')
        self.add_bezier('drop-r',(10,32),((10,35),(14,35),(14,38)))
        self.add_arc('drop-base',(14,38),(6,38),radius_x=4)
        self.add_bezier('drop-l',(6,38),((6,35),(10,35),(10,32)))
        self.add_contour('drop','drop-r','drop-base','drop-l',closed=True)

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
