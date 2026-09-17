"""Opened Spiky Durian Fruit.
Symbol plan: Two jagged shell sections framing oval flesh and short stem. Bounds (6,6)-(42,42).
Construction reference: Supplied opened durian; no useful direct Lucide match.
Reduction: Dense small spikes reduced to six large tips around exposed flesh.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8e7d502-fe5d-4522-a86c-a96b575ac081'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/durian peeled_a8e7d502-fe5d-4522-a86c-a96b575ac081.svg'
AUTHOR = 'gpt-6'

class OpenedSpikyDurian(Solo48):
    icon_id = 'opened-spiky-durian'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('opened', 'spiky', 'durian')

    def build(self):
        self.add_polyline('left-shell',(29,10),(24,6),(19,10),(10,10),(11,16),(6,24),(10,29),(10,38))
        self.add_polyline('right-shell',(10,38),(19,38),(24,42),(29,38),(38,38),(37,30),(42,24),(38,19));self.relate('connect','left-shell','right-shell')
        self.path('flesh',(19,29),[((15,24),(24,15),(29,19)),((33,24),(24,33),(19,29))],True)
        self.add_line('stem',(10,10),(6,6));self.relate('connect','stem','left-shell')

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
