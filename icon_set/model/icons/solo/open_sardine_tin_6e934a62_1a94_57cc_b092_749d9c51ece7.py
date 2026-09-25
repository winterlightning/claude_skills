"""Open Sardine Can.
Symbol plan: Rounded tin with rolled lid on right and one exposed fish. Bounds (4,10)-(44,38).
Construction reference: Supplied sardine tin; Lucide fish tapered body and forked tail.
Reduction: Two fish reduced to one; cramped pull-tab omitted; rolled lid division retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e934a62-1a94-57cc-b092-749d9c51ece7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/sardine can_6e934a62-1a94-57cc-b092-749d9c51ece7.svg'
AUTHOR = 'gpt-6'

class OpenSardineTin(Solo48):
    icon_id = 'open-sardine-tin'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('open', 'sardine', 'tin')

    def build(self):
        self.path('tin',(10,10),[(34,10),(38,10),((42,10),(44,12),(44,16)),(44,32),((44,36),(42,38),(38,38)),(34,38),(10,38),((6,38),(4,36),(4,32)),(4,16),((4,12),(6,10),(10,10))],True)
        self.add_line('lid',(34,10),(34,38));self.relate('connect','lid','tin')
        self.path('fish',(16,24),[((22,17),(25,18),(25,24)),((25,30),(22,31),(16,24))],True)
        self.add_polyline('tail',(13,21),(16,24),(13,27));self.relate('connect','tail','fish')

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
