"""Kitchen Extractor Hood.
Symbol plan: Central chimney and sloping canopy over three matching steam waves. Bounds (8,4)-(40,44).
Construction reference: Supplied extractor; Lucide cooking-pot broad lid construction.
Reduction: Lower double band omitted; short steam tails keep clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65a44733-2f8b-5ccc-a771-fa0b05c22d32'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/aspirator_65a44733-2f8b-5ccc-a771-fa0b05c22d32.svg'
AUTHOR = 'gpt-6'

class KitchenExtractorHood(Solo48):
    icon_id = 'kitchen-extractor-hood'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('kitchen', 'extractor', 'hood')

    def build(self):
        self.add_polyline('chimney',(16,18),(16,4),(32,4),(32,18))
        self.add_polyline('hood',(16,18),(8,28),(40,28),(32,18),(16,18));self.relate('connect','chimney','hood')
        for j,x in enumerate((14,24,34)):self.add_bezier('steam-'+str(j),(x,44),((x-2,42),(x+2,39),(x,37)))

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
