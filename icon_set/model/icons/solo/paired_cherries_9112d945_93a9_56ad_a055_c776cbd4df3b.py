"""Pair of Cherries.
Symbol plan: Two equal cherry circles and converging stems. Bounds (4,8)-(44,40).
Construction reference: Supplied cherries; Lucide cherry rounded fruits and shared stem junction.
Reduction: Small top notches omitted; straight and curved stem distinction retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9112d945-93a9-56ad-a055-c776cbd4df3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cherry_9112d945-93a9-56ad-a055-c776cbd4df3b.svg'
AUTHOR = 'gpt-6'

class PairedCherries(Solo48):
    icon_id = 'paired-cherries'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('paired', 'cherries')

    def build(self):
        for name,x in [('left',11),('right',37)]:self.loop(name,x,33,7)
        join=(24,8)
        self.add_line('left-stem',(11,26),join);self.relate('connect','left-stem','left')
        self.add_bezier('right-stem',join,((35,10),(37,18),(37,26)));self.relate('connect','right-stem','right');self.relate('connect','left-stem','right-stem')

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
