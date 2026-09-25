"""Noodle Takeout Box with Chopsticks.
Symbol plan: Tapered carton with flaps, paired chopsticks and hanging noodle. Bounds (6,6)-(42,42).
Construction reference: Supplied noodle carton; Lucide utensils for simple repeated sticks.
Reduction: Two noodle strands reduced to one; box handle retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e73788f8-3382-5a41-b2fa-433d13f548b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/boxed noodle_e73788f8-3382-5a41-b2fa-433d13f548b2.svg'
AUTHOR = 'gpt-6'

class NoodleTakeoutBoxChopsticks(Solo48):
    icon_id = 'noodle-takeout-box-chopsticks'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('noodle', 'takeout', 'box', 'chopsticks')

    def build(self):
        self.add_polyline('box',(8,24),(18,24),(20,24),(30,24),(40,24),(36,42),(12,42),closed=True)
        for side,x,end in [('left',8,6),('right',40,42)]:self.add_line(side,(x,24),(end,32));self.relate('connect',side,'box')
        for j,y in enumerate((6,14)):self.add_line('stick-'+str(j),(14,y),(42,y))
        self.add_bezier('noodle',(14,14),((12,18),(20,20),(20,24)));self.relate('connect','noodle','stick-1');self.relate('connect','noodle','box')
        self.add_arc('handle',(30,24),(18,24),radius_x=6);self.relate('connect','handle','box')

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
