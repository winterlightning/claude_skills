"""Japanese Takoyaki Octopus Balls.
Symbol plan: Two lower balls and one upper ball in tapered tray; leaning pick. Bounds (6,6)-(42,42).
Construction reference: Supplied takoyaki tray; Lucide cooking-pot broad rim.
Reduction: Sauce and enlarged pick handle omitted to keep three balls legible.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6045185a-12f6-4637-8a15-3895152cec03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/japanese takoyagi squid ball_6045185a-12f6-4637-8a15-3895152cec03.svg'
AUTHOR = 'gpt-6'

class TakoyakiOctopusBallTray(Solo48):
    icon_id = 'takoyaki-octopus-ball-tray'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('takoyaki', 'octopus', 'ball', 'tray')

    def build(self):
        self.path('tray',(6,31),[(24,31),(42,31),(39,42),(9,42),(6,31)],True)
        for name,x in [('left',15),('right',33)]:
         self.add_arc(name+'-a',(x-9,31),(x,22),radius_x=9);self.add_arc(name+'-b',(x,22),(x+9,31),radius_x=9);self.add_contour(name,name+'-a',name+'-b');self.relate('connect',name,'tray')
        self.relate('connect','left','right')
        self.add_arc('top',(15,22),(33,22),radius_x=9)
        for n in ('left','right'):self.relate('connect','top',n)
        self.add_line('pick',(33,22),(39,6));self.relate('connect','pick','top');self.relate('connect','pick','right')

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
