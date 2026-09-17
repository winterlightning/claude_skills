"""Pair of Oven Mitts.
Symbol plan: Large front mitt with cuff and occluded second mitt to right. Bounds (6,6)-(42,42).
Construction reference: Supplied mitts; no useful direct Lucide protective-mitt match.
Reduction: Rear cuff, hidden thumb and fabric marks omitted; front thumb and two rounded finger sections retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '825c63ec-9d55-4ce1-a285-799a738dd8f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/chef gear gloves_825c63ec-9d55-4ce1-a285-799a738dd8f2.svg'
AUTHOR = 'gpt-6'

class PairedOvenMitt(Solo48):
    icon_id = 'paired-oven-mitt'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('paired', 'oven', 'mitt')

    def build(self):
        self.path('front',(6,18),[(6,33),(6,42),(26,42),(26,33),(32,24),((32,18),(26,17),(24,24)),(24,16),((24,10),(20,6),(14,6)),((8,6),(6,10),(6,18))],True)
        self.add_line('cuff',(6,33),(26,33));self.relate('connect','cuff','front')
        self.path('back',(24,16),[((26,8),(32,8),(34,8)),((40,8),(42,14),(42,22)),(42,30),(38,42),(26,42)]);self.relate('connect','back','front')

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
