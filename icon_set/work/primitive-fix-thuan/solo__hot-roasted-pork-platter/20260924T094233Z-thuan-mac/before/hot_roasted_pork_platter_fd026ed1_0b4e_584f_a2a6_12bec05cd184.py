"""Hot Roasted Pork Platter.
Symbol plan: Left-facing pig head on tapered platter, with pointed ear, snout and two steam curls. Bounds (4,8)-(44,40).
Construction reference: Supplied pork platter; Lucide soup for separated steam.
Reduction: Eye and garnish omitted to preserve the pig head and plate spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd026ed1-0b4e-584f-a2a6-12bec05cd184'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/barbeque sucking pork roasted_fd026ed1-0b4e-584f-a2a6-12bec05cd184.svg'
AUTHOR = 'gpt-6'

class HotRoastedPorkPlatter(Solo48):
    icon_id = 'hot-roasted-pork-platter'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('hot', 'roasted', 'pork', 'platter')

    def build(self):
        self.path('pig',(12,32),[(8,23),(14,21),(12,14),(22,23),(30,23),((36,23),(38,27),(38,32))])
        self.path('platter',(4,32),[(12,32),(38,32),(44,32),((44,38),(42,40),(40,40)),(8,40),((4,40),(4,38),(4,32))],True)
        self.relate('connect','pig','platter')
        for i,x in enumerate((28,40)):self.steam(x,8,14,f'steam-{i}')

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
