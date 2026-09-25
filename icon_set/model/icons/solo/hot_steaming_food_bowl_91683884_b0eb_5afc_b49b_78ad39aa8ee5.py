"""Hot Steaming Food Bowl.
Symbol plan: Oval opening, round bowl underside, three equal steam curls. Bounds (6,6)-(42,42).
Construction reference: Lucide soup: smooth bowl and repeated steam; source oval rim preserved.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91683884-b0eb-5afc-b49b-78ad39aa8ee5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pasta bowl warm_91683884-b0eb-5afc-b49b-78ad39aa8ee5.svg'
AUTHOR = 'gpt-6'

class HotSteamingFoodBowl(Solo48):
    icon_id = 'hot-steaming-food-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('hot', 'steaming', 'food', 'bowl')

    def build(self):
        axis = 24  # Mirror pairs derive from a shared vertical axis.
        self.add_arc('rim-top',(axis-18,26),(axis+18,26),radius_x=18,radius_y=4)
        self.add_arc('rim-front',(axis+18,26),(axis-18,26),radius_x=18,radius_y=4)
        self.add_contour('rim','rim-top','rim-front',closed=True)
        self.path('bowl',(axis-18,26),[((axis-18,36),(axis-10,42),(axis+0,42)),((axis+10,42),(axis+18,36),(axis+18,26))])
        self.relate('connect','rim','bowl')
        for i,x in enumerate((axis-12,24,36)):self.steam(x,6,14,f'steam-{i}')

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
