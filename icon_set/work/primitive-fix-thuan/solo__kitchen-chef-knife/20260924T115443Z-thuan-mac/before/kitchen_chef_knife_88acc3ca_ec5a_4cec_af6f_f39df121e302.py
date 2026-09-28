"""Kitchen Chef Knife.
Symbol plan: Diagonal chef blade and rounded narrow handle, shared bolster. Bounds (6,6)-(42,42).
Construction reference: Supplied chef knife; Lucide utensils for characteristic broad blade against narrow grip.
Reduction: Rivets omitted; diagonal direction preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88acc3ca-ec5a-4cec-af6f-f39df121e302'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/knife 1_88acc3ca-ec5a-4cec-af6f-f39df121e302.svg'
AUTHOR = 'gpt-6'

class KitchenChefKnife(Solo48):
    icon_id = 'kitchen-chef-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('kitchen', 'chef', 'knife')

    def build(self):
        self.path('blade',(6,6),[(29,29),(26,32),(23,35),((11,23),(6,17),(6,6))],True)
        self.path('handle',(29,29),[(39,32),((41,34),(42,36),(42,38)),((42,41),(41,42),(38,42)),((36,42),(34,41),(32,39)),(26,32)]);self.relate('connect','handle','blade')

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
