"""Maki Sushi Roll.
Symbol plan: Oval top, deep cylindrical side and single central filling mark. Bounds (4,8)-(44,40).
Construction reference: Supplied maki; Lucide citrus for concentric food sections.
Reduction: Filling subdivisions reduced to one central dot; oval rice band and sidewall retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8191fbcc-d413-5591-9281-98daa81149be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/americanized sushi roll_8191fbcc-d413-5591-9281-98daa81149be.svg'
AUTHOR = 'gpt-6'

class MakiSushiRollSection(Solo48):
    icon_id = 'maki-sushi-roll-section'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('maki', 'sushi', 'roll', 'section')

    def build(self):
        axis=24
        self.add_arc('top-upper',(4,17),(44,17),radius_x=20,radius_y=9)
        self.add_arc('top-lower',(44,17),(4,17),radius_x=20,radius_y=9)
        self.add_contour('top','top-upper','top-lower',closed=True)
        self.path('side',(4,17),[(4,28),((4,35),(13,40),(axis,40)),((35,40),(44,35),(44,28)),(44,17)]);self.relate('connect','side','top')
        self.add_dot('filling',(axis,17))

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
