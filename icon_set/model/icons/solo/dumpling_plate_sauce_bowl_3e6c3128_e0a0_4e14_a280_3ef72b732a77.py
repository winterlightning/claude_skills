"""Plate of Dumplings with Sauce Bowl.
Symbol plan: Two plump dumplings on broad plate and separate sauce bowl at upper left. Bounds (4,8)-(44,40).
Construction reference: Supplied dumpling serving; Lucide soup bowl and shallow serving contours.
Reduction: Cluster reduced to two dumplings; sauce opening simplified to one rim.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e6c3128-e0a0-4e14-a280-3ef72b732a77'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear taco plate_3e6c3128-e0a0-4e14-a280-3ef72b732a77.svg'
AUTHOR = 'gpt-6'

class DumplingPlateSauceBowl(Solo48):
    icon_id = 'dumpling-plate-sauce-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('dumpling', 'plate', 'sauce', 'bowl')

    def build(self):
        self.add_line('sauce-rim',(4,8),(20,8));self.add_arc('sauce',(20,8),(4,8),radius_x=8);self.relate('connect','sauce-rim','sauce')
        for j,x in enumerate((23,37)):
         self.add_arc('dumpling-'+str(j),(x-7,30),(x+7,30),radius_x=7)
        self.add_polyline('front',(16,30),(30,30),(44,30))
        for j in range(2):self.relate('connect','dumpling-'+str(j),'front')
        self.relate('connect','dumpling-0','dumpling-1')
        self.path('plate',(16,30),[(4,30),((4,37),(12,40),(24,40)),((36,40),(44,37),(44,30))]);self.relate('connect','plate','front')
        for j in range(2):self.relate('connect','plate','dumpling-'+str(j))

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
